from enum import IntEnum


class Target(IntEnum):
    pass


class BufferTarget(Target):
    ARRAY_BUFFER = 0x8892
    ELEMENT_ARRAY_BUFFER = 0x8893
    UNIFORM_BUFFER = 0x8A11

    ATOMIC_COUNTER_BUFFER = 0x92C0
    COPY_READ_BUFFER = 0x8F36
    COPY_WRITE_BUFFER = 0x8F37
    DISPATCH_INDIRECT_BUFFER = 0x90EE
    DRAW_INDIRECT_BUFFER = 0x8F3F
    PIXEL_PACK_BUFFER = 0x88EB
    PIXEL_UNPACK_BUFFER = 0x88EC
    SHADER_STORAGE_BUFFER = 0x90D2
    TEXTURE_BUFFER = 0x8C2A
    TRANSFORM_FEEDBACK_BUFFER = 0x8C8E


class FrameBufferTarget(Target):
    FRAMEBUFFER = 0x8D40
    READ_FRAMEBUFFER = 0x8CA8
    DRAW_FRAMEBUFFER = 0x8CA9


class TextureTarget(Target):
    TEXTURE_1D = 0x0DE0
    TEXTURE_2D = 0x0DE1
    TEXTURE_3D = 0x806F
    TEXTURE_1D_ARRAY = 0x8C18
    TEXTURE_2D_ARRAY = 0x8C1A
    TEXTURE_RECTANGLE = 0x84F5
    TEXTURE_BUFFER = 0x8C2A
    TEXTURE_CUBE_MAP = 0x8513
    TEXTURE_CUBE_MAP_ARRAY = 0x9009
    TEXTURE_2D_MULTISAMPLE = 0x9100
    TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102

    TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
    TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
    TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
    TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
    TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
    TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A

    PROXY_TEXTURE_1D = 0x8063
    PROXY_TEXTURE_2D = 0x8064
    PROXY_TEXTURE_3D = 0x8070
    PROXY_TEXTURE_1D_ARRAY = 0x8C19
    PROXY_TEXTURE_2D_ARRAY = 0x8C1B
    PROXY_TEXTURE_RECTANGLE = 0x84F7
    PROXY_TEXTURE_CUBE_MAP = 0x851B


class BufferBit(IntEnum):
    DEPTH = 0x00000100
    STENCIL = 0x00000400
    COLOR = 0x00004000


class BufferUsage(IntEnum):
    STREAM_DRAW = 0x88E0
    STREAM_READ = 0x88E1
    STREAM_COPY = 0x88E2
    STATIC_DRAW = 0x88E4
    STATIC_READ = 0x88E5
    STATIC_COPY = 0x88E6
    DYNAMIC_DRAW = 0x88E8
    DYNAMIC_READ = 0x88E9
    DYNAMIC_COPY = 0x88EA


class Interface(IntEnum):
    UNIFORM = 0x92E1
    UNIFORM_BLOCK = 0x92E2
    ATOMIC_COUNTER_BUFFER = 0x92C0
    PROGRAM_INPUT = 0x92E3
    PROGRAM_OUTPUT = 0x92E4
    VERTEX_SUBROUTINE = 0x92E8
    FRAGMENT_SUBROUTINE = 0x92EC
    GEOMETRY_SUBROUTINE = 0x92EB
    TESS_CONTROL_SUBROUTINE = 0x92E9
    TESS_EVALUATION_SUBROUTINE = 0x92EA
    COMPUTE_SUBROUTINE = 0x92ED
    VERTEX_SUBROUTINE_UNIFORM = 0x92EE
    FRAGMENT_SUBROUTINE_UNIFORM = 0x92F2
    GEOMETRY_SUBROUTINE_UNIFORM = 0x92F1
    TESS_CONTROL_SUBROUTINE_UNIFORM = 0x92EF
    TESS_EVALUATION_SUBROUTINE_UNIFORM = 0x92F0
    COMPUTE_SUBROUTINE_UNIFORM = 0x92F3
    TRANSFORM_FEEDBACK_VARYING = 0x92F4
    BUFFER_VARIABLE = 0x92E5
    SHADER_STORAGE_BLOCK = 0x92E6


class InterfaceParameter(IntEnum):
    ACTIVE_RESOURCES = 0x92F5
    MAX_NAME_LENGTH = 0x92F6
    MAX_NUM_ACTIVE_VARIABLES = 0x92F7
    MAX_NUM_COMPATIBLE_SUBROUTINES = 0x92F8


