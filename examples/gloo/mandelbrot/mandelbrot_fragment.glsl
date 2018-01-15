#version 430

uniform int iterations;
uniform vec3 colormap[8];
uniform float time;

in vec2 coordinate;
out vec4 color;

int mandelbrot(float creal, float cimag){
    float real = creal;
    float imag = cimag;

    float real2, imag2;

    for (int i=0; i<iterations; i++){
        real2 = real * real;
        imag2 = imag * imag;

        if (real2 + imag2 > 4.0) return i;

        imag = 2 * real * imag + cimag;
        real = real2 - imag2 + creal;
    }

    return 0;
}

void main() {
    float offset = sqrt(mandelbrot(coordinate.x, coordinate.y) / float(iterations))*(colormap.length() - 1) + time;
    int index = int(offset);
    float factor = offset - index;

    vec3 c = (1-factor) * colormap[index % colormap.length()] + factor * colormap[(index+1) % colormap.length()];
    color = vec4(c, 1.0);
}