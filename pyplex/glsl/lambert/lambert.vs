#version 430 core

uniform Camera {
    mat4 projection;
    mat4 view;
};

uniform mat4 model;
uniform mat3 model_1T;

layout (location = 0) in vec3 position;
layout (location = 2) in vec3 normal;

out Vertex {
    vec3 position;
    vec3 normal;
} v;

void main() {
    gl_Position = projection * view * model * vec4(position, 1);
    v.position = position;
    v.normal = normalize(model_1T * normal);
}