class Primitive(IntEnum):
    POINTS = 0x0000
    LINES = 0x0001
    LINE_LOOP = 0x0002
    LINE_STRIP = 0x0003
    TRIANGLES = 0x0004
    TRIANGLE_STRIP = 0x0005


class DebugSource(IntEnum):
    API = 0x8246
    WINDOW_SYSTEM = 0x8247
    SHADER_COMPILER = 0x8248
    THIRD_PARTY = 0x8249
    APPLICATION = 0x824A
    OTHER = 0x824B
    

class DebugType(IntEnum):
    ERROR = 0x824C
    DEPRECATED_BEHAVIOR = 0x824D
    UNDEFINED_BEHAVIOR = 0x824E
    PORTABILITY = 0x824F
    PERFORMANCE = 0x8250
    MARKER = 0x8268
    PUSH_GROUP = 0x8269
    POP_GROUP = 0x826A
    OTHER = 0x8251


class DebugSeverity(IntEnum):
    HIGH = 0x9146
    MEDIUM = 0x9147
    LOW = 0x9148
    NOTIFICATION = 0x826B
    

class Error(IntEnum):
    NO_ERROR = 0
    INVALID_ENUM = 0x0500
    INVALID_VALUE = 0x0501
    INVALID_INDEX = 0xFFFFFFFF
    INVALID_OPERATION = 0x0502
    OUT_OF_MEMORY = 0x0505
    STACK_OVERFLOW = 0x0503
    STACK_UNDERFLOW = 0x0504


class FrameBufferAttachment(IntEnum):
    DEPTH = 0x8D00
    STENCIL = 0x8D20
    DEPTH_STENCIL = 0x821A

    COLOR_0 = 0x8CE0
    COLOR_1 = 0x8CE1
    COLOR_2 = 0x8CE2
    COLOR_3 = 0x8CE3
    COLOR_4 = 0x8CE4
    COLOR_5 = 0x8CE5
    COLOR_6 = 0x8CE6
    COLOR_7 = 0x8CE7
    COLOR_8 = 0x8CE8
    COLOR_9 = 0x8CE9
    COLOR_10 = 0x8CEA
    COLOR_11 = 0x8CEB
    COLOR_12 = 0x8CEC
    COLOR_13 = 0x8CED
    COLOR_14 = 0x8CEE
    COLOR_15 = 0x8CEF
    COLOR_16 = 0x8CF0
    COLOR_17 = 0x8CF1
    COLOR_18 = 0x8CF2
    COLOR_19 = 0x8CF3
    COLOR_20 = 0x8CF4
    COLOR_21 = 0x8CF5
    COLOR_22 = 0x8CF6
    COLOR_23 = 0x8CF7
    COLOR_24 = 0x8CF8
    COLOR_25 = 0x8CF9
    COLOR_26 = 0x8CFA
    COLOR_27 = 0x8CFB
    COLOR_28 = 0x8CFC
    COLOR_29 = 0x8CFD
    COLOR_30 = 0x8CFE
    COLOR_31 = 0x8CFF


class CullFace(IntEnum):
    FRONT_AND_BACK = 0x0408
    FRONT = 0x0404
    BACK = 0x0405


class DepthFunction(IntEnum):
    NEVER = 0x0200
    LESS = 0x0201
    EQUAL = 0x0202
    LEQUAL = 0x0203
    GREATER = 0x0204
    NOTEQUAL = 0x0205
    GEQUAL = 0x0206
    ALWAYS = 0x0207


class Enableable(IntEnum):
    POLYGON_SMOOTH = 0x0B41
    CULL_FACE = 0x0B44
    DEPTH_TEST = 0x0B71


class PolygonMode(IntEnum):
    POINT = 0x1B00
    LINE = 0x1B01
    FILL = 0x1B02


class ProgramParameter(IntEnum):
    DELETE_STATUS = 0x8B80
    LINK_STATUS = 0x8B82
    VALIDATE_STATUS = 0x8B83
    INFO_LOG_LENGTH = 0x8B84
    ATTACHED_SHADERS = 0x8B85
    ACTIVE_ATTRIBUTES = 0x8B89
    ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
    ACTIVE_UNIFORMS = 0x8B86
    ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
    TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
    TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
    TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x8C76
    ACTIVE_UNIFORM_BLOCKS = 0x8A36
    ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
    GEOMETRY_VERTICES_OUT = 0x8916
    GEOMETRY_INPUT_TYPE = 0x8917
    GEOMETRY_OUTPUT_TYPE = 0x8918
    GEOMETRY_SHADER_INVOCATIONS = 0x887F
    TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
    TESS_GEN_MODE = 0x8E76
    COMPUTE_WORK_GROUP_SIZE = 0x8267
    PROGRAM_SEPARABLE = 0x8258
    PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
    ACTIVE_ATOMIC_COUNTER_BUFFERS = 0x92D9


