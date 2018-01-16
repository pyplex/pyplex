#version 430

uniform mat4 view;
uniform mat4 projection;

in vec2 position;
out vec2 coordinate;

void main() {
    // Set position of Screen-Space Quad
    gl_Position = vec4(position, 0.0, 1.0);

    // Transform Quad Coordinates to View Coordinates
    coordinate = (view * projection * vec4(position, 0.0, 1.0)).xy;
}
