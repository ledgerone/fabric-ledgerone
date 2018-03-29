# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/events.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from peer import chaincode_event_pb2 as peer_dot_chaincode__event__pb2
from peer import transaction_pb2 as peer_dot_transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='peer/events.proto',
  package='protos',
  syntax='proto3',
  serialized_pb=_b('\n\x11peer/events.proto\x12\x06protos\x1a\x13\x63ommon/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1apeer/chaincode_event.proto\x1a\x16peer/transaction.proto\"8\n\x0c\x43haincodeReg\x12\x14\n\x0c\x63haincode_id\x18\x01 \x01(\t\x12\x12\n\nevent_name\x18\x02 \x01(\t\"\x81\x01\n\x08Interest\x12%\n\nevent_type\x18\x01 \x01(\x0e\x32\x11.protos.EventType\x12\x32\n\x12\x63haincode_reg_info\x18\x02 \x01(\x0b\x32\x14.protos.ChaincodeRegH\x00\x12\x0f\n\x07\x63hainID\x18\x03 \x01(\tB\t\n\x07RegInfo\",\n\x08Register\x12 \n\x06\x65vents\x18\x01 \x03(\x0b\x32\x10.protos.Interest\"?\n\tRejection\x12\x1f\n\x02tx\x18\x01 \x01(\x0b\x32\x13.protos.Transaction\x12\x11\n\terror_msg\x18\x02 \x01(\t\".\n\nUnregister\x12 \n\x06\x65vents\x18\x01 \x03(\x0b\x32\x10.protos.Interest\"o\n\rFilteredBlock\x12\x12\n\nchannel_id\x18\x01 \x01(\t\x12\x0e\n\x06number\x18\x02 \x01(\x04\x12:\n\x15\x66iltered_transactions\x18\x04 \x03(\x0b\x32\x1b.protos.FilteredTransaction\"\xc6\x01\n\x13\x46ilteredTransaction\x12\x0c\n\x04txid\x18\x01 \x01(\t\x12 \n\x04type\x18\x02 \x01(\x0e\x32\x12.common.HeaderType\x12\x34\n\x12tx_validation_code\x18\x03 \x01(\x0e\x32\x18.protos.TxValidationCode\x12\x41\n\x13transaction_actions\x18\x04 \x01(\x0b\x32\".protos.FilteredTransactionActionsH\x00\x42\x06\n\x04\x44\x61ta\"X\n\x1a\x46ilteredTransactionActions\x12:\n\x11\x63haincode_actions\x18\x01 \x03(\x0b\x32\x1f.protos.FilteredChaincodeAction\"J\n\x17\x46ilteredChaincodeAction\x12/\n\x0f\x63haincode_event\x18\x01 \x01(\x0b\x32\x16.protos.ChaincodeEvent\"4\n\x0bSignedEvent\x12\x11\n\tsignature\x18\x01 \x01(\x0c\x12\x12\n\neventBytes\x18\x02 \x01(\x0c\"\xe3\x02\n\x05\x45vent\x12$\n\x08register\x18\x01 \x01(\x0b\x32\x10.protos.RegisterH\x00\x12\x1e\n\x05\x62lock\x18\x02 \x01(\x0b\x32\r.common.BlockH\x00\x12\x31\n\x0f\x63haincode_event\x18\x03 \x01(\x0b\x32\x16.protos.ChaincodeEventH\x00\x12&\n\trejection\x18\x04 \x01(\x0b\x32\x11.protos.RejectionH\x00\x12(\n\nunregister\x18\x05 \x01(\x0b\x32\x12.protos.UnregisterH\x00\x12/\n\x0e\x66iltered_block\x18\x07 \x01(\x0b\x32\x15.protos.FilteredBlockH\x00\x12\x0f\n\x07\x63reator\x18\x06 \x01(\x0c\x12-\n\ttimestamp\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x15\n\rtls_cert_hash\x18\t \x01(\x0c\x42\x07\n\x05\x45vent\"\x8c\x01\n\x0f\x44\x65liverResponse\x12 \n\x06status\x18\x01 \x01(\x0e\x32\x0e.common.StatusH\x00\x12\x1e\n\x05\x62lock\x18\x02 \x01(\x0b\x32\r.common.BlockH\x00\x12/\n\x0e\x66iltered_block\x18\x03 \x01(\x0b\x32\x15.protos.FilteredBlockH\x00\x42\x06\n\x04Type*U\n\tEventType\x12\x0c\n\x08REGISTER\x10\x00\x12\t\n\x05\x42LOCK\x10\x01\x12\r\n\tCHAINCODE\x10\x02\x12\r\n\tREJECTION\x10\x03\x12\x11\n\rFILTEREDBLOCK\x10\x04\x32:\n\x06\x45vents\x12\x30\n\x04\x43hat\x12\x13.protos.SignedEvent\x1a\r.protos.Event\"\x00(\x01\x30\x01\x32\x89\x01\n\x07\x44\x65liver\x12:\n\x07\x44\x65liver\x12\x10.common.Envelope\x1a\x17.protos.DeliverResponse\"\x00(\x01\x30\x01\x12\x42\n\x0f\x44\x65liverFiltered\x12\x10.common.Envelope\x1a\x17.protos.DeliverResponse\"\x00(\x01\x30\x01\x42n\n*org.ledgerone.fabric_ledgerone.protos.peerB\rEventsPackageZ1github.com/ledgerone/fabric-ledgerone/protos/peerb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,peer_dot_chaincode__event__pb2.DESCRIPTOR,peer_dot_transaction__pb2.DESCRIPTOR,])

_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='protos.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REGISTER', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHAINCODE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REJECTION', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FILTEREDBLOCK', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1519,
  serialized_end=1604,
)
_sym_db.RegisterEnumDescriptor(_EVENTTYPE)

