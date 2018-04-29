#version 430 core

uniform vec3 albedo;
uniform sampler2D tex;

in Vertex {
    vec2 position;
    vec3 color;
} o;

out vec4 color;

void main() {
    color = vec4(o.color * albedo + texture(tex, o.position).xyz, 1);
}
