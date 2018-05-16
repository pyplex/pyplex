#version 430 core

uniform vec3 light_pos;
uniform vec3 view_pos;

uniform vec3 albedo;

uniform sampler2D shadow_map;

uniform float sample_width = 0.0015;
uniform float[9] gaussian = {1, 8, 28, 56, 70, 56, 38, 8, 1};

in Vertex {
    vec3 position;
    vec3 normal;
    vec4 position_light_space;
} v;

out vec4 color;

float sample_shadow(vec4 position_light_space, float bias) {
    vec3 coord = (position_light_space.xyz / position_light_space.w) * 0.5 + 0.5;
    float closest_depth = texture(shadow_map, coord.xy).r;
    float current_depth = coord.z;
    float shadow = current_depth - bias > closest_depth ? 1.0 : 0.0;
    return shadow;
}

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

    float shadow = 0;
    float total = 0;

    float bias = max(0.001 * (1.0 - dot(v.normal, light_dir)), 0.002);

    for (int i=-4; i<=4; i++) {
        for (int j=-4; j<=4; j++) {
            vec2 offset = vec2(sample_width * i, sample_width * j);
            float weight = gaussian[i+4] * gaussian[j+4];
            shadow += weight * sample_shadow(v.position_light_space + vec4(offset, 0, 0), bias);
            total += weight;
        }
    }
    shadow /= total;

    color = vec4((0.1 + (1 - shadow) * (diffuse + specular)) * albedo, 1);
}