EventType = enum_type_wrapper.EnumTypeWrapper(_EVENTTYPE)
REGISTER = 0
BLOCK = 1
CHAINCODE = 2
REJECTION = 3
FILTEREDBLOCK = 4



_CHAINCODEREG = _descriptor.Descriptor(
  name='ChaincodeReg',
  full_name='protos.ChaincodeReg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_id', full_name='protos.ChaincodeReg.chaincode_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='event_name', full_name='protos.ChaincodeReg.event_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=191,
)


_INTEREST = _descriptor.Descriptor(
  name='Interest',
  full_name='protos.Interest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='protos.Interest.event_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chaincode_reg_info', full_name='protos.Interest.chaincode_reg_info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chainID', full_name='protos.Interest.chainID', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='RegInfo', full_name='protos.Interest.RegInfo',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=194,
  serialized_end=323,
)


_REGISTER = _descriptor.Descriptor(
  name='Register',
  full_name='protos.Register',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='protos.Register.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=369,
)


_REJECTION = _descriptor.Descriptor(
  name='Rejection',
  full_name='protos.Rejection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx', full_name='protos.Rejection.tx', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='protos.Rejection.error_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=371,
  serialized_end=434,
)


_UNREGISTER = _descriptor.Descriptor(
  name='Unregister',
  full_name='protos.Unregister',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='protos.Unregister.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=436,
  serialized_end=482,
)


_FILTEREDBLOCK = _descriptor.Descriptor(
  name='FilteredBlock',
  full_name='protos.FilteredBlock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='protos.FilteredBlock.channel_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='protos.FilteredBlock.number', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filtered_transactions', full_name='protos.FilteredBlock.filtered_transactions', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=484,
  serialized_end=595,
)


_FILTEREDTRANSACTION = _descriptor.Descriptor(
  name='FilteredTransaction',
  full_name='protos.FilteredTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txid', full_name='protos.FilteredTransaction.txid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='protos.FilteredTransaction.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_validation_code', full_name='protos.FilteredTransaction.tx_validation_code', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transaction_actions', full_name='protos.FilteredTransaction.transaction_actions', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Data', full_name='protos.FilteredTransaction.Data',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=598,
  serialized_end=796,
)


