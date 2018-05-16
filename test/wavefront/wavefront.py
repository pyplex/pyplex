import pyplex as px
import numpy as np
import math
from time import time
import os


class WavefrontTest(px.Canvas):
    def on_start(self, ctx: px.gl.GL43):
        self.ctx = ctx

        self.program = px.Program(self.ctx,
            px.VertexShader(self.ctx, 'phong_vertex.glsl'),
            px.FragmentShader(self.ctx, 'phong_fragment.glsl'))

        geometry = px.loader.wavefront(os.path.abspath('../../obj/suzanne.obj'))
        # geometry = px.Sphere(128, 64)
        # geometry = px.Cube()
        geometry.recalculate_normals()

        self.program['position'] = px.ArrayBuffer(self.ctx, geometry.vertices)
        self.program['normal'] = px.ArrayBuffer(self.ctx, geometry.normals)
        self.elements = px.ElementArrayBuffer(self.ctx, geometry.elements)

        self.program['albedo'] = np.random.uniform(size=3).astype(np.float32)

        self._light_count = 50
        self._rotation = np.random.uniform(0.001, 0.002, (self._light_count, 3)).astype(np.float32)
        self._lights = np.recarray(self._light_count, [('position', '3f4'), ('color', '3f4')])

        self._lights['position'] = np.random.uniform(-1, 1, (self._light_count, 3)).astype(np.float32)
        self._lights['position'] *= 10 / np.linalg.norm(self._lights['position'], 2, -1, True)

        self._lights['color'] = np.random.uniform(0, 1, (self._light_count, 3)).astype(np.float32)
        self._lights['color'] /= np.linalg.norm(self._lights['color'], 2, -1, True)

        self._light_buffer = px.UniformBuffer(self.ctx, self._lights, px.gl.BufferUsage.STREAM_DRAW)
        self.program['LightBlock'] = self._light_buffer
        self.program['lightCount'] = np.array(self._light_count, np.int)

        self._view_pos = np.array([0, 0, -3], np.float32)
        self._view = px.transform.translation(self._view_pos)

        self.program['view_pos'] = self._view_pos

        self.ctx.enable(px.gl.Enableable.CULL_FACE)
        self.ctx.cull_face(px.gl.CullFace.BACK)
        self.ctx.enable(px.gl.Enableable.DEPTH_TEST)
        self.ctx.clear_color(0.1, 0.2, 0.4, 1)

        self._MOUSE_DRAG_SPEED = 4
        self._FRICTION = 0.95
        self._mouse_x, self._mouse_y = -1, -1
        self._delta_x, self._delta_y = 0, 0
        self._theta, self._phi = 0, 0
        self._r = -5

        # self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)

    def on_framebuffer_resize(self, width: int, height: int):
        self.program['projection'] = px.transform.perspective(60, width / height, 1, 10)
        self.ctx.viewport(0, 0, width, height)

    def on_mouse_button(self, button: px.Button, action: px.Action, modifiers: px.Modifiers):
        if button == px.Button.LEFT and action == px.Action.PRESS:
            self._mouse_x, self._mouse_y = self.mouse_position

    def on_scroll(self, x: float, y: float):
        self._r += y
        self._view = px.transform.translation([0, 0, self._r])

    def on_update(self):
        if self.get_mouse_button(px.Button.LEFT) == px.Action.PRESS:
            x, y = self.mouse_position

            self._delta_x = (self._mouse_x - x) / self.framebuffer_size[0] * self._MOUSE_DRAG_SPEED
            self._delta_y = (self._mouse_y - y) / self.framebuffer_size[1] * self._MOUSE_DRAG_SPEED

            self._mouse_x, self._mouse_y = x, y

        self._theta = np.clip(self._theta - self._delta_y, -np.pi / 2, np.pi / 2)
        self._phi = (self._phi - self._delta_x) % (2 * np.pi)

        self._model = px.transform.rotation([self._theta, self._phi, 0])

        self._delta_x *= self._FRICTION
        self._delta_y *= self._FRICTION

        modelview = self._model * self._view

        modelview_inv_t = np.ascontiguousarray(np.linalg.inv(self._model).T[:3, :3])

        self.program['modelview'] = modelview
        self.program['model_inv_t'] = modelview_inv_t

        for i in range(self._light_count):
            self._lights['position'][i] = px.transform.apply(self._lights['position'][None, i],
                                                             px.transform.rotation(self._rotation[i]))
        self._light_buffer.data = self._lights

    def on_draw(self):
        self.ctx.clear(px.gl.BufferBit.COLOR | px.gl.BufferBit.DEPTH)
        with self._light_buffer:
            self.program.draw_elements(px.gl.DrawMode.TRIANGLES, self.elements)


if __name__ == "__main__":
    WavefrontTest(px.CanvasConfig(samples=16)).run()