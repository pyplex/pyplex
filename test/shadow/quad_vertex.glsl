#version 430 core

in vec2 position;
in vec2 uv;

out Vertex {
    vec2 uv;
} v;

void main() {
    gl_Position = vec4(position, 0, 1);
    v.uv = uv;
}
