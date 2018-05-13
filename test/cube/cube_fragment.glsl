#version 430 core

in Vertex {
    vec3 color;
} o;

out vec4 color;

void main() {
    color = vec4(o.color, 1);
}
