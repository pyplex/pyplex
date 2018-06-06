#version 430 core

#define MAX_DIRECTIONAL_LIGHTS 4
#define MAX_POINT_LIGHTS 4

uniform int DirectionalLightCount;
layout(std140) uniform DirectionalLight {
    vec3 direction;
    float strength;
    vec3 color;
    float _;
} dirlight[MAX_DIRECTIONAL_LIGHTS];

uniform int PointLightCount;
layout(std140) uniform PointLight {
    vec3 position;
    float strength;
    vec3 color;
    float falloff;
} pointlight[MAX_POINT_LIGHTS];

uniform vec3 ambient;
uniform vec3 albedo;

in Vertex {
    vec3 position;
    vec3 normal;
} v;

out vec4 color;

float lambert(vec3 normal, vec3 light_dir) {
    return max(dot(light_dir, normal), 0);
}

void main() {
    vec3 diffuse = vec3(0);

    // Directional Lights
    for (int i=0; i<DirectionalLightCount; i++){
        diffuse += lambert(v.normal, dirlight[i].direction) * dirlight[i].color * dirlight[i].strength;
    }

    // Point Lights
    for (int i=0; i<PointLightCount; i++) {
        vec3 direction = pointlight[i].position - v.position;
        diffuse += lambert(v.normal, normalize(direction)) * pointlight[i].color *
                   pointlight[i].strength / (1.0 + pointlight[i].falloff * pow(length(direction), 2));
    }

    color = vec4((ambient + diffuse) * albedo, 1);
}
