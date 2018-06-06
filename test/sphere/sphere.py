import pyplex as px
import numpy as np
from time import time
import os


class SphereTest(px.Canvas):
    def on_start(self, ctx: px.gl.GL43):
        self.ctx = ctx

        self.program = px.Program(self.ctx,
            px.VertexShader(self.ctx, os.path.join(os.path.dirname(__file__), 'sphere_vertex.glsl')),
            px.FragmentShader(self.ctx, os.path.join(os.path.dirname(__file__), 'sphere_fragment.glsl')))

        sphere = px.Sphere(64, 32)

        self.vertices = sphere.vertices
        self.program['position'] = px.ArrayBuffer(ctx, self.vertices)
        self.program['normal'] = px.ArrayBuffer(ctx, self.vertices)
        self.elements = px.ElementArrayBuffer(ctx, sphere.elements)

        self.program['albedo'] = np.random.uniform(size=3).astype(np.float32)


        # self.ctx.enable(px.gl.Enableable.CULL_FACE)
        # self.ctx.cull_face(px.gl.CullFace.BACK)
        self.ctx.enable(px.gl.Enableable.DEPTH_TEST)
        self.ctx.clear_color(0.1, 0.2, 0.4, 1)

        self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)

    def on_framebuffer_resize(self, width: int, height: int):
        self.program['projection'] = px.transform.perspective(60, width / height, 1, 10)
        self.ctx.viewport(0, 0, width, height)

    def on_update(self, dt: float):
        view = px.transform.translation([0, 0, -5])
        model = px.transform.rotation([0, time()/np.pi, 0])
        modelview = model * view

        modelview_inv_t = np.ascontiguousarray(np.linalg.inv(modelview).T[:3, :3])

        self.program['light'] = np.array([-1, 0, 1], np.float32)

        self.program['modelview'] = modelview
        self.program['modelview_inv_t'] = modelview_inv_t

    def on_draw(self):
        self.ctx.clear(px.gl.BufferBit.COLOR | px.gl.BufferBit.DEPTH)
        self.program.draw_elements(px.gl.Primitive.TRIANGLES, self.elements)


if __name__ == "__main__":
    SphereTest(px.CanvasConfig(samples=16)).run()