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
    vec3 tex_ = texture(tex, vec2(cos(o.position.x * 3.14159), sin(o.position.y * 3.14159))).xyz;
    color = vec4((o.color * albedo + tex_ * int(circle)), 1);
}
