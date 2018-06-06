#version 430 core

uniform mat4 MVP;
uniform mat3 M1T;

in vec3 position;
in vec3 normal;

out Vertex {
    vec3 position;
    vec3 normal;
} v;

void main() {
    gl_Position = MVP * vec4(position, 1);
    v.position = position;
    v.normal = normalize(M1T * normal);
}
