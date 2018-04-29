#version 430 core

in vec2 position;
in vec3 color;

out Vertex {
    vec2 position;
    vec3 color;
} o;

void main() {
    gl_Position = vec4(position, 0, 1);
    o.position = position;
    o.color = color;
}
