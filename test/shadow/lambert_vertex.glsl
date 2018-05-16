#version 430 core

uniform mat4 MVP;
uniform mat3 M1T;

uniform mat4 light_space;

in vec3 position;
in vec3 normal;

out Vertex {
    vec3 position;
    vec3 normal;
    vec4 position_light_space;
} v;

void main() {
    gl_Position = MVP * vec4(position, 1);
    v.position = position;
    v.normal = normalize(M1T * normal);
    v.position_light_space = light_space * vec4(position, 1);
}