_FILTEREDTRANSACTIONACTIONS = _descriptor.Descriptor(
  name='FilteredTransactionActions',
  full_name='protos.FilteredTransactionActions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_actions', full_name='protos.FilteredTransactionActions.chaincode_actions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=798,
  serialized_end=886,
)


_FILTEREDCHAINCODEACTION = _descriptor.Descriptor(
  name='FilteredChaincodeAction',
  full_name='protos.FilteredChaincodeAction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chaincode_event', full_name='protos.FilteredChaincodeAction.chaincode_event', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=888,
  serialized_end=962,
)


_SIGNEDEVENT = _descriptor.Descriptor(
  name='SignedEvent',
  full_name='protos.SignedEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='protos.SignedEvent.signature', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='eventBytes', full_name='protos.SignedEvent.eventBytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=964,
  serialized_end=1016,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='protos.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='register', full_name='protos.Event.register', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='protos.Event.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chaincode_event', full_name='protos.Event.chaincode_event', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rejection', full_name='protos.Event.rejection', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unregister', full_name='protos.Event.unregister', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filtered_block', full_name='protos.Event.filtered_block', index=5,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creator', full_name='protos.Event.creator', index=6,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='protos.Event.timestamp', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tls_cert_hash', full_name='protos.Event.tls_cert_hash', index=8,
      number=9, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Event', full_name='protos.Event.Event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1019,
  serialized_end=1374,
)


_DELIVERRESPONSE = _descriptor.Descriptor(
  name='DeliverResponse',
  full_name='protos.DeliverResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='protos.DeliverResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='protos.DeliverResponse.block', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filtered_block', full_name='protos.DeliverResponse.filtered_block', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='protos.DeliverResponse.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1377,
  serialized_end=1517,
)

_INTEREST.fields_by_name['event_type'].enum_type = _EVENTTYPE
_INTEREST.fields_by_name['chaincode_reg_info'].message_type = _CHAINCODEREG
_INTEREST.oneofs_by_name['RegInfo'].fields.append(
  _INTEREST.fields_by_name['chaincode_reg_info'])
_INTEREST.fields_by_name['chaincode_reg_info'].containing_oneof = _INTEREST.oneofs_by_name['RegInfo']
_REGISTER.fields_by_name['events'].message_type = _INTEREST
_REJECTION.fields_by_name['tx'].message_type = peer_dot_transaction__pb2._TRANSACTION
_UNREGISTER.fields_by_name['events'].message_type = _INTEREST
_FILTEREDBLOCK.fields_by_name['filtered_transactions'].message_type = _FILTEREDTRANSACTION
_FILTEREDTRANSACTION.fields_by_name['type'].enum_type = common_dot_common__pb2._HEADERTYPE
_FILTEREDTRANSACTION.fields_by_name['tx_validation_code'].enum_type = peer_dot_transaction__pb2._TXVALIDATIONCODE
_FILTEREDTRANSACTION.fields_by_name['transaction_actions'].message_type = _FILTEREDTRANSACTIONACTIONS
_FILTEREDTRANSACTION.oneofs_by_name['Data'].fields.append(
  _FILTEREDTRANSACTION.fields_by_name['transaction_actions'])
_FILTEREDTRANSACTION.fields_by_name['transaction_actions'].containing_oneof = _FILTEREDTRANSACTION.oneofs_by_name['Data']
_FILTEREDTRANSACTIONACTIONS.fields_by_name['chaincode_actions'].message_type = _FILTEREDCHAINCODEACTION
_FILTEREDCHAINCODEACTION.fields_by_name['chaincode_event'].message_type = peer_dot_chaincode__event__pb2._CHAINCODEEVENT
_EVENT.fields_by_name['register'].message_type = _REGISTER
_EVENT.fields_by_name['block'].message_type = common_dot_common__pb2._BLOCK
_EVENT.fields_by_name['chaincode_event'].message_type = peer_dot_chaincode__event__pb2._CHAINCODEEVENT
_EVENT.fields_by_name['rejection'].message_type = _REJECTION
_EVENT.fields_by_name['unregister'].message_type = _UNREGISTER
_EVENT.fields_by_name['filtered_block'].message_type = _FILTEREDBLOCK
_EVENT.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENT.oneofs_by_name['Event'].fields.append(
  _EVENT.fields_by_name['register'])
