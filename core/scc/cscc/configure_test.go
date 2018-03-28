/*

Copyright IBM Corp. 2016 All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

		 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/
package cscc

import (
	"fmt"
	"os"
	"testing"
	"time"

	"github.com/golang/protobuf/proto"
	configtxtest "github.com/ledgerone/fabric-ledgerone/common/configtx/test"
	"github.com/ledgerone/fabric-ledgerone/common/genesis"
	"github.com/ledgerone/fabric-ledgerone/common/localmsp"
	"github.com/ledgerone/fabric-ledgerone/common/mocks/scc"
	"github.com/ledgerone/fabric-ledgerone/common/policies"
	"github.com/ledgerone/fabric-ledgerone/common/tools/configtxgen/encoder"
	genesisconfig "github.com/ledgerone/fabric-ledgerone/common/tools/configtxgen/localconfig"
	"github.com/ledgerone/fabric-ledgerone/core/aclmgmt"
	aclmocks "github.com/ledgerone/fabric-ledgerone/core/aclmgmt/mocks"
	"github.com/ledgerone/fabric-ledgerone/core/aclmgmt/resources"
	"github.com/ledgerone/fabric-ledgerone/core/chaincode"
	"github.com/ledgerone/fabric-ledgerone/core/chaincode/accesscontrol"
	"github.com/ledgerone/fabric-ledgerone/core/chaincode/shim"
	"github.com/ledgerone/fabric-ledgerone/core/common/sysccprovider"
	"github.com/ledgerone/fabric-ledgerone/core/deliverservice"
	"github.com/ledgerone/fabric-ledgerone/core/deliverservice/blocksprovider"
	"github.com/ledgerone/fabric-ledgerone/core/ledger/ledgermgmt"
	"github.com/ledgerone/fabric-ledgerone/core/peer"
	"github.com/ledgerone/fabric-ledgerone/core/policy"
	policymocks "github.com/ledgerone/fabric-ledgerone/core/policy/mocks"
	"github.com/ledgerone/fabric-ledgerone/gossip/api"
	"github.com/ledgerone/fabric-ledgerone/gossip/service"
	"github.com/ledgerone/fabric-ledgerone/msp/mgmt"
	"github.com/ledgerone/fabric-ledgerone/msp/mgmt/testtools"
	peergossip "github.com/ledgerone/fabric-ledgerone/peer/gossip"
	"github.com/ledgerone/fabric-ledgerone/peer/gossip/mocks"
	cb "github.com/ledgerone/fabric-ledgerone/protos/common"
	pb "github.com/ledgerone/fabric-ledgerone/protos/peer"
	"github.com/ledgerone/fabric-ledgerone/protos/utils"
	"github.com/pkg/errors"
	"github.com/spf13/viper"
	"github.com/stretchr/testify/assert"
)

type mockDeliveryClient struct {
}

func (ds *mockDeliveryClient) UpdateEndpoints(chainID string, endpoints []string) error {
	return nil
}

// StartDeliverForChannel dynamically starts delivery of new blocks from ordering service
// to channel peers.
func (ds *mockDeliveryClient) StartDeliverForChannel(chainID string, ledgerInfo blocksprovider.LedgerInfo, f func()) error {
	return nil
}

// StopDeliverForChannel dynamically stops delivery of new blocks from ordering service
// to channel peers.
func (ds *mockDeliveryClient) StopDeliverForChannel(chainID string) error {
	return nil
}

// Stop terminates delivery service and closes the connection
func (*mockDeliveryClient) Stop() {

}

type mockDeliveryClientFactory struct {
}

func (*mockDeliveryClientFactory) Service(g service.GossipService, endpoints []string, mcs api.MessageCryptoService) (deliverclient.DeliverService, error) {
	return &mockDeliveryClient{}, nil
}

var mockAclProvider *aclmocks.MockACLProvider

func TestMain(m *testing.M) {
	msptesttools.LoadMSPSetupForTesting()

	mockAclProvider = &aclmocks.MockACLProvider{}
	mockAclProvider.Reset()

	aclmgmt.RegisterACLProvider(mockAclProvider)

	os.Exit(m.Run())
}

func TestConfigerInit(t *testing.T) {
	e := new(PeerConfiger)
	stub := shim.NewMockStub("PeerConfiger", e)

	if res := stub.MockInit("1", nil); res.Status != shim.OK {
		fmt.Println("Init failed", string(res.Message))
		t.FailNow()
	}
}

func TestConfigerInvokeInvalidParameters(t *testing.T) {
	e := new(PeerConfiger)
	stub := shim.NewMockStub("PeerConfiger", e)

	res := stub.MockInit("1", nil)
	assert.Equal(t, res.Status, int32(shim.OK), "Init failed")

	res = stub.MockInvoke("2", nil)
	assert.Equal(t, res.Status, int32(shim.ERROR), "CSCC invoke expected to fail having zero arguments")
	assert.Equal(t, res.Message, "Incorrect number of arguments, 0")

	args := [][]byte{[]byte("GetChannels")}
	res = stub.MockInvokeWithSignedProposal("3", args, nil)
	assert.Equal(t, res.Status, int32(shim.ERROR), "CSCC invoke expected to fail no signed proposal provided")
	assert.Contains(t, res.Message, "failed authorization check")

	args = [][]byte{[]byte("fooFunction"), []byte("testChainID")}
	res = stub.MockInvoke("5", args)
	assert.Equal(t, res.Status, int32(shim.ERROR), "CSCC invoke expected wrong function name provided")
	assert.Equal(t, res.Message, "Requested function fooFunction not found.")

	mockAclProvider.Reset()
	mockAclProvider.On("CheckACL", resources.CSCC_GetConfigBlock, "testChainID", (*pb.SignedProposal)(nil)).Return(errors.New("Nil SignedProposal"))
	args = [][]byte{[]byte("GetConfigBlock"), []byte("testChainID")}
	res = stub.MockInvokeWithSignedProposal("4", args, nil)
	assert.Equal(t, res.Status, int32(shim.ERROR), "CSCC invoke expected to fail no signed proposal provided")
	assert.Contains(t, res.Message, "Nil SignedProposal")
	mockAclProvider.AssertExpectations(t)
}

func TestConfigerInvokeJoinChainMissingParams(t *testing.T) {
	viper.Set("peer.fileSystemPath", "/tmp/hyperledgertest/")
	os.Mkdir("/tmp/hyperledgertest", 0755)
	defer os.RemoveAll("/tmp/hyperledgertest/")

	e := new(PeerConfiger)
	stub := shim.NewMockStub("PeerConfiger", e)

	if res := stub.MockInit("1", nil); res.Status != shim.OK {
		fmt.Println("Init failed", string(res.Message))
		t.FailNow()
	}

	// Failed path: expected to have at least one argument
	args := [][]byte{[]byte("JoinChain")}
	if res := stub.MockInvoke("2", args); res.Status == shim.OK {
		t.Fatalf("cscc invoke JoinChain should have failed with invalid number of args: %v", args)
	}
}

func TestConfigerInvokeJoinChainWrongParams(t *testing.T) {

	viper.Set("peer.fileSystemPath", "/tmp/hyperledgertest/")
	os.Mkdir("/tmp/hyperledgertest", 0755)
	defer os.RemoveAll("/tmp/hyperledgertest/")

	e := new(PeerConfiger)
	stub := shim.NewMockStub("PeerConfiger", e)

	if res := stub.MockInit("1", nil); res.Status != shim.OK {
		fmt.Println("Init failed", string(res.Message))
		t.FailNow()
	}

	// Failed path: wrong parameter type
	args := [][]byte{[]byte("JoinChain"), []byte("action")}
	if res := stub.MockInvoke("2", args); res.Status == shim.OK {
		t.Fatalf("cscc invoke JoinChain should have failed with null genesis block.  args: %v", args)
	}
}

func TestConfigerInvokeJoinChainCorrectParams(t *testing.T) {
	sysccprovider.RegisterSystemChaincodeProviderFactory(&scc.MocksccProviderFactory{})

	viper.Set("peer.fileSystemPath", "/tmp/hyperledgertest/")
	viper.Set("chaincode.executetimeout", "3s")
	os.Mkdir("/tmp/hyperledgertest", 0755)

	peer.MockInitialize()
	ledgermgmt.InitializeTestEnv()
	defer ledgermgmt.CleanupTestEnv()
	defer os.RemoveAll("/tmp/hyperledgertest/")

	e := new(PeerConfiger)
	stub := shim.NewMockStub("PeerConfiger", e)

	peerEndpoint := "localhost:13611"

	ccStartupTimeout := time.Duration(30000) * time.Millisecond
	ca, _ := accesscontrol.NewCA()
	chaincode.NewChaincodeSupport(peerEndpoint, false, ccStartupTimeout, ca)

	// Init the policy checker
	policyManagerGetter := &policymocks.MockChannelPolicyManagerGetter{
		Managers: map[string]policies.Manager{
			"mytestchainid": &policymocks.MockChannelPolicyManager{MockPolicy: &policymocks.MockPolicy{Deserializer: &policymocks.MockIdentityDeserializer{[]byte("Alice"), []byte("msg1")}}},
		},
	}

	identityDeserializer := &policymocks.MockIdentityDeserializer{[]byte("Alice"), []byte("msg1")}

	e.policyChecker = policy.NewPolicyChecker(
		policyManagerGetter,
		identityDeserializer,
		&policymocks.MockMSPPrincipalGetter{Principal: []byte("Alice")},
	)

	identity, _ := mgmt.GetLocalSigningIdentityOrPanic().Serialize()
	messageCryptoService := peergossip.NewMCS(&mocks.ChannelPolicyManagerGetter{}, localmsp.NewSigner(), mgmt.NewDeserializersManager())
	secAdv := peergossip.NewSecurityAdvisor(mgmt.NewDeserializersManager())
	err := service.InitGossipServiceCustomDeliveryFactory(identity, peerEndpoint, nil, nil, &mockDeliveryClientFactory{}, messageCryptoService, secAdv, nil)
	assert.NoError(t, err)

	// Successful path for JoinChain
	blockBytes := mockConfigBlock()
	if blockBytes == nil {
		t.Fatalf("cscc invoke JoinChain failed because invalid block")
	}
	args := [][]byte{[]byte("JoinChain"), blockBytes}
	sProp, _ := utils.MockSignedEndorserProposalOrPanic("", &pb.ChaincodeSpec{}, []byte("Alice"), []byte("msg1"))
	identityDeserializer.Msg = sProp.ProposalBytes
	sProp.Signature = sProp.ProposalBytes

	// Try fail path with nil block
	res := stub.MockInvokeWithSignedProposal("2", [][]byte{[]byte("JoinChain"), nil}, sProp)
	assert.Equal(t, res.Status, int32(shim.ERROR))

	// Try fail path with block and nil payload header
	payload, _ := proto.Marshal(&cb.Payload{})
	env, _ := proto.Marshal(&cb.Envelope{
		Payload: payload,
	})
	badBlock := &cb.Block{
		Data: &cb.BlockData{
			Data: [][]byte{env},
		},
	}
	badBlockBytes := utils.MarshalOrPanic(badBlock)
	res = stub.MockInvokeWithSignedProposal("2", [][]byte{[]byte("JoinChain"), badBlockBytes}, sProp)
	assert.Equal(t, res.Status, int32(shim.ERROR))

	// Now, continue with valid execution path
	if res := stub.MockInvokeWithSignedProposal("2", args, sProp); res.Status != shim.OK {
		t.Fatalf("cscc invoke JoinChain failed with: %v", res.Message)
	}

	// This call must fail
	sProp.Signature = nil
	res = stub.MockInvokeWithSignedProposal("3", args, sProp)
	if res.Status == shim.OK {
		t.Fatalf("cscc invoke JoinChain must fail : %v", res.Message)
	}
	assert.Contains(t, res.Message, "\"JoinChain\" request failed authorization check for channel")
	sProp.Signature = sProp.ProposalBytes

	// Query the configuration block
	//chainID := []byte{143, 222, 22, 192, 73, 145, 76, 110, 167, 154, 118, 66, 132, 204, 113, 168}
	chainID, err := utils.GetChainIDFromBlockBytes(blockBytes)
	if err != nil {
		t.Fatalf("cscc invoke JoinChain failed with: %v", err)
	}

	// Test an ACL failure on GetConfigBlock
	mockAclProvider.Reset()
	mockAclProvider.On("CheckACL", resources.CSCC_GetConfigBlock, "mytestchainid", sProp).Return(errors.New("Failed authorization"))
	args = [][]byte{[]byte("GetConfigBlock"), []byte(chainID)}
	res = stub.MockInvokeWithSignedProposal("2", args, sProp)
	if res.Status == shim.OK {
		t.Fatalf("cscc invoke GetConfigBlock shoulda have failed: %v", res.Message)
	}
	assert.Contains(t, res.Message, "Failed authorization")
	mockAclProvider.AssertExpectations(t)

	// Test with ACL okay
	mockAclProvider.Reset()
	mockAclProvider.On("CheckACL", resources.CSCC_GetConfigBlock, "mytestchainid", sProp).Return(nil)
	if res := stub.MockInvokeWithSignedProposal("2", args, sProp); res.Status != shim.OK {
		t.Fatalf("cscc invoke GetConfigBlock failed with: %v", res.Message)
	}

	// get channels for the peer
	args = [][]byte{[]byte(GetChannels)}
	res = stub.MockInvokeWithSignedProposal("2", args, sProp)
	if res.Status != shim.OK {
		t.FailNow()
	}

	cqr := &pb.ChannelQueryResponse{}
	err = proto.Unmarshal(res.Payload, cqr)
	if err != nil {
		t.FailNow()
	}

	// peer joined one channel so query should return an array with one channel
	if len(cqr.GetChannels()) != 1 {
		t.FailNow()
	}
}

func TestPeerConfiger_SubmittingOrdererGenesis(t *testing.T) {

	viper.Set("peer.fileSystemPath", "/tmp/hyperledgertest/")
	os.Mkdir("/tmp/hyperledgertest", 0755)
	defer os.RemoveAll("/tmp/hyperledgertest/")

	e := new(PeerConfiger)
	stub := shim.NewMockStub("PeerConfiger", e)

	if res := stub.MockInit("1", nil); res.Status != shim.OK {
		fmt.Println("Init failed", string(res.Message))
		t.FailNow()
	}
	conf := genesisconfig.Load(genesisconfig.SampleSingleMSPSoloProfile)
	conf.Application = nil
	cg, err := encoder.NewChannelGroup(conf)
	assert.NoError(t, err)
	block, err := genesis.NewFactoryImpl(cg).Block("mytestchainid")
	assert.NoError(t, err)
	blockBytes := utils.MarshalOrPanic(block)

	// Failed path: wrong parameter type
	args := [][]byte{[]byte("JoinChain"), []byte(blockBytes)}
	if res := stub.MockInvoke("2", args); res.Status == shim.OK {
		t.Fatalf("cscc invoke JoinChain should have failed with wrong genesis block.  args: %v", args)
	} else {
		assert.Contains(t, res.Message, "missing Application configuration group")
	}

}

func mockConfigBlock() []byte {
	var blockBytes []byte = nil
	block, err := configtxtest.MakeGenesisBlock("mytestchainid")
	if err == nil {
		blockBytes = utils.MarshalOrPanic(block)
	}
	return blockBytes
}
