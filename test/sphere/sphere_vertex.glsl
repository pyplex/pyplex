#version 430 core

uniform mat4 projection;
uniform mat4 modelview;
uniform mat3 modelview_inv_t;

in vec3 position;
in vec3 normal;

out Vertex {
    vec3 normal;
    vec3 color;
} o;

void main() {
    gl_Position = projection * modelview * vec4(position, 1.0f);
    o.normal = normalize(modelview_inv_t * normal);
//    o.color = abs(position) * 1.5 - (gl_Position.zzz / gl_Position.w);
//    o.color = gl_Position.zzz / gl_Position.w;
//    o.color = abs(normal);
}