class ResourceParameter(IntEnum):
    NAME_LENGTH = 0x92F9
    TYPE = 0x92FA
    ARRAY_SIZE = 0x92FB
    OFFSET = 0x92FC
    BLOCK_INDEX = 0x92FD
    ARRAY_STRIDE = 0x92FE
    MATRIX_STRIDE = 0x92FF
    IS_ROW_MAJOR = 0x9300
    ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
    BUFFER_BINDING = 0x9302
    BUFFER_DATA_SIZE = 0x9303
    NUM_ACTIVE_VARIABLES = 0x9304
    ACTIVE_VARIABLES = 0x9305
    REFERENCED_BY_VERTEX_SHADER = 0x9306
    REFERENCED_BY_FRAGMENT_SHADER = 0x930A
    REFERENCED_BY_GEOMETRY_SHADER = 0x9309
    REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
    REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
    REFERENCED_BY_COMPUTE_SHADER = 0x930B
    NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
    COMPATIBLE_SUBROUTINES = 0x8E4B
    TOP_LEVEL_ARRAY_SIZE = 0x930C
    TOP_LEVEL_ARRAY_STRIDE = 0x930D
    LOCATION = 0x930E
    LOCATION_INDEX = 0x930F
    IS_PER_PATCH = 0x92E7


class ShaderParameter(IntEnum):
    SHADER_TYPE = 0x8B4F
    DELETE_STATUS = 0x8B80
    COMPILE_STATUS = 0x8B81
    INFO_LOG_LENGTH = 0x8B84
    SHADER_SOURCE_LENGTH = 0x8B88


class ShaderType(IntEnum):
    VERTEX = 0x8B31
    FRAGMENT = 0x8B30
    GEOMETRY = 0x8DD9
    TESS_CONTROL = 0x8E88
    TESS_EVALUATION = 0x8E87
    COMPUTE = 0x91B9


class TextureParameter(IntEnum):
    DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
    BASE_LEVEL = 0x813C
    MAX_LEVEL = 0x813D
    MIN_LOD = 0x813A
    MAX_LOD = 0x813B
    LOD_BIAS = 0x8501

    COMPARE_MODE = 0x884C
    COMPARE_FUNC = 0x884D

    SWIZZLE_R = 0x8E42
    SWIZZLE_G = 0x8E43
    SWIZZLE_B = 0x8E44
    SWIZZLE_A = 0x8E45

    WRAP_S = 0x2802
    WRAP_T = 0x2803
    WRAP_R = 0x8072

    SWIZZLE_RGBA = 0x8E46
    BORDER_COLOR = 0x1004

    MAG_FILTER = 0x2800
    MIN_FILTER = 0x2801

    TEXTURE_MAX_ANISOTROPY = 0x84FE


class TextureFilter(IntEnum):
    NEAREST = 0x2600
    LINEAR = 0x2601
    NEAREST_MIPMAP_NEAREST = 0x2700
    LINEAR_MIPMAP_NEAREST = 0x2701
    NEAREST_MIPMAP_LINEAR = 0x2702
    LINEAR_MIPMAP_LINEAR = 0x2703


class TextureWrap(IntEnum):
    REPEAT = 0x2901
    MIRRORED_REPEAT = 0x8370
    CLAMP_TO_EDGE = 0x812F
    CLAMP_TO_BORDER = 0x812D


class TextureSwizzle(IntEnum):
    RED = 0x1903
    GREEN = 0x1904
    BLUE = 0x1905
    ALPHA = 0x1906


