#version 430 core

in Vertex {
    vec3 position;
    vec3 normal;
    vec3 color;
} o;

out vec4 color;

void main() {
    color = vec4(abs(o.normal), 1);
}
