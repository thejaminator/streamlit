# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: streamlit/proto/ArrowVegaLiteChart.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from streamlit.proto import Arrow_pb2 as streamlit_dot_proto_dot_Arrow__pb2
from streamlit.proto import ArrowNamedDataSet_pb2 as streamlit_dot_proto_dot_ArrowNamedDataSet__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='streamlit/proto/ArrowVegaLiteChart.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(streamlit/proto/ArrowVegaLiteChart.proto\x1a\x1bstreamlit/proto/Arrow.proto\x1a\'streamlit/proto/ArrowNamedDataSet.proto\"\x81\x01\n\x12\x41rrowVegaLiteChart\x12\x0c\n\x04spec\x18\x01 \x01(\t\x12\x14\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x06.Arrow\x12$\n\x08\x64\x61tasets\x18\x04 \x03(\x0b\x32\x12.ArrowNamedDataSet\x12\x1b\n\x13use_container_width\x18\x05 \x01(\x08J\x04\x08\x03\x10\x04\x62\x06proto3'
  ,
  dependencies=[streamlit_dot_proto_dot_Arrow__pb2.DESCRIPTOR,streamlit_dot_proto_dot_ArrowNamedDataSet__pb2.DESCRIPTOR,])




_ARROWVEGALITECHART = _descriptor.Descriptor(
  name='ArrowVegaLiteChart',
  full_name='ArrowVegaLiteChart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='spec', full_name='ArrowVegaLiteChart.spec', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ArrowVegaLiteChart.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='datasets', full_name='ArrowVegaLiteChart.datasets', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_container_width', full_name='ArrowVegaLiteChart.use_container_width', index=3,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=115,
  serialized_end=244,
)

_ARROWVEGALITECHART.fields_by_name['data'].message_type = streamlit_dot_proto_dot_Arrow__pb2._ARROW
_ARROWVEGALITECHART.fields_by_name['datasets'].message_type = streamlit_dot_proto_dot_ArrowNamedDataSet__pb2._ARROWNAMEDDATASET
DESCRIPTOR.message_types_by_name['ArrowVegaLiteChart'] = _ARROWVEGALITECHART
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ArrowVegaLiteChart = _reflection.GeneratedProtocolMessageType('ArrowVegaLiteChart', (_message.Message,), {
  'DESCRIPTOR' : _ARROWVEGALITECHART,
  '__module__' : 'streamlit.proto.ArrowVegaLiteChart_pb2'
  # @@protoc_insertion_point(class_scope:ArrowVegaLiteChart)
  })
_sym_db.RegisterMessage(ArrowVegaLiteChart)


# @@protoc_insertion_point(module_scope)
