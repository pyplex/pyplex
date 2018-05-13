#version 430 core

uniform mat4 MVP;

in vec3 position;
in vec3 color;

out Vertex {
    vec3 color;
} o;

void main() {
    gl_Position = MVP * vec4(position, 1.0f);
    o.color = color;
}
