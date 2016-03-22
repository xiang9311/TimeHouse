# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pilot.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


# import common_pb2 as common__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pilot.proto',
  package='com.xiang.proto.pilot',
  syntax='proto3',
  serialized_pb=b'\n\x0bpilot.proto\x12\x15\x63om.xiang.proto.pilot\x1a\x0c\x63ommon.proto\"\x96\x01\n\x0cRequest11001\x12.\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1e.com.xiang.proto.RequestCommon\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.com.xiang.proto.pilot.Request11001.Params\x1a\x1a\n\x06Params\x12\x10\n\x08userName\x18\x01 \x01(\t\"\x81\x01\n\rResponse11001\x12/\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1f.com.xiang.proto.ResponseCommon\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).com.xiang.proto.pilot.Response11001.Data\x1a\x06\n\x04\x44\x61ta\"\xd1\x01\n\x0cRequest11002\x12.\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1e.com.xiang.proto.RequestCommon\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.com.xiang.proto.pilot.Request11002.Params\x1aU\n\x06Params\x12\x13\n\x0bphoneNumber\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\x12\r\n\x05pwMd5\x18\x03 \x01(\t\x12\x15\n\ruserAvatarKey\x18\x04 \x01(\t\"\x81\x01\n\rResponse11002\x12/\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1f.com.xiang.proto.ResponseCommon\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).com.xiang.proto.pilot.Response11002.Data\x1a\x06\n\x04\x44\x61ta\"\xa5\x01\n\x0cRequest11003\x12.\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1e.com.xiang.proto.RequestCommon\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.com.xiang.proto.pilot.Request11003.Params\x1a)\n\x06Params\x12\x10\n\x08username\x18\x01 \x01(\t\x12\r\n\x05pwMd5\x18\x02 \x01(\t\"\x8e\x01\n\rResponse11003\x12/\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1f.com.xiang.proto.ResponseCommon\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).com.xiang.proto.pilot.Response11003.Data\x1a\x13\n\x04\x44\x61ta\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x84\x01\n\x0cRequest11004\x12.\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1e.com.xiang.proto.RequestCommon\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.com.xiang.proto.pilot.Request11004.Params\x1a\x08\n\x06Params\"\xad\x01\n\rResponse11004\x12/\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1f.com.xiang.proto.ResponseCommon\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).com.xiang.proto.pilot.Response11004.Data\x1a\x32\n\x04\x44\x61ta\x12*\n\x08\x61rticles\x18\x01 \x03(\x0b\x32\x18.com.xiang.proto.Article\"\xa9\x01\n\x0cRequest11005\x12.\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1e.com.xiang.proto.RequestCommon\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.com.xiang.proto.pilot.Request11005.Params\x1a-\n\x06Params\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x11\n\tavatarKey\x18\x02 \x01(\t\"\x81\x01\n\rResponse11005\x12/\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1f.com.xiang.proto.ResponseCommon\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).com.xiang.proto.pilot.Response11005.Data\x1a\x06\n\x04\x44\x61ta\"\xa9\x01\n\x0cRequest11006\x12.\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1e.com.xiang.proto.RequestCommon\x12:\n\x06params\x18\x02 \x01(\x0b\x32*.com.xiang.proto.pilot.Request11006.Params\x1a-\n\x06Params\x12\x14\n\x0cneedArticles\x18\x01 \x01(\x08\x12\r\n\x05orgId\x18\x02 \x01(\x05\"\xb2\x01\n\rResponse11006\x12/\n\x06\x63ommon\x18\x01 \x01(\x0b\x32\x1f.com.xiang.proto.ResponseCommon\x12\x37\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32).com.xiang.proto.pilot.Response11006.Data\x1a\x37\n\x04\x44\x61ta\x12/\n\ndetailUser\x18\x01 \x01(\x0b\x32\x1b.com.xiang.proto.DetailUserb\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUEST11001_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='com.xiang.proto.pilot.Request11001.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='com.xiang.proto.pilot.Request11001.Params.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=177,
  serialized_end=203,
)

_REQUEST11001 = _descriptor.Descriptor(
  name='Request11001',
  full_name='com.xiang.proto.pilot.Request11001',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Request11001.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.xiang.proto.pilot.Request11001.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST11001_PARAMS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=203,
)


_RESPONSE11001_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.xiang.proto.pilot.Response11001.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=329,
  serialized_end=335,
)

_RESPONSE11001 = _descriptor.Descriptor(
  name='Response11001',
  full_name='com.xiang.proto.pilot.Response11001',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Response11001.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.xiang.proto.pilot.Response11001.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE11001_DATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=206,
  serialized_end=335,
)


