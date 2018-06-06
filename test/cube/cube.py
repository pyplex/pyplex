import pyplex as px
import numpy as np


class CubeTest(px.Canvas):
    def on_start(self, ctx: px.gl.GL43):
        self.ctx = ctx

        self.program = px.Program(self.ctx,
            px.VertexShader(self.ctx, 'cube_vertex.glsl'),
            px.FragmentShader(self.ctx, 'cube_fragment.glsl'))

        N = 2000
        vertices = np.empty((N*8, 3), np.float32)
        colors = np.empty((N*8, 3), np.float32)
        elements = np.empty((N*36), np.uint32)

        for i in range(N):
            vertices[i*8:(i+1)*8] = px.transform.apply(
                px.Cube._VERTICES, px.transform.rotation(np.random.uniform(0, 2 * np.pi, 3))) * \
                                    np.random.normal(0.5, 0.2, 1) + np.random.normal(0, 10, 3)
            colors[i*8:(i+1)*8] = np.random.uniform(size=3)
            elements[i*36:(i+1)*36] = px.Cube._ELEMENTS + i * 8

        self.program['position'] = px.ArrayBuffer(self.ctx, vertices)
        self.program['color'] = px.ArrayBuffer(self.ctx, colors)
        self.elements = px.ElementArrayBuffer(self.ctx, elements)

        self.ctx.enable(px.gl.Enableable.CULL_FACE)
        self.ctx.cull_face(px.gl.CullFace.BACK)
        self.ctx.enable(px.gl.Enableable.DEPTH_TEST)
        self.ctx.clear_color(0.5, 0.25, 0.125, 1)

        self._MOUSE_DRAG_SPEED = 4
        self._FRICTION = 0.95
        self._mouse_x, self._mouse_y = -1, -1
        self._delta_x, self._delta_y = 0, 0
        self._theta, self._phi = 0, 0
        self._r = -50

        self._model = px.transform.identity()
        self._view = px.transform.translation([0, 0, self._r])
        self._projection = px.transform.perspective(60, 1, 0.1, 200)

        # self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)

    def on_framebuffer_resize(self, width: int, height: int):
        self._projection = px.transform.perspective(60, width / height, 0.1, 200)

        # S = 50; S_ = S / width * height
        # self._projection = px.transform.orthographic(-S, S, S_, -S_, 0.1, 200)

        self.ctx.viewport(0, 0, width, height)

    def on_mouse_button(self, button: px.Button, action: px.Action, modifiers: px.Modifiers):
        if button == px.Button.LEFT and action == px.Action.PRESS:
            self._mouse_x, self._mouse_y = self.mouse_position

    def on_update(self):
        if self.get_mouse_button(px.Button.LEFT) == px.Action.PRESS:
            x, y = self.mouse_position

            self._delta_x = (self._mouse_x - x) / self.framebuffer_size[0] * self._MOUSE_DRAG_SPEED
            self._delta_y = (self._mouse_y - y) / self.framebuffer_size[1] * self._MOUSE_DRAG_SPEED

            self._mouse_x, self._mouse_y = x, y

        self._theta = np.clip(self._theta - self._delta_y, -np.pi / 2, np.pi / 2)
        self._phi = (self._phi - self._delta_x) % (2 * np.pi)

        self._model = px.transform.rotation([self._theta, self._phi, 0])

        self.program['MVP'] = self._model * self._view * self._projection
        self._delta_x *= self._FRICTION
        self._delta_y *= self._FRICTION

    def on_scroll(self, x: float, y: float):
        self._r += y
        self._view = px.transform.translation([0, 0, self._r])

    def on_draw(self):
        self.ctx.clear(px.gl.BufferBit.COLOR | px.gl.BufferBit.DEPTH)
        self.program.draw_elements(px.gl.Primitive.TRIANGLES, self.elements)


if __name__ == "__main__":
    CubeTest(px.CanvasConfig(samples=32)).start()