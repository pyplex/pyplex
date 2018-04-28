from pyplex.gl import Type


BASE_TYPE = {
    Type.BYTE: Type.BYTE,
    Type.UNSIGNED_BYTE: Type.UNSIGNED_BYTE,
    Type.SHORT: Type.SHORT,
    Type.UNSIGNED_SHORT: Type.UNSIGNED_SHORT,

    Type.BOOL: Type.BOOL,
    Type.BOOL_VEC2: Type.BOOL,
    Type.BOOL_VEC3: Type.BOOL,
    Type.BOOL_VEC4: Type.BOOL,

    Type.INT: Type.INT,
    Type.INT_VEC2: Type.INT,
    Type.INT_VEC3: Type.INT,
    Type.INT_VEC4: Type.INT,

    Type.UNSIGNED_INT: Type.UNSIGNED_INT,
    Type.UNSIGNED_INT_VEC2: Type.UNSIGNED_INT,
    Type.UNSIGNED_INT_VEC3: Type.UNSIGNED_INT,
    Type.UNSIGNED_INT_VEC4: Type.UNSIGNED_INT,

    Type.FLOAT: Type.FLOAT,
    Type.FLOAT_VEC2: Type.FLOAT,
    Type.FLOAT_VEC3: Type.FLOAT,
    Type.FLOAT_VEC4: Type.FLOAT,

    Type.DOUBLE: Type.DOUBLE,
    Type.DOUBLE_VEC2: Type.DOUBLE,
    Type.DOUBLE_VEC3: Type.DOUBLE,
    Type.DOUBLE_VEC4: Type.DOUBLE,

    Type.FLOAT_MAT2: Type.FLOAT,
    Type.FLOAT_MAT3: Type.FLOAT,
    Type.FLOAT_MAT4: Type.FLOAT,
    Type.FLOAT_MAT2x3: Type.FLOAT,
    Type.FLOAT_MAT2x4: Type.FLOAT,
    Type.FLOAT_MAT3x2: Type.FLOAT,
    Type.FLOAT_MAT3x4: Type.FLOAT,
    Type.FLOAT_MAT4x2: Type.FLOAT,
    Type.FLOAT_MAT4x3: Type.FLOAT,

    Type.DOUBLE_MAT2: Type.DOUBLE,
    Type.DOUBLE_MAT3: Type.DOUBLE,
    Type.DOUBLE_MAT4: Type.DOUBLE,
    Type.DOUBLE_MAT2x3: Type.DOUBLE,
    Type.DOUBLE_MAT2x4: Type.DOUBLE,
    Type.DOUBLE_MAT3x2: Type.DOUBLE,
    Type.DOUBLE_MAT3x4: Type.DOUBLE,
    Type.DOUBLE_MAT4x2: Type.DOUBLE,
    Type.DOUBLE_MAT4x3: Type.DOUBLE,
}