class TextureUnit(IntEnum):
    TEXTURE0 = 0x84C0
    TEXTURE1 = 0x84C1
    TEXTURE2 = 0x84C2
    TEXTURE3 = 0x84C3
    TEXTURE4 = 0x84C4
    TEXTURE5 = 0x84C5
    TEXTURE6 = 0x84C6
    TEXTURE7 = 0x84C7
    TEXTURE8 = 0x84C8
    TEXTURE9 = 0x84C9
    TEXTURE10 = 0x84CA
    TEXTURE11 = 0x84CB
    TEXTURE12 = 0x84CC
    TEXTURE13 = 0x84CD
    TEXTURE14 = 0x84CE
    TEXTURE15 = 0x84CF
    TEXTURE16 = 0x84D0
    TEXTURE17 = 0x84D1
    TEXTURE18 = 0x84D2
    TEXTURE19 = 0x84D3
    TEXTURE20 = 0x84D4
    TEXTURE21 = 0x84D5
    TEXTURE22 = 0x84D6
    TEXTURE23 = 0x84D7
    TEXTURE24 = 0x84D8
    TEXTURE25 = 0x84D9
    TEXTURE26 = 0x84DA
    TEXTURE27 = 0x84DB
    TEXTURE28 = 0x84DC
    TEXTURE29 = 0x84DD
    TEXTURE30 = 0x84DE
    TEXTURE31 = 0x84DF


class TextureType(IntEnum):
    BYTE = 0x1400
    UNSIGNED_BYTE = 0x1401
    SHORT = 0x1402
    UNSIGNED_SHORT = 0x1403
    INT = 0x1404
    UNSIGNED_INT = 0x1405
    FLOAT = 0x1406
    HALF_FLOAT = 0x140B

    UNSIGNED_BYTE_3_3_2 = 0x8032
    UNSIGNED_BYTE_2_3_3_REV = 0x8362
    UNSIGNED_SHORT_5_6_5 = 0x8363
    UNSIGNED_SHORT_5_6_5_REV = 0x8364
    UNSIGNED_SHORT_4_4_4_4 = 0x8033
    UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
    UNSIGNED_SHORT_5_5_5_1 = 0x8034
    UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
    UNSIGNED_INT_8_8_8_8 = 0x8035
    UNSIGNED_INT_8_8_8_8_REV = 0x8367
    UNSIGNED_INT_10_10_10_2 = 0x8036
    UNSIGNED_INT_2_10_10_10_REV = 0x8368
    UNSIGNED_INT_24_8 = 0x84FA
    UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
    UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
    FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD


class TextureFormat(IntEnum):
    STENCIL_INDEX = 0x1901
    DEPTH_COMPONENT = 0x1902
    DEPTH_STENCIL = 0x84F9

    RED = 0x1903
    GREEN = 0x1904
    BLUE = 0x1905
    RG = 0x8227
    RGB = 0x1907
    RGBA = 0x1908
    BGR = 0x80E0
    BGRA = 0x80E1

    RED_INTEGER = 0x8D94
    GREEN_INTEGER = 0x8D95
    BLUE_INTEGER = 0x8D96
    RG_INTEGER = 0x8228
    RGB_INTEGER = 0x8D98
    RGBA_INTEGER = 0x8D99
    BGR_INTEGER = 0x8D9A
    BGRA_INTEGER = 0x8D9B


