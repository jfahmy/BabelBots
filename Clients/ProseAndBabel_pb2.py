# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProseAndBabel.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ProseAndBabel.proto',
  package='proseandbabel',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13ProseAndBabel.proto\x12\rproseandbabel\"\x1b\n\x0c\x42\x61\x62\x65lRequest\x12\x0b\n\x03\x61sk\x18\x01 \x01(\t\"\x16\n\x05\x42\x61\x62\x65l\x12\r\n\x05prose\x18\x01 \x01(\t\"\x1c\n\nUserTweets\x12\x0e\n\x06tweets\x18\x01 \x01(\t\"\x1a\n\tUserBabel\x12\r\n\x05prose\x18\x01 \x01(\t2\xe7\x02\n\rProseAndBabel\x12?\n\x08GetHaiku\x12\x1b.proseandbabel.BabelRequest\x1a\x14.proseandbabel.Babel\"\x00\x12?\n\x08GetBabel\x12\x1b.proseandbabel.BabelRequest\x1a\x14.proseandbabel.Babel\"\x00\x12K\n\x10UserMarkovStream\x12\x19.proseandbabel.UserTweets\x1a\x18.proseandbabel.UserBabel\"\x00(\x01\x12\x43\n\nUserMarkov\x12\x19.proseandbabel.UserTweets\x1a\x18.proseandbabel.UserBabel\"\x00\x12\x42\n\tUserHaiku\x12\x19.proseandbabel.UserTweets\x1a\x18.proseandbabel.UserBabel\"\x00\x62\x06proto3')
)




_BABELREQUEST = _descriptor.Descriptor(
  name='BabelRequest',
  full_name='proseandbabel.BabelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ask', full_name='proseandbabel.BabelRequest.ask', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=65,
)


_BABEL = _descriptor.Descriptor(
  name='Babel',
  full_name='proseandbabel.Babel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prose', full_name='proseandbabel.Babel.prose', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=89,
)


_USERTWEETS = _descriptor.Descriptor(
  name='UserTweets',
  full_name='proseandbabel.UserTweets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tweets', full_name='proseandbabel.UserTweets.tweets', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=119,
)


_USERBABEL = _descriptor.Descriptor(
  name='UserBabel',
  full_name='proseandbabel.UserBabel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prose', full_name='proseandbabel.UserBabel.prose', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=147,
)

DESCRIPTOR.message_types_by_name['BabelRequest'] = _BABELREQUEST
DESCRIPTOR.message_types_by_name['Babel'] = _BABEL
DESCRIPTOR.message_types_by_name['UserTweets'] = _USERTWEETS
DESCRIPTOR.message_types_by_name['UserBabel'] = _USERBABEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BabelRequest = _reflection.GeneratedProtocolMessageType('BabelRequest', (_message.Message,), dict(
  DESCRIPTOR = _BABELREQUEST,
  __module__ = 'ProseAndBabel_pb2'
  # @@protoc_insertion_point(class_scope:proseandbabel.BabelRequest)
  ))
_sym_db.RegisterMessage(BabelRequest)

Babel = _reflection.GeneratedProtocolMessageType('Babel', (_message.Message,), dict(
  DESCRIPTOR = _BABEL,
  __module__ = 'ProseAndBabel_pb2'
  # @@protoc_insertion_point(class_scope:proseandbabel.Babel)
  ))
_sym_db.RegisterMessage(Babel)

UserTweets = _reflection.GeneratedProtocolMessageType('UserTweets', (_message.Message,), dict(
  DESCRIPTOR = _USERTWEETS,
  __module__ = 'ProseAndBabel_pb2'
  # @@protoc_insertion_point(class_scope:proseandbabel.UserTweets)
  ))
_sym_db.RegisterMessage(UserTweets)

UserBabel = _reflection.GeneratedProtocolMessageType('UserBabel', (_message.Message,), dict(
  DESCRIPTOR = _USERBABEL,
  __module__ = 'ProseAndBabel_pb2'
  # @@protoc_insertion_point(class_scope:proseandbabel.UserBabel)
  ))
_sym_db.RegisterMessage(UserBabel)



_PROSEANDBABEL = _descriptor.ServiceDescriptor(
  name='ProseAndBabel',
  full_name='proseandbabel.ProseAndBabel',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=150,
  serialized_end=509,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetHaiku',
    full_name='proseandbabel.ProseAndBabel.GetHaiku',
    index=0,
    containing_service=None,
    input_type=_BABELREQUEST,
    output_type=_BABEL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetBabel',
    full_name='proseandbabel.ProseAndBabel.GetBabel',
    index=1,
    containing_service=None,
    input_type=_BABELREQUEST,
    output_type=_BABEL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserMarkovStream',
    full_name='proseandbabel.ProseAndBabel.UserMarkovStream',
    index=2,
    containing_service=None,
    input_type=_USERTWEETS,
    output_type=_USERBABEL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserMarkov',
    full_name='proseandbabel.ProseAndBabel.UserMarkov',
    index=3,
    containing_service=None,
    input_type=_USERTWEETS,
    output_type=_USERBABEL,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='UserHaiku',
    full_name='proseandbabel.ProseAndBabel.UserHaiku',
    index=4,
    containing_service=None,
    input_type=_USERTWEETS,
    output_type=_USERBABEL,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROSEANDBABEL)

DESCRIPTOR.services_by_name['ProseAndBabel'] = _PROSEANDBABEL

# @@protoc_insertion_point(module_scope)