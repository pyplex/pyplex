#version 430 core

uniform vec3 light;

uniform vec3 albedo;

in Vertex {
    vec3 normal;
    vec3 color;
} o;

out vec4 color;

float lambert(vec3 normal, vec3 light){
    return max(dot(normal, normalize(light)), 0);
}

void main() {
    vec3 diffuse = lambert(o.normal, light) * albedo;
    color = vec4(diffuse, 1);
}
