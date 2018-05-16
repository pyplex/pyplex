#version 430 core

uniform mat4 light_space;
uniform mat4 model;

in vec3 position;

out float depth;

void main() {
    gl_Position = light_space * model * vec4(position, 1);
}
