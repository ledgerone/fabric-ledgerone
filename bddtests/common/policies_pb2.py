# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/policies.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from msp import msp_principal_pb2 as msp_dot_msp__principal__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='common/policies.proto',
  package='common',
  syntax='proto3',
  serialized_pb=_b('\n\x15\x63ommon/policies.proto\x12\x06\x63ommon\x1a\x17msp/msp_principal.proto\"k\n\x06Policy\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\x0c\"D\n\nPolicyType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tSIGNATURE\x10\x01\x12\x07\n\x03MSP\x10\x02\x12\x11\n\rIMPLICIT_META\x10\x03\"{\n\x17SignaturePolicyEnvelope\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12%\n\x04rule\x18\x02 \x01(\x0b\x32\x17.common.SignaturePolicy\x12(\n\nidentities\x18\x03 \x03(\x0b\x32\x14.common.MSPPrincipal\"\x9f\x01\n\x0fSignaturePolicy\x12\x13\n\tsigned_by\x18\x01 \x01(\x05H\x00\x12\x32\n\x08n_out_of\x18\x02 \x01(\x0b\x32\x1e.common.SignaturePolicy.NOutOfH\x00\x1a;\n\x06NOutOf\x12\t\n\x01n\x18\x01 \x01(\x05\x12&\n\x05rules\x18\x02 \x03(\x0b\x32\x17.common.SignaturePolicyB\x06\n\x04Type\"\x7f\n\x12ImplicitMetaPolicy\x12\x12\n\nsub_policy\x18\x01 \x01(\t\x12-\n\x04rule\x18\x02 \x01(\x0e\x32\x1f.common.ImplicitMetaPolicy.Rule\"&\n\x04Rule\x12\x07\n\x03\x41NY\x10\x00\x12\x07\n\x03\x41LL\x10\x01\x12\x0c\n\x08MAJORITY\x10\x02\x42\x63\n,org.ledgerone.fabric_ledgerone.protos.commonZ3github.com/ledgerone/fabric-ledgerone/protos/commonb\x06proto3')
  ,
  dependencies=[msp_dot_msp__principal__pb2.DESCRIPTOR,])



_POLICY_POLICYTYPE = _descriptor.EnumDescriptor(
  name='PolicyType',
  full_name='common.Policy.PolicyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SIGNATURE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MSP', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IMPLICIT_META', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=97,
  serialized_end=165,
)
_sym_db.RegisterEnumDescriptor(_POLICY_POLICYTYPE)

_IMPLICITMETAPOLICY_RULE = _descriptor.EnumDescriptor(
  name='Rule',
  full_name='common.ImplicitMetaPolicy.Rule',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAJORITY', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=543,
  serialized_end=581,
)
_sym_db.RegisterEnumDescriptor(_IMPLICITMETAPOLICY_RULE)


_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='common.Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='common.Policy.type', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='common.Policy.value', index=1,
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
    _POLICY_POLICYTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=165,
)


_SIGNATUREPOLICYENVELOPE = _descriptor.Descriptor(
  name='SignaturePolicyEnvelope',
  full_name='common.SignaturePolicyEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='common.SignaturePolicyEnvelope.version', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='common.SignaturePolicyEnvelope.rule', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identities', full_name='common.SignaturePolicyEnvelope.identities', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=167,
  serialized_end=290,
)


_SIGNATUREPOLICY_NOUTOF = _descriptor.Descriptor(
  name='NOutOf',
  full_name='common.SignaturePolicy.NOutOf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n', full_name='common.SignaturePolicy.NOutOf.n', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='common.SignaturePolicy.NOutOf.rules', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=385,
  serialized_end=444,
)

_SIGNATUREPOLICY = _descriptor.Descriptor(
  name='SignaturePolicy',
  full_name='common.SignaturePolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signed_by', full_name='common.SignaturePolicy.signed_by', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n_out_of', full_name='common.SignaturePolicy.n_out_of', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SIGNATUREPOLICY_NOUTOF, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Type', full_name='common.SignaturePolicy.Type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=293,
  serialized_end=452,
)


