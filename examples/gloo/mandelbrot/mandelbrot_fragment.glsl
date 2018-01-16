#version 430

uniform int iterations;
uniform vec3 colormap[10];

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
    // Calculate Mandelbrot for Fragment
    int mandelbrot_result = mandelbrot(coordinate.x, coordinate.y);

    // Color according to colormap
    float colormap_offset = sqrt(mandelbrot_result / float(iterations))*(colormap.length() - 1);
    int colormap_index = int(colormap_offset); float colormap_factor = colormap_offset - colormap_index;
    color = vec4((1-colormap_factor) * colormap[colormap_index] + colormap_factor * colormap[colormap_index+1], 1.0);
}