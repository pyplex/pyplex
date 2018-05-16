#version 430 core

uniform sampler2D tex;

in Vertex {
    vec2 uv;
} v;

out vec4 color;

void main() {
    float depth =  texture(tex, v.uv).r;
    color = vec4(vec3(depth), 1);
}