_REQUEST11002_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='com.xiang.proto.pilot.Request11002.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phoneNumber', full_name='com.xiang.proto.pilot.Request11002.Params.phoneNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userName', full_name='com.xiang.proto.pilot.Request11002.Params.userName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pwMd5', full_name='com.xiang.proto.pilot.Request11002.Params.pwMd5', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='userAvatarKey', full_name='com.xiang.proto.pilot.Request11002.Params.userAvatarKey', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=462,
  serialized_end=547,
)

_REQUEST11002 = _descriptor.Descriptor(
  name='Request11002',
  full_name='com.xiang.proto.pilot.Request11002',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Request11002.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.xiang.proto.pilot.Request11002.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST11002_PARAMS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=338,
  serialized_end=547,
)


_RESPONSE11002_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.xiang.proto.pilot.Response11002.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=329,
  serialized_end=335,
)

_RESPONSE11002 = _descriptor.Descriptor(
  name='Response11002',
  full_name='com.xiang.proto.pilot.Response11002',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Response11002.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.xiang.proto.pilot.Response11002.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE11002_DATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=550,
  serialized_end=679,
)


_REQUEST11003_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='com.xiang.proto.pilot.Request11003.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='com.xiang.proto.pilot.Request11003.Params.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pwMd5', full_name='com.xiang.proto.pilot.Request11003.Params.pwMd5', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=806,
  serialized_end=847,
)

_REQUEST11003 = _descriptor.Descriptor(
  name='Request11003',
  full_name='com.xiang.proto.pilot.Request11003',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Request11003.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.xiang.proto.pilot.Request11003.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST11003_PARAMS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=682,
  serialized_end=847,
)


_RESPONSE11003_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.xiang.proto.pilot.Response11003.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='com.xiang.proto.pilot.Response11003.Data.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=973,
  serialized_end=992,
)

_RESPONSE11003 = _descriptor.Descriptor(
  name='Response11003',
  full_name='com.xiang.proto.pilot.Response11003',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Response11003.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.xiang.proto.pilot.Response11003.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE11003_DATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=850,
  serialized_end=992,
)


_REQUEST11004_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='com.xiang.proto.pilot.Request11004.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=177,
  serialized_end=185,
)

_REQUEST11004 = _descriptor.Descriptor(
  name='Request11004',
  full_name='com.xiang.proto.pilot.Request11004',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Request11004.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.xiang.proto.pilot.Request11004.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST11004_PARAMS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=995,
  serialized_end=1127,
)


_RESPONSE11004_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.xiang.proto.pilot.Response11004.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='articles', full_name='com.xiang.proto.pilot.Response11004.Data.articles', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1253,
  serialized_end=1303,
)

_RESPONSE11004 = _descriptor.Descriptor(
  name='Response11004',
  full_name='com.xiang.proto.pilot.Response11004',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Response11004.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.xiang.proto.pilot.Response11004.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE11004_DATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1130,
  serialized_end=1303,
)


_REQUEST11005_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='com.xiang.proto.pilot.Request11005.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='com.xiang.proto.pilot.Request11005.Params.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatarKey', full_name='com.xiang.proto.pilot.Request11005.Params.avatarKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1430,
  serialized_end=1475,
)

_REQUEST11005 = _descriptor.Descriptor(
  name='Request11005',
  full_name='com.xiang.proto.pilot.Request11005',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Request11005.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.xiang.proto.pilot.Request11005.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST11005_PARAMS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1306,
  serialized_end=1475,
)


_RESPONSE11005_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.xiang.proto.pilot.Response11005.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=329,
  serialized_end=335,
)

_RESPONSE11005 = _descriptor.Descriptor(
  name='Response11005',
  full_name='com.xiang.proto.pilot.Response11005',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Response11005.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.xiang.proto.pilot.Response11005.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE11005_DATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1478,
  serialized_end=1607,
)


_REQUEST11006_PARAMS = _descriptor.Descriptor(
  name='Params',
  full_name='com.xiang.proto.pilot.Request11006.Params',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='needArticles', full_name='com.xiang.proto.pilot.Request11006.Params.needArticles', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orgId', full_name='com.xiang.proto.pilot.Request11006.Params.orgId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1734,
  serialized_end=1779,
)

_REQUEST11006 = _descriptor.Descriptor(
  name='Request11006',
  full_name='com.xiang.proto.pilot.Request11006',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Request11006.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='params', full_name='com.xiang.proto.pilot.Request11006.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST11006_PARAMS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1610,
  serialized_end=1779,
)


