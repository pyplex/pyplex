#version 430 core

#define MAX_DIRECTIONAL_LIGHTS 1
#define MAX_POINT_LIGHTS 12

uniform Camera {
    mat4 projection;
    mat4 view;
    vec3 position;
} camera;

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


uniform vec3 ambient;   // Ambient Color

uniform float Ns;       // Specular Exponent
uniform vec3 Ka;        // Ambient Reflectivity
uniform vec3 Kd;        // Diffuse Reflectivity
uniform vec3 Ks;        // Specular Reflectivity
uniform vec3 Ke;        // Emission

in Vertex {
    vec3 position;
    vec3 normal;
} v;

out vec4 color;

float lambert(vec3 N, vec3 L) {
    return max(dot(N, L), 0);
}

float phong(vec3 N, vec3 L, vec3 V) {
    return pow(max(dot(V, reflect(-L, N)), 0), Ns);
}

float blinn_phong(vec3 N, vec3 L, vec3 V) {
    return pow(max(dot(N, normalize(L + V)), 0), Ns);
}

void main() {
    vec3 c = Ke + Ka * ambient;

    vec3 N = normalize(v.normal);
    vec3 V = normalize(camera.position - v.position);

    // Point Lights
    for (int i=0; i<PointLightCount; i++) {
        vec3 L = pointlight[i].position - v.position;
        vec3 Ln = normalize(L);

        c += pointlight[i].color * pointlight[i].strength *             // Color & Strength
             (Kd * lambert(N, Ln) + Ks * blinn_phong(N, Ln, V)) /       // Diffuse and Specular
             (1 + pointlight[i].falloff * pow(length(L), 2));           // Attenuation
    }

    color = vec4(c, 1);
}