_EVENT.fields_by_name['register'].containing_oneof = _EVENT.oneofs_by_name['Event']
_EVENT.oneofs_by_name['Event'].fields.append(
  _EVENT.fields_by_name['block'])
_EVENT.fields_by_name['block'].containing_oneof = _EVENT.oneofs_by_name['Event']
_EVENT.oneofs_by_name['Event'].fields.append(
  _EVENT.fields_by_name['chaincode_event'])
_EVENT.fields_by_name['chaincode_event'].containing_oneof = _EVENT.oneofs_by_name['Event']
_EVENT.oneofs_by_name['Event'].fields.append(
  _EVENT.fields_by_name['rejection'])
_EVENT.fields_by_name['rejection'].containing_oneof = _EVENT.oneofs_by_name['Event']
_EVENT.oneofs_by_name['Event'].fields.append(
  _EVENT.fields_by_name['unregister'])
_EVENT.fields_by_name['unregister'].containing_oneof = _EVENT.oneofs_by_name['Event']
_EVENT.oneofs_by_name['Event'].fields.append(
  _EVENT.fields_by_name['filtered_block'])
_EVENT.fields_by_name['filtered_block'].containing_oneof = _EVENT.oneofs_by_name['Event']
_DELIVERRESPONSE.fields_by_name['status'].enum_type = common_dot_common__pb2._STATUS
_DELIVERRESPONSE.fields_by_name['block'].message_type = common_dot_common__pb2._BLOCK
_DELIVERRESPONSE.fields_by_name['filtered_block'].message_type = _FILTEREDBLOCK
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['status'])
_DELIVERRESPONSE.fields_by_name['status'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['block'])
_DELIVERRESPONSE.fields_by_name['block'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
_DELIVERRESPONSE.oneofs_by_name['Type'].fields.append(
  _DELIVERRESPONSE.fields_by_name['filtered_block'])
_DELIVERRESPONSE.fields_by_name['filtered_block'].containing_oneof = _DELIVERRESPONSE.oneofs_by_name['Type']
DESCRIPTOR.message_types_by_name['ChaincodeReg'] = _CHAINCODEREG
DESCRIPTOR.message_types_by_name['Interest'] = _INTEREST
DESCRIPTOR.message_types_by_name['Register'] = _REGISTER
DESCRIPTOR.message_types_by_name['Rejection'] = _REJECTION
DESCRIPTOR.message_types_by_name['Unregister'] = _UNREGISTER
DESCRIPTOR.message_types_by_name['FilteredBlock'] = _FILTEREDBLOCK
DESCRIPTOR.message_types_by_name['FilteredTransaction'] = _FILTEREDTRANSACTION
DESCRIPTOR.message_types_by_name['FilteredTransactionActions'] = _FILTEREDTRANSACTIONACTIONS
DESCRIPTOR.message_types_by_name['FilteredChaincodeAction'] = _FILTEREDCHAINCODEACTION
DESCRIPTOR.message_types_by_name['SignedEvent'] = _SIGNEDEVENT
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['DeliverResponse'] = _DELIVERRESPONSE
DESCRIPTOR.enum_types_by_name['EventType'] = _EVENTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChaincodeReg = _reflection.GeneratedProtocolMessageType('ChaincodeReg', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCODEREG,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.ChaincodeReg)
  ))
_sym_db.RegisterMessage(ChaincodeReg)

Interest = _reflection.GeneratedProtocolMessageType('Interest', (_message.Message,), dict(
  DESCRIPTOR = _INTEREST,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.Interest)
  ))
