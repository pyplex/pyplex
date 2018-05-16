#version 430 core

uniform mat4 projection;
uniform mat4 modelview;
uniform mat3 model_inv_t;

in vec3 position;
in vec3 normal;

out Vertex {
    vec3 position;
    vec3 normal;
    vec3 color;
} o;

void main() {
    gl_Position = projection * modelview * vec4(position, 1.0f);
    o.position = gl_Position.xyz;
    o.normal = normalize(model_inv_t * normal);
}
