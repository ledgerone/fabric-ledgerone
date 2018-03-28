/*
 * Copyright Greg Haskins All Rights Reserved
 *
 * SPDX-License-Identifier: Apache-2.0
 *
 * See github.com/ledgerone/fabric-ledgerone/test/chaincodes/AutoVendor/chaincode/main.go for details
 */
package directdep

import (
	"github.com/ledgerone/fabric-ledgerone/test/chaincodes/AutoVendor/indirectdep"
)

func PointlessFunction() {
	// delegate to our indirect dependency
	indirectdep.PointlessFunction()
}
