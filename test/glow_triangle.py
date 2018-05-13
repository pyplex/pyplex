from pyplex import *
import numpy as np
import os


class Canvas(canvas.Canvas):
    def on_start(self, ctx: gl.GL_ANY):
        self.ctx = ctx

        self.program = Program(ctx,
            VertexShader(ctx, os.path.abspath('../pyplex/glsl/default_vertex.glsl')),
            FragmentShader(ctx, os.path.abspath('../pyplex/glsl/default_fragment.glsl')))

        self.program['tex'] = Texture2D(self.ctx, np.random.uniform(0,1,(64,64,3)).astype(np.float32), TextureFilter.nearest())
        self.program['albedo'] = np.array([1, 1, 1], np.float32)

        self.buffer = ArrayBuffer(ctx, np.array([
            -3/4, -3/4,     1, 0, 0,
             3/4, -3/4,     0, 1, 0,
             0  ,  3/4,     0, 0, 1],
            np.float32).view([('position', '2f4'), ('color', '3f4')]))
        self.program.vertices(self.buffer)

        self.ctx.clear_color(np.random.random(), np.random.random(), np.random.random(), 1)
        self.set_aspect_ratio(1, 1)

    def on_framebuffer_resize(self, width: int, height: int):
        self.ctx.viewport(0, 0, width, height)

    def on_draw(self):
        self.ctx.clear(gl.BufferBit.COLOR)
        self.program.draw_arrays(gl.DrawMode.TRIANGLES, 0, 3)


if __name__ == "__main__":
    Canvas().run()