_sym_db.RegisterMessage(Interest)

Register = _reflection.GeneratedProtocolMessageType('Register', (_message.Message,), dict(
  DESCRIPTOR = _REGISTER,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.Register)
  ))
_sym_db.RegisterMessage(Register)

Rejection = _reflection.GeneratedProtocolMessageType('Rejection', (_message.Message,), dict(
  DESCRIPTOR = _REJECTION,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.Rejection)
  ))
_sym_db.RegisterMessage(Rejection)

Unregister = _reflection.GeneratedProtocolMessageType('Unregister', (_message.Message,), dict(
  DESCRIPTOR = _UNREGISTER,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.Unregister)
  ))
_sym_db.RegisterMessage(Unregister)

FilteredBlock = _reflection.GeneratedProtocolMessageType('FilteredBlock', (_message.Message,), dict(
  DESCRIPTOR = _FILTEREDBLOCK,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.FilteredBlock)
  ))
_sym_db.RegisterMessage(FilteredBlock)

FilteredTransaction = _reflection.GeneratedProtocolMessageType('FilteredTransaction', (_message.Message,), dict(
  DESCRIPTOR = _FILTEREDTRANSACTION,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.FilteredTransaction)
  ))
_sym_db.RegisterMessage(FilteredTransaction)

FilteredTransactionActions = _reflection.GeneratedProtocolMessageType('FilteredTransactionActions', (_message.Message,), dict(
  DESCRIPTOR = _FILTEREDTRANSACTIONACTIONS,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.FilteredTransactionActions)
  ))
_sym_db.RegisterMessage(FilteredTransactionActions)

FilteredChaincodeAction = _reflection.GeneratedProtocolMessageType('FilteredChaincodeAction', (_message.Message,), dict(
  DESCRIPTOR = _FILTEREDCHAINCODEACTION,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.FilteredChaincodeAction)
  ))
_sym_db.RegisterMessage(FilteredChaincodeAction)

SignedEvent = _reflection.GeneratedProtocolMessageType('SignedEvent', (_message.Message,), dict(
  DESCRIPTOR = _SIGNEDEVENT,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.SignedEvent)
  ))
_sym_db.RegisterMessage(SignedEvent)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.Event)
  ))
_sym_db.RegisterMessage(Event)

DeliverResponse = _reflection.GeneratedProtocolMessageType('DeliverResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELIVERRESPONSE,
  __module__ = 'peer.events_pb2'
  # @@protoc_insertion_point(class_scope:protos.DeliverResponse)
  ))
_sym_db.RegisterMessage(DeliverResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n*org.ledgerone.fabric_ledgerone.protos.peerB\rEventsPackageZ1github.com/ledgerone/fabric-ledgerone/protos/peer'))

_EVENTS = _descriptor.ServiceDescriptor(
  name='Events',
  full_name='protos.Events',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1606,
  serialized_end=1664,
  methods=[
  _descriptor.MethodDescriptor(
    name='Chat',
    full_name='protos.Events.Chat',
    index=0,
    containing_service=None,
    input_type=_SIGNEDEVENT,
    output_type=_EVENT,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTS)

DESCRIPTOR.services_by_name['Events'] = _EVENTS


_DELIVER = _descriptor.ServiceDescriptor(
  name='Deliver',
  full_name='protos.Deliver',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=1667,
  serialized_end=1804,
  methods=[
  _descriptor.MethodDescriptor(
    name='Deliver',
    full_name='protos.Deliver.Deliver',
    index=0,
    containing_service=None,
    input_type=common_dot_common__pb2._ENVELOPE,
    output_type=_DELIVERRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DeliverFiltered',
    full_name='protos.Deliver.DeliverFiltered',
    index=1,
    containing_service=None,
    input_type=common_dot_common__pb2._ENVELOPE,
    output_type=_DELIVERRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DELIVER)

DESCRIPTOR.services_by_name['Deliver'] = _DELIVER

# @@protoc_insertion_point(module_scope)
