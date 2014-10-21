# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: convolutional_neural_network_settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='convolutional_neural_network_settings.proto',
  package='convnn',
  serialized_pb=_b('\n+convolutional_neural_network_settings.proto\x12\x06\x63onvnn\"\xca\x03\n\x0b\x43NNSettings\x12\x15\n\rlearning_rate\x18\x01 \x01(\x02\x12\x10\n\x08n_epochs\x18\x02 \x01(\x05\x12\x0f\n\x07\x64\x61taset\x18\x03 \x02(\t\x12\x12\n\nbatch_size\x18\x04 \x01(\x05\x12\x10\n\x08poolsize\x18\x05 \x01(\x05\x12:\n\nconv_layer\x18\x06 \x03(\x0b\x32&.convnn.CNNSettings.ConvolutionalLayer\x12\x35\n\x0chidden_layer\x18\x07 \x03(\x0b\x32\x1f.convnn.CNNSettings.HiddenLayer\x12\x31\n\nlast_layer\x18\x08 \x02(\x0b\x32\x1d.convnn.CNNSettings.LastLayer\x12\x15\n\rcost_function\x18\t \x02(\t\x1a;\n\x12\x43onvolutionalLayer\x12\x13\n\x0bnum_filters\x18\x01 \x02(\x05\x12\x10\n\x08\x66ilter_w\x18\x02 \x02(\x05\x1a?\n\x0bHiddenLayer\x12\x13\n\x0bnum_outputs\x18\x01 \x02(\x05\x12\x1b\n\x13\x61\x63tivation_function\x18\x02 \x02(\t\x1a \n\tLastLayer\x12\x13\n\x0bnum_outputs\x18\x01 \x02(\x05')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CNNSETTINGS_CONVOLUTIONALLAYER = _descriptor.Descriptor(
  name='ConvolutionalLayer',
  full_name='convnn.CNNSettings.ConvolutionalLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_filters', full_name='convnn.CNNSettings.ConvolutionalLayer.num_filters', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_w', full_name='convnn.CNNSettings.ConvolutionalLayer.filter_w', index=1,
      number=2, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=356,
  serialized_end=415,
)

_CNNSETTINGS_HIDDENLAYER = _descriptor.Descriptor(
  name='HiddenLayer',
  full_name='convnn.CNNSettings.HiddenLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_outputs', full_name='convnn.CNNSettings.HiddenLayer.num_outputs', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activation_function', full_name='convnn.CNNSettings.HiddenLayer.activation_function', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=417,
  serialized_end=480,
)

_CNNSETTINGS_LASTLAYER = _descriptor.Descriptor(
  name='LastLayer',
  full_name='convnn.CNNSettings.LastLayer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_outputs', full_name='convnn.CNNSettings.LastLayer.num_outputs', index=0,
      number=1, type=5, cpp_type=1, label=2,
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
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=482,
  serialized_end=514,
)

_CNNSETTINGS = _descriptor.Descriptor(
  name='CNNSettings',
  full_name='convnn.CNNSettings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='learning_rate', full_name='convnn.CNNSettings.learning_rate', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='n_epochs', full_name='convnn.CNNSettings.n_epochs', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset', full_name='convnn.CNNSettings.dataset', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='convnn.CNNSettings.batch_size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poolsize', full_name='convnn.CNNSettings.poolsize', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='conv_layer', full_name='convnn.CNNSettings.conv_layer', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hidden_layer', full_name='convnn.CNNSettings.hidden_layer', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_layer', full_name='convnn.CNNSettings.last_layer', index=7,
      number=8, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cost_function', full_name='convnn.CNNSettings.cost_function', index=8,
      number=9, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CNNSETTINGS_CONVOLUTIONALLAYER, _CNNSETTINGS_HIDDENLAYER, _CNNSETTINGS_LASTLAYER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=56,
  serialized_end=514,
)

_CNNSETTINGS_CONVOLUTIONALLAYER.containing_type = _CNNSETTINGS
_CNNSETTINGS_HIDDENLAYER.containing_type = _CNNSETTINGS
_CNNSETTINGS_LASTLAYER.containing_type = _CNNSETTINGS
_CNNSETTINGS.fields_by_name['conv_layer'].message_type = _CNNSETTINGS_CONVOLUTIONALLAYER
_CNNSETTINGS.fields_by_name['hidden_layer'].message_type = _CNNSETTINGS_HIDDENLAYER
_CNNSETTINGS.fields_by_name['last_layer'].message_type = _CNNSETTINGS_LASTLAYER
DESCRIPTOR.message_types_by_name['CNNSettings'] = _CNNSETTINGS

CNNSettings = _reflection.GeneratedProtocolMessageType('CNNSettings', (_message.Message,), dict(

  ConvolutionalLayer = _reflection.GeneratedProtocolMessageType('ConvolutionalLayer', (_message.Message,), dict(
    DESCRIPTOR = _CNNSETTINGS_CONVOLUTIONALLAYER,
    __module__ = 'convolutional_neural_network_settings_pb2'
    # @@protoc_insertion_point(class_scope:convnn.CNNSettings.ConvolutionalLayer)
    ))
  ,

  HiddenLayer = _reflection.GeneratedProtocolMessageType('HiddenLayer', (_message.Message,), dict(
    DESCRIPTOR = _CNNSETTINGS_HIDDENLAYER,
    __module__ = 'convolutional_neural_network_settings_pb2'
    # @@protoc_insertion_point(class_scope:convnn.CNNSettings.HiddenLayer)
    ))
  ,

  LastLayer = _reflection.GeneratedProtocolMessageType('LastLayer', (_message.Message,), dict(
    DESCRIPTOR = _CNNSETTINGS_LASTLAYER,
    __module__ = 'convolutional_neural_network_settings_pb2'
    # @@protoc_insertion_point(class_scope:convnn.CNNSettings.LastLayer)
    ))
  ,
  DESCRIPTOR = _CNNSETTINGS,
  __module__ = 'convolutional_neural_network_settings_pb2'
  # @@protoc_insertion_point(class_scope:convnn.CNNSettings)
  ))
_sym_db.RegisterMessage(CNNSettings)
_sym_db.RegisterMessage(CNNSettings.ConvolutionalLayer)
_sym_db.RegisterMessage(CNNSettings.HiddenLayer)
_sym_db.RegisterMessage(CNNSettings.LastLayer)


# @@protoc_insertion_point(module_scope)