class TextureInternalFormat(IntEnum):
    DEPTH_COMPONENT = 0x1902
    DEPTH_STENCIL = 0x84F9
    RED = 0x1903
    RG = 0x8227
    RGB = 0x1907
    RGBA = 0x1908

    DEPTH_COMPONENT16 = 0x81A5
    DEPTH_COMPONENT24 = 0x81A6
    DEPTH_COMPONENT32 = 0x81A7
    DEPTH_COMPONENT32F = 0x8CAC
    DEPTH24_STENCIL8 = 0x88F0
    DEPTH32F_STENCIL8 = 0x8CAD

    R8 = 0x8229
    R8_SNORM = 0x8F94
    R16 = 0x822A
    R16_SNORM = 0x8F98
    RG8 = 0x822B
    RG8_SNORM = 0x8F95
    RG16 = 0x822C
    RG16_SNORM = 0x8F99
    R3_G3_B2 = 0x2A10
    RGB4 = 0x804F
    RGB5 = 0x8050
    RGB565 = 0x8D62
    RGB8 = 0x8051
    RGB8_SNORM = 0x8F96
    RGB10 = 0x8052
    RGB12 = 0x8053
    RGB16 = 0x8054
    RGB16_SNORM = 0x8F9A
    RGBA2 = 0x8055
    RGBA4 = 0x8056
    RGB5_A1 = 0x8057
    RGBA8 = 0x8058
    RGBA8_SNORM = 0x8F97
    RGB10_A2 = 0x8059
    RGB10_A2UI = 0x906F
    RGBA12 = 0x805A
    RGBA16 = 0x805B
    RGBA16_SNORM = 0x8F9B
    SRGB_ALPHA = 0x8C42
    SRGB8_ALPHA8 = 0x8C43
    R16F = 0x822D
    RG16F = 0x822F
    RGB16F = 0x881B
    RGBA16F = 0x881A
    R32F = 0x822E
    RG32F = 0x8230
    RGB32F = 0x8815
    RGBA32F = 0x8814
    R11F_G11F_B10F = 0x8C3A
    RGB9_E5 = 0x8C3D
    R8I = 0x8231
    R8UI = 0x8232
    R16I = 0x8233
    R16UI = 0x8234
    R32I = 0x8235
    R32UI = 0x8236
    RG8I = 0x8237
    RG8UI = 0x8238
    RG16I = 0x8239
    RG16UI = 0x823A
    RG32I = 0x823B
    RG32UI = 0x823C
    RGB8I = 0x8D8F
    RGB8UI = 0x8D7D
    RGB16I = 0x8D89
    RGB16UI = 0x8D77
    RGB32I = 0x8D83
    RGB32UI = 0x8D71
    RGBA8I = 0x8D8E
    RGBA8UI = 0x8D7C
    RGBA16I = 0x8D88
    RGBA16UI = 0x8D76
    RGBA32I = 0x8D82
    RGBA32UI = 0x8D70

    COMPRESSED_RED = 0x8225
    COMPRESSED_RG = 0x8226
    COMPRESSED_RGB = 0x84ED
    COMPRESSED_RGBA = 0x84EE
    COMPRESSED_SRGB = 0x8C48
    COMPRESSED_SRGB_ALPHA = 0x8C49
    COMPRESSED_RED_RGTC1 = 0x8DBB
    COMPRESSED_SIGNED_RED_RGTC1 = 0x8DBC
    COMPRESSED_RG_RGTC2 = 0x8DBD
    COMPRESSED_SIGNED_RG_RGTC2 = 0x8DBE
    COMPRESSED_RGBA_BPTC_UNORM = 0x8E8C
    COMPRESSED_RGB_BPTC_SIGNED_FLOAT = 0x8E8E
    COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT = 0x8E8F
    COMPRESSED_RGB8_ETC2 = 0x9274
    COMPRESSED_SRGB8_ETC2 = 0x9275
    COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
    COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
    COMPRESSED_RGBA8_ETC2_EAC = 0x9278
    COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279
    COMPRESSED_R11_EAC = 0x9270
    COMPRESSED_SIGNED_R11_EAC = 0x9271
    COMPRESSED_RG11_EAC = 0x9272
    COMPRESSED_SIGNED_RG11_EAC = 0x9273