_RESPONSE11006_DATA = _descriptor.Descriptor(
  name='Data',
  full_name='com.xiang.proto.pilot.Response11006.Data',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='detailUser', full_name='com.xiang.proto.pilot.Response11006.Data.detailUser', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=1905,
  serialized_end=1960,
)

_RESPONSE11006 = _descriptor.Descriptor(
  name='Response11006',
  full_name='com.xiang.proto.pilot.Response11006',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='com.xiang.proto.pilot.Response11006.common', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='com.xiang.proto.pilot.Response11006.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE11006_DATA, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1782,
  serialized_end=1960,
)

_REQUEST11001_PARAMS.containing_type = _REQUEST11001
_REQUEST11001.fields_by_name['common'].message_type = common__pb2._REQUESTCOMMON
_REQUEST11001.fields_by_name['params'].message_type = _REQUEST11001_PARAMS
_RESPONSE11001_DATA.containing_type = _RESPONSE11001
_RESPONSE11001.fields_by_name['common'].message_type = common__pb2._RESPONSECOMMON
_RESPONSE11001.fields_by_name['data'].message_type = _RESPONSE11001_DATA
_REQUEST11002_PARAMS.containing_type = _REQUEST11002
_REQUEST11002.fields_by_name['common'].message_type = common__pb2._REQUESTCOMMON
_REQUEST11002.fields_by_name['params'].message_type = _REQUEST11002_PARAMS
_RESPONSE11002_DATA.containing_type = _RESPONSE11002
_RESPONSE11002.fields_by_name['common'].message_type = common__pb2._RESPONSECOMMON
_RESPONSE11002.fields_by_name['data'].message_type = _RESPONSE11002_DATA
_REQUEST11003_PARAMS.containing_type = _REQUEST11003
_REQUEST11003.fields_by_name['common'].message_type = common__pb2._REQUESTCOMMON
_REQUEST11003.fields_by_name['params'].message_type = _REQUEST11003_PARAMS
_RESPONSE11003_DATA.containing_type = _RESPONSE11003
_RESPONSE11003.fields_by_name['common'].message_type = common__pb2._RESPONSECOMMON
_RESPONSE11003.fields_by_name['data'].message_type = _RESPONSE11003_DATA
_REQUEST11004_PARAMS.containing_type = _REQUEST11004
_REQUEST11004.fields_by_name['common'].message_type = common__pb2._REQUESTCOMMON
_REQUEST11004.fields_by_name['params'].message_type = _REQUEST11004_PARAMS
_RESPONSE11004_DATA.fields_by_name['articles'].message_type = common__pb2._ARTICLE
_RESPONSE11004_DATA.containing_type = _RESPONSE11004
_RESPONSE11004.fields_by_name['common'].message_type = common__pb2._RESPONSECOMMON
_RESPONSE11004.fields_by_name['data'].message_type = _RESPONSE11004_DATA
_REQUEST11005_PARAMS.containing_type = _REQUEST11005
_REQUEST11005.fields_by_name['common'].message_type = common__pb2._REQUESTCOMMON
_REQUEST11005.fields_by_name['params'].message_type = _REQUEST11005_PARAMS
_RESPONSE11005_DATA.containing_type = _RESPONSE11005
_RESPONSE11005.fields_by_name['common'].message_type = common__pb2._RESPONSECOMMON
_RESPONSE11005.fields_by_name['data'].message_type = _RESPONSE11005_DATA
_REQUEST11006_PARAMS.containing_type = _REQUEST11006
_REQUEST11006.fields_by_name['common'].message_type = common__pb2._REQUESTCOMMON
_REQUEST11006.fields_by_name['params'].message_type = _REQUEST11006_PARAMS
_RESPONSE11006_DATA.fields_by_name['detailUser'].message_type = common__pb2._DETAILUSER
_RESPONSE11006_DATA.containing_type = _RESPONSE11006
_RESPONSE11006.fields_by_name['common'].message_type = common__pb2._RESPONSECOMMON
_RESPONSE11006.fields_by_name['data'].message_type = _RESPONSE11006_DATA
DESCRIPTOR.message_types_by_name['Request11001'] = _REQUEST11001
DESCRIPTOR.message_types_by_name['Response11001'] = _RESPONSE11001
DESCRIPTOR.message_types_by_name['Request11002'] = _REQUEST11002
DESCRIPTOR.message_types_by_name['Response11002'] = _RESPONSE11002
DESCRIPTOR.message_types_by_name['Request11003'] = _REQUEST11003
DESCRIPTOR.message_types_by_name['Response11003'] = _RESPONSE11003
DESCRIPTOR.message_types_by_name['Request11004'] = _REQUEST11004
DESCRIPTOR.message_types_by_name['Response11004'] = _RESPONSE11004
DESCRIPTOR.message_types_by_name['Request11005'] = _REQUEST11005
DESCRIPTOR.message_types_by_name['Response11005'] = _RESPONSE11005
DESCRIPTOR.message_types_by_name['Request11006'] = _REQUEST11006
DESCRIPTOR.message_types_by_name['Response11006'] = _RESPONSE11006