_IMPLICITMETAPOLICY = _descriptor.Descriptor(
  name='ImplicitMetaPolicy',
  full_name='common.ImplicitMetaPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub_policy', full_name='common.ImplicitMetaPolicy.sub_policy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rule', full_name='common.ImplicitMetaPolicy.rule', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMPLICITMETAPOLICY_RULE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=454,
  serialized_end=581,
)

_POLICY_POLICYTYPE.containing_type = _POLICY
_SIGNATUREPOLICYENVELOPE.fields_by_name['rule'].message_type = _SIGNATUREPOLICY
_SIGNATUREPOLICYENVELOPE.fields_by_name['identities'].message_type = msp_dot_msp__principal__pb2._MSPPRINCIPAL
_SIGNATUREPOLICY_NOUTOF.fields_by_name['rules'].message_type = _SIGNATUREPOLICY
_SIGNATUREPOLICY_NOUTOF.containing_type = _SIGNATUREPOLICY
_SIGNATUREPOLICY.fields_by_name['n_out_of'].message_type = _SIGNATUREPOLICY_NOUTOF
_SIGNATUREPOLICY.oneofs_by_name['Type'].fields.append(
  _SIGNATUREPOLICY.fields_by_name['signed_by'])
_SIGNATUREPOLICY.fields_by_name['signed_by'].containing_oneof = _SIGNATUREPOLICY.oneofs_by_name['Type']
_SIGNATUREPOLICY.oneofs_by_name['Type'].fields.append(
  _SIGNATUREPOLICY.fields_by_name['n_out_of'])
_SIGNATUREPOLICY.fields_by_name['n_out_of'].containing_oneof = _SIGNATUREPOLICY.oneofs_by_name['Type']
_IMPLICITMETAPOLICY.fields_by_name['rule'].enum_type = _IMPLICITMETAPOLICY_RULE
_IMPLICITMETAPOLICY_RULE.containing_type = _IMPLICITMETAPOLICY
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['SignaturePolicyEnvelope'] = _SIGNATUREPOLICYENVELOPE
DESCRIPTOR.message_types_by_name['SignaturePolicy'] = _SIGNATUREPOLICY
DESCRIPTOR.message_types_by_name['ImplicitMetaPolicy'] = _IMPLICITMETAPOLICY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), dict(
  DESCRIPTOR = _POLICY,
  __module__ = 'common.policies_pb2'
  # @@protoc_insertion_point(class_scope:common.Policy)
  ))
_sym_db.RegisterMessage(Policy)

SignaturePolicyEnvelope = _reflection.GeneratedProtocolMessageType('SignaturePolicyEnvelope', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATUREPOLICYENVELOPE,
  __module__ = 'common.policies_pb2'
  # @@protoc_insertion_point(class_scope:common.SignaturePolicyEnvelope)
  ))
_sym_db.RegisterMessage(SignaturePolicyEnvelope)

SignaturePolicy = _reflection.GeneratedProtocolMessageType('SignaturePolicy', (_message.Message,), dict(

  NOutOf = _reflection.GeneratedProtocolMessageType('NOutOf', (_message.Message,), dict(
    DESCRIPTOR = _SIGNATUREPOLICY_NOUTOF,
    __module__ = 'common.policies_pb2'
    # @@protoc_insertion_point(class_scope:common.SignaturePolicy.NOutOf)
    ))
  ,
  DESCRIPTOR = _SIGNATUREPOLICY,
  __module__ = 'common.policies_pb2'
  # @@protoc_insertion_point(class_scope:common.SignaturePolicy)
  ))
_sym_db.RegisterMessage(SignaturePolicy)
_sym_db.RegisterMessage(SignaturePolicy.NOutOf)

ImplicitMetaPolicy = _reflection.GeneratedProtocolMessageType('ImplicitMetaPolicy', (_message.Message,), dict(
  DESCRIPTOR = _IMPLICITMETAPOLICY,
  __module__ = 'common.policies_pb2'
  # @@protoc_insertion_point(class_scope:common.ImplicitMetaPolicy)
  ))
_sym_db.RegisterMessage(ImplicitMetaPolicy)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n,org.ledgerone.fabric_ledgerone.protos.commonZ3github.com/ledgerone/fabric-ledgerone/protos/common'))
# @@protoc_insertion_point(module_scope)
