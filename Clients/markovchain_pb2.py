# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: markovchain.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='markovchain.proto',
  package='markovchain',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x11markovchain.proto\x12\x0bmarkovchain\"t\n\x05\x43hain\x12*\n\x04link\x18\x01 \x03(\x0b\x32\x1c.markovchain.Chain.LinkEntry\x1a?\n\tLinkEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.markovchain.Value:\x02\x38\x01\"r\n\x05Value\x12%\n\x04word\x18\x02 \x03(\x0b\x32\x17.markovchain.Value.Word\x1a\x42\n\x04Word\x12\x11\n\twordvalue\x18\x01 \x02(\t\x12\x12\n\nselections\x18\x02 \x01(\x05\x12\x13\n\x0bscreen_name\x18\x03 \x02(\t')
)




_CHAIN_LINKENTRY = _descriptor.Descriptor(
  name='LinkEntry',
  full_name='markovchain.Chain.LinkEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='markovchain.Chain.LinkEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='markovchain.Chain.LinkEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=150,
)

_CHAIN = _descriptor.Descriptor(
  name='Chain',
  full_name='markovchain.Chain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link', full_name='markovchain.Chain.link', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CHAIN_LINKENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=150,
)


_VALUE_WORD = _descriptor.Descriptor(
  name='Word',
  full_name='markovchain.Value.Word',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wordvalue', full_name='markovchain.Value.Word.wordvalue', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='selections', full_name='markovchain.Value.Word.selections', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='screen_name', full_name='markovchain.Value.Word.screen_name', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=200,
  serialized_end=266,
)

_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='markovchain.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='word', full_name='markovchain.Value.word', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_VALUE_WORD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=266,
)

_CHAIN_LINKENTRY.fields_by_name['value'].message_type = _VALUE
_CHAIN_LINKENTRY.containing_type = _CHAIN
_CHAIN.fields_by_name['link'].message_type = _CHAIN_LINKENTRY
_VALUE_WORD.containing_type = _VALUE
_VALUE.fields_by_name['word'].message_type = _VALUE_WORD
DESCRIPTOR.message_types_by_name['Chain'] = _CHAIN
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Chain = _reflection.GeneratedProtocolMessageType('Chain', (_message.Message,), dict(

  LinkEntry = _reflection.GeneratedProtocolMessageType('LinkEntry', (_message.Message,), dict(
    DESCRIPTOR = _CHAIN_LINKENTRY,
    __module__ = 'markovchain_pb2'
    # @@protoc_insertion_point(class_scope:markovchain.Chain.LinkEntry)
    ))
  ,
  DESCRIPTOR = _CHAIN,
  __module__ = 'markovchain_pb2'
  # @@protoc_insertion_point(class_scope:markovchain.Chain)
  ))
_sym_db.RegisterMessage(Chain)
_sym_db.RegisterMessage(Chain.LinkEntry)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(

  Word = _reflection.GeneratedProtocolMessageType('Word', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_WORD,
    __module__ = 'markovchain_pb2'
    # @@protoc_insertion_point(class_scope:markovchain.Value.Word)
    ))
  ,
  DESCRIPTOR = _VALUE,
  __module__ = 'markovchain_pb2'
  # @@protoc_insertion_point(class_scope:markovchain.Value)
  ))
_sym_db.RegisterMessage(Value)
_sym_db.RegisterMessage(Value.Word)


_CHAIN_LINKENTRY._options = None
# @@protoc_insertion_point(module_scope)