Request11001 = _reflection.GeneratedProtocolMessageType('Request11001', (_message.Message,), dict(

  Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST11001_PARAMS,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11001.Params)
    ))
  ,
  DESCRIPTOR = _REQUEST11001,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11001)
  ))
_sym_db.RegisterMessage(Request11001)
_sym_db.RegisterMessage(Request11001.Params)

Response11001 = _reflection.GeneratedProtocolMessageType('Response11001', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE11001_DATA,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11001.Data)
    ))
  ,
  DESCRIPTOR = _RESPONSE11001,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11001)
  ))
_sym_db.RegisterMessage(Response11001)
_sym_db.RegisterMessage(Response11001.Data)

Request11002 = _reflection.GeneratedProtocolMessageType('Request11002', (_message.Message,), dict(

  Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST11002_PARAMS,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11002.Params)
    ))
  ,
  DESCRIPTOR = _REQUEST11002,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11002)
  ))
_sym_db.RegisterMessage(Request11002)
_sym_db.RegisterMessage(Request11002.Params)

Response11002 = _reflection.GeneratedProtocolMessageType('Response11002', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE11002_DATA,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11002.Data)
    ))
  ,
  DESCRIPTOR = _RESPONSE11002,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11002)
  ))
_sym_db.RegisterMessage(Response11002)
_sym_db.RegisterMessage(Response11002.Data)

Request11003 = _reflection.GeneratedProtocolMessageType('Request11003', (_message.Message,), dict(

  Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST11003_PARAMS,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11003.Params)
    ))
  ,
  DESCRIPTOR = _REQUEST11003,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11003)
  ))
_sym_db.RegisterMessage(Request11003)
_sym_db.RegisterMessage(Request11003.Params)

Response11003 = _reflection.GeneratedProtocolMessageType('Response11003', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE11003_DATA,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11003.Data)
    ))
  ,
  DESCRIPTOR = _RESPONSE11003,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11003)
  ))
_sym_db.RegisterMessage(Response11003)
_sym_db.RegisterMessage(Response11003.Data)

Request11004 = _reflection.GeneratedProtocolMessageType('Request11004', (_message.Message,), dict(

  Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST11004_PARAMS,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11004.Params)
    ))
  ,
  DESCRIPTOR = _REQUEST11004,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11004)
  ))
_sym_db.RegisterMessage(Request11004)
_sym_db.RegisterMessage(Request11004.Params)

Response11004 = _reflection.GeneratedProtocolMessageType('Response11004', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE11004_DATA,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11004.Data)
    ))
  ,
  DESCRIPTOR = _RESPONSE11004,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11004)
  ))
_sym_db.RegisterMessage(Response11004)
_sym_db.RegisterMessage(Response11004.Data)

Request11005 = _reflection.GeneratedProtocolMessageType('Request11005', (_message.Message,), dict(

  Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST11005_PARAMS,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11005.Params)
    ))
  ,
  DESCRIPTOR = _REQUEST11005,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11005)
  ))
_sym_db.RegisterMessage(Request11005)
_sym_db.RegisterMessage(Request11005.Params)

Response11005 = _reflection.GeneratedProtocolMessageType('Response11005', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE11005_DATA,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11005.Data)
    ))
  ,
  DESCRIPTOR = _RESPONSE11005,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11005)
  ))
_sym_db.RegisterMessage(Response11005)
_sym_db.RegisterMessage(Response11005.Data)

Request11006 = _reflection.GeneratedProtocolMessageType('Request11006', (_message.Message,), dict(

  Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST11006_PARAMS,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11006.Params)
    ))
  ,
  DESCRIPTOR = _REQUEST11006,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Request11006)
  ))
_sym_db.RegisterMessage(Request11006)
_sym_db.RegisterMessage(Request11006.Params)

Response11006 = _reflection.GeneratedProtocolMessageType('Response11006', (_message.Message,), dict(

  Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE11006_DATA,
    __module__ = 'pilot_pb2'
    # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11006.Data)
    ))
  ,
  DESCRIPTOR = _RESPONSE11006,
  __module__ = 'pilot_pb2'
  # @@protoc_insertion_point(class_scope:com.xiang.proto.pilot.Response11006)
  ))
_sym_db.RegisterMessage(Response11006)
_sym_db.RegisterMessage(Response11006.Data)


# @@protoc_insertion_point(module_scope)
