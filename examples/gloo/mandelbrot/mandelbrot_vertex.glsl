#version 430

uniform mat4 view;
uniform mat4 projection;

in vec2 position;
out vec2 coordinate;

void main() {
    gl_Position = vec4(position, 0.0, 1.0);
    coordinate = (view * projection * vec4(position, 0.0, 1.0)).xy;
}
