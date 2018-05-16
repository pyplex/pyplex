#version 430 core

uniform vec3 view_pos;
uniform vec3 albedo;

struct Light {
    vec3 position;
    vec3 color;
};

uniform int lightCount;
layout(std140) uniform LightBlock {
    Light lights[100];
};

in Vertex {
    vec3 position;
    vec3 normal;
    vec3 color;
} o;

out vec4 color;


float phong(vec3 light_pos, float strength, float shininess){
    vec3 norm = normalize(o.normal);
    vec3 light_dir = normalize(light_pos - o.position);
    vec3 view_dir = normalize(view_pos - o.position);
    vec3 reflect_dir = reflect(light_dir, norm);

    float diffuse = max(dot(norm, light_dir), 0);
    float specular = pow(max(dot(view_dir, reflect_dir), 0), shininess) * strength;

    return diffuse + specular;
}


void main() {
    vec3 c = vec3(0);

    for (int i=0; i<lightCount; i++){
        c += phong(lights[i].position, 0.5, 8) * lights[i].color;
    }

    color = vec4((c / lightCount + 0.1) * albedo, 1);
}