class Type(IntEnum):
    BOOL = 0x8B56
    BYTE = 0x1400
    UNSIGNED_BYTE = 0x1401
    SHORT = 0x1402
    UNSIGNED_SHORT = 0x1403
    INT = 0x1404
    UNSIGNED_INT = 0x1405
    FLOAT = 0x1406
    DOUBLE = 0x140A
    HALF_FLOAT = 0x140B

    BOOL_VEC2 = 0x8B57
    BOOL_VEC3 = 0x8B58
    BOOL_VEC4 = 0x8B59
    INT_VEC2 = 0x8B53
    INT_VEC3 = 0x8B54
    INT_VEC4 = 0x8B55
    UNSIGNED_INT_VEC2 = 0x8DC6
    UNSIGNED_INT_VEC3 = 0x8DC7
    UNSIGNED_INT_VEC4 = 0x8DC8
    FLOAT_VEC2 = 0x8B50
    FLOAT_VEC3 = 0x8B51
    FLOAT_VEC4 = 0x8B52
    DOUBLE_VEC2 = 0x8FFC
    DOUBLE_VEC3 = 0x8FFD
    DOUBLE_VEC4 = 0x8FFE

    FLOAT_MAT2 = 0x8B5A
    FLOAT_MAT3 = 0x8B5B
    FLOAT_MAT4 = 0x8B5C
    FLOAT_MAT2x3 = 0x8B65
    FLOAT_MAT2x4 = 0x8B66
    FLOAT_MAT3x2 = 0x8B67
    FLOAT_MAT3x4 = 0x8B68
    FLOAT_MAT4x2 = 0x8B69
    FLOAT_MAT4x3 = 0x8B6A

    DOUBLE_MAT2 = 0x8F46
    DOUBLE_MAT3 = 0x8F47
    DOUBLE_MAT4 = 0x8F48
    DOUBLE_MAT2x3 = 0x8F49
    DOUBLE_MAT2x4 = 0x8F4A
    DOUBLE_MAT3x2 = 0x8F4B
    DOUBLE_MAT3x4 = 0x8F4C
    DOUBLE_MAT4x2 = 0x8F4D
    DOUBLE_MAT4x3 = 0x8F4E

    SAMPLER_1D = 0x8B5D
    SAMPLER_2D = 0x8B5E
    SAMPLER_3D = 0x8B5F
    SAMPLER_CUBE = 0x8B60
    SAMPLER_1D_SHADOW = 0x8B61
    SAMPLER_2D_SHADOW = 0x8B62
    SAMPLER_1D_ARRAY = 0x8DC0
    SAMPLER_2D_ARRAY = 0x8DC1
    SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
    SAMPLER_2D_ARRAY_SHADOW = 0x8D
    SAMPLER_CUBE_MAP_ARRAY = 0x900C
    SAMPLER_2D_MULTISAMPLE = 0x9108
    SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
    SAMPLER_CUBE_SHADOW = 0x8DC5
    SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
    SAMPLER_BUFFER = 0x8DC2
    SAMPLER_2D_RECT = 0x8B63
    SAMPLER_2D_RECT_SHADOW = 0x8B64

    INT_SAMPLER_1D = 0x8DC9
    INT_SAMPLER_2D = 0x8DCA
    INT_SAMPLER_3D = 0x8DCB
    INT_SAMPLER_CUBE = 0x8DCC
    INT_SAMPLER_1D_ARRAY = 0x8DCE
    INT_SAMPLER_2D_ARRAY = 0x8DCF
    INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
    INT_SAMPLER_2D_MULTISAMPLE = 0x9109
    INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
    INT_SAMPLER_BUFFER = 0x8DD0
    INT_SAMPLER_2D_RECT = 0x8DCD

    UNSIGNED_INT_SAMPLER_1D = 0x8DD1
    UNSIGNED_INT_SAMPLER_2D = 0x8DD2
    UNSIGNED_INT_SAMPLER_3D = 0x8DD3
    UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
    UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
    UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
    UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
    UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
    UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
    UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
    UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5

    IMAGE_1D = 0x904C
    IMAGE_2D = 0x904D
    IMAGE_3D = 0x904E
    IMAGE_2D_RECT = 0x904F
    IMAGE_CUBE = 0x9050
    IMAGE_BUFFER = 0x9051
    IMAGE_1D_ARRAY = 0x9052
    IMAGE_2D_ARRAY = 0x9053
    IMAGE_CUBE_MAP_ARRAY = 0x9054
    IMAGE_2D_MULTISAMPLE = 0x9055
    IMAGE_2D_MULTISAMPLE_ARRAY = 0x9056

    INT_IMAGE_1D = 0x9057
    INT_IMAGE_2D = 0x9058
    INT_IMAGE_3D = 0x9059
    INT_IMAGE_2D_RECT = 0x905A
    INT_IMAGE_CUBE = 0x905B
    INT_IMAGE_BUFFER = 0x905C
    INT_IMAGE_1D_ARRAY = 0x905D
    INT_IMAGE_2D_ARRAY = 0x905E
    INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
    INT_IMAGE_2D_MULTISAMPLE = 0x9060
    INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9061

    UNSIGNED_INT_IMAGE_1D = 0x9062
    UNSIGNED_INT_IMAGE_2D = 0x9063
    UNSIGNED_INT_IMAGE_3D = 0x9064
    UNSIGNED_INT_IMAGE_2D_RECT = 0x9065
    UNSIGNED_INT_IMAGE_CUBE = 0x9066
    UNSIGNED_INT_IMAGE_BUFFER = 0x9067
    UNSIGNED_INT_IMAGE_1D_ARRAY = 0x9068
    UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
    UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
    UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 0x906B
    UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x906C

    UNSIGNED_INT_ATOMIC_COUNTER = 0x92DB



