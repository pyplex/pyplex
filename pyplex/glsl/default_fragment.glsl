#version 430 core

uniform vec3 albedo;
uniform sampler2D tex;

in Vertex {
    vec2 position;
    vec3 color;
} o;

out vec4 color;

void main() {
    bool circle = length(o.position) < 0.5;
    vec3 tex_ = texture(tex, o.position * length(o.position)).xyz;
    color = vec4((o.color * albedo + tex_ * int(circle)), 1);
}
