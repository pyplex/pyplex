#version 430 core

uniform vec3 ambient;
uniform vec3 albedo;

uniform vec3 light_pos;
uniform vec3 view_pos;

in Vertex {
    vec3 position;
    vec3 normal;
} v;

out vec4 color;

float phong(vec3 position, vec3 normal, vec3 light_pos, float strength, float shininess){
    vec3 norm = normalize(normal);
    vec3 light_dir = normalize(light_pos - position);
    vec3 view_dir = normalize(view_pos - position);
    vec3 reflect_dir = reflect(-light_dir, norm);

    float specular = pow(max(dot(view_dir, reflect_dir), 0), shininess) * strength;

    return specular;
}

float lambert(vec3 normal, vec3 light_dir) {
    return max(dot(light_dir, normal), 0);
}

void main() {
    vec3 light_dir = normalize(light_pos - v.position);
    float diffuse = lambert(v.normal, light_dir);
    float specular = phong(v.position, v.normal, light_pos, 0.8, 32);

    color = vec4((ambient + diffuse + specular) * albedo, 1);
}
