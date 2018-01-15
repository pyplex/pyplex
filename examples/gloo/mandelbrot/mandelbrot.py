import pyplex as px
import numpy as np
from time import time


class Mandelbrot(px.Canvas):

    QUAD = np.array([[-1, -1], [-1, 1], [1, 1], [-1, -1], [1, 1], [1, -1]], np.float32)

    ZOOM_SPEED = 0.1

    def __init__(self):
        super().__init__(title=self.__class__.__name__, width=1024, height=1024)

        print(self.ctx.get_int(px.StateParameter.MAX_TEXTURE_SIZE))

        self.iterations = np.array([512], np.int32)

        self.zoom = 2
        self.pan = np.array([-0.75, 0, 0], np.float32)

        self.drag = False
        self.last_position = None
        self.colormap = np.random.uniform(size=(8,3)).astype(np.float32)
        self.time = time()

        with open('mandelbrot_vertex.glsl') as vertex_file, open('mandelbrot_fragment.glsl') as fragment_file:
            vertex_shader = px.VertexShader(self.ctx, vertex_file.read())
            fragment_shader = px.FragmentShader(self.ctx, fragment_file.read())

        self.program = px.Program(self.ctx, vertex_shader, fragment_shader)
        self.program.input('position', px.ArrayBuffer(self.ctx, self.QUAD))
        self.program.uniform('iterations', self.iterations)
        self.program.uniform('colormap', self.colormap)

        self.on_framebuffer_resize(self.size)

    def on_framebuffer_resize(self, size: np.ndarray):
        self.ctx.viewport(size)
        aspect = size[1] / size[0]
        self.program.uniform('projection', px.orthographic(-aspect, aspect, -1, 1, (0, 1)))
        self.update()

    def on_scroll(self, offset: np.ndarray):
        self.zoom += np.sum(offset) * self.ZOOM_SPEED * self.zoom

    def on_mouse_move(self, position: np.ndarray):
        if self.drag:
            if not self.last_position is None:
                delta = position - self.last_position
                self.pan[0] -= 2 * delta[0] / self.height * self.zoom
                self.pan[1] += 2 * delta[1] / self.height * self.zoom
            self.last_position = position

    def on_mouse_button(self, button: px.Button, action: px.Action, modifier: px.Modifier):
        if button == px.Button.LEFT:
            if action == px.Action.PRESS:
                self.drag = True
            elif action == px.Action.RELEASE:
                self.drag = False
                self.last_position = None

    def on_draw(self):
        self.program.uniform('time', np.array([time() - self.time], np.float32))

        view = np.eye(4, 4, dtype=np.float32)
        view = np.dot(px.scale(self.zoom), view)
        view = np.dot(px.translation(self.pan), view)
        self.program.uniform('view', view)

        self.program.draw(px.DrawMode.TRIANGLES)


if __name__ == "__main__":
    with Mandelbrot() as canvas:
        canvas.run()