class MatrixType(IntEnum):
    FLOAT_MAT2 = 0x8B5A
    FLOAT_MAT3 = 0x8B5B
    FLOAT_MAT4 = 0x8B5C
    FLOAT_MAT2x3 = 0x8B65
    FLOAT_MAT2x4 = 0x8B66
    FLOAT_MAT3x2 = 0x8B67
    FLOAT_MAT3x4 = 0x8B68
    FLOAT_MAT4x2 = 0x8B69
    FLOAT_MAT4x3 = 0x8B6A

    DOUBLE_MAT2 = 0x8F46
    DOUBLE_MAT3 = 0x8F47
    DOUBLE_MAT4 = 0x8F48
    DOUBLE_MAT2x3 = 0x8F49
    DOUBLE_MAT2x4 = 0x8F4A
    DOUBLE_MAT3x2 = 0x8F4B
    DOUBLE_MAT3x4 = 0x8F4C
    DOUBLE_MAT4x2 = 0x8F4D
    DOUBLE_MAT4x3 = 0x8F4E


class OpaqueType(IntEnum):
    SAMPLER_1D = 0x8B5D
    SAMPLER_2D = 0x8B5E
    SAMPLER_3D = 0x8B5F
    SAMPLER_CUBE = 0x8B60
    SAMPLER_1D_SHADOW = 0x8B61
    SAMPLER_2D_SHADOW = 0x8B62
    SAMPLER_1D_ARRAY = 0x8DC0
    SAMPLER_2D_ARRAY = 0x8DC1
    SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
    SAMPLER_2D_ARRAY_SHADOW = 0x8D
    SAMPLER_CUBE_MAP_ARRAY = 0x900C
    SAMPLER_2D_MULTISAMPLE = 0x9108
    SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
    SAMPLER_CUBE_SHADOW = 0x8DC5
    SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
    SAMPLER_BUFFER = 0x8DC2
    SAMPLER_2D_RECT = 0x8B63
    SAMPLER_2D_RECT_SHADOW = 0x8B64

    INT_SAMPLER_1D = 0x8DC9
    INT_SAMPLER_2D = 0x8DCA
    INT_SAMPLER_3D = 0x8DCB
    INT_SAMPLER_CUBE = 0x8DCC
    INT_SAMPLER_1D_ARRAY = 0x8DCE
    INT_SAMPLER_2D_ARRAY = 0x8DCF
    INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
    INT_SAMPLER_2D_MULTISAMPLE = 0x9109
    INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
    INT_SAMPLER_BUFFER = 0x8DD0
    INT_SAMPLER_2D_RECT = 0x8DCD

    UNSIGNED_INT_SAMPLER_1D = 0x8DD1
    UNSIGNED_INT_SAMPLER_2D = 0x8DD2
    UNSIGNED_INT_SAMPLER_3D = 0x8DD3
    UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
    UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
    UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
    UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
    UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
    UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
    UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
    UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5

    IMAGE_1D = 0x904C
    IMAGE_2D = 0x904D
    IMAGE_3D = 0x904E
    IMAGE_2D_RECT = 0x904F
    IMAGE_CUBE = 0x9050
    IMAGE_BUFFER = 0x9051
    IMAGE_1D_ARRAY = 0x9052
    IMAGE_2D_ARRAY = 0x9053
    IMAGE_CUBE_MAP_ARRAY = 0x9054
    IMAGE_2D_MULTISAMPLE = 0x9055
    IMAGE_2D_MULTISAMPLE_ARRAY = 0x9056

    INT_IMAGE_1D = 0x9057
    INT_IMAGE_2D = 0x9058
    INT_IMAGE_3D = 0x9059
    INT_IMAGE_2D_RECT = 0x905A
    INT_IMAGE_CUBE = 0x905B
    INT_IMAGE_BUFFER = 0x905C
    INT_IMAGE_1D_ARRAY = 0x905D
    INT_IMAGE_2D_ARRAY = 0x905E
    INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
    INT_IMAGE_2D_MULTISAMPLE = 0x9060
    INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9061

    UNSIGNED_INT_IMAGE_1D = 0x9062
    UNSIGNED_INT_IMAGE_2D = 0x9063
    UNSIGNED_INT_IMAGE_3D = 0x9064
    UNSIGNED_INT_IMAGE_2D_RECT = 0x9065
    UNSIGNED_INT_IMAGE_CUBE = 0x9066
    UNSIGNED_INT_IMAGE_BUFFER = 0x9067
    UNSIGNED_INT_IMAGE_1D_ARRAY = 0x9068
    UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
    UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
    UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 0x906B
