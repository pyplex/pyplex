import pyplex as px
import numpy as np


class Mandelbrot(px.Canvas):
    """
    Interactively Renders Mandelbrot Set on GPU,

    Move by left clicking and dragging the mouse
    Zoom with the scroll wheel
    """

    ITERATIONS = 200  # Mandelbrot Iterations | Trade-off between Performance and Fractal Depth
    ZOOM_SPEED = 0.1  # Speed of Mouse Scroll Wheel zoom

    def __init__(self):
        super().__init__(title="Mandelbrot | pyplex", wait_for_events=True)

        # Variables for Mouse Controls
        self.zoom, self.pan = 2, np.array([-0.75, 0, 0], np.float32)
        self.last_position, self.drag = None, False

        # Data to be uploaded to the GPU as numpy arrays
        self.quad = np.array([[-1, -1], [-1, 1], [1, 1], [-1, -1], [1, 1], [1, -1]], np.float32)  # Quad in Screen Space
        self.colormap = np.random.uniform(size=(10, 3)).astype(np.float32)  # Random Colormap (of length 10)
        self.colormap[0] *= 0.2  # Ensure Base Color is quite dark
        self.iterations = np.array([self.ITERATIONS], np.int32)  # Recursion Depth for Mandelbrot Function

        # Load Vertex and Fragment Shaders from disk
        with open('mandelbrot_vertex.glsl') as vertex_file, open('mandelbrot_fragment.glsl') as fragment_file:
            vertex_shader = px.VertexShader(self.ctx, vertex_file.read())
            fragment_shader = px.FragmentShader(self.ctx, fragment_file.read())

        # Create Program using the Vertex & Fragment Shader and set Program Input/Uniforms
        self.program = px.Program(self.ctx, vertex_shader, fragment_shader)
        self.program.input('position', px.ArrayBuffer(self.ctx, self.quad))
        self.program.uniform('iterations', self.iterations)
        self.program.uniform('colormap', self.colormap)

        # Resize Framebuffer to ensure Projection Matrix gets updated
        self.on_framebuffer_resize(self.size)

    def on_framebuffer_resize(self, size: np.ndarray):
        """Update Viewport and Projection whenever User resizes the window"""

        self.ctx.viewport(size)
        aspect = size[1] / size[0]
        self.program.uniform('projection', px.orthographic(-aspect, aspect, -1, 1, (0, 1)))
        self.update()

    def on_scroll(self, offset: np.ndarray):
        """Set Zoom level when User scrolls mouse"""

        self.zoom -= np.sum(offset) * self.ZOOM_SPEED * self.zoom

    def on_mouse_button(self, button: px.Button, action: px.Action, modifier: px.Modifier):
        """Check if User is dragging the mouse"""

        if button == px.Button.LEFT:
            if action == px.Action.PRESS:
                self.drag = True
            elif action == px.Action.RELEASE:
                self.drag = False
                self.last_position = None

    def on_mouse_move(self, position: np.ndarray):
        """Pan view whenever User is dragging the mouse"""

        if self.drag:
            if not self.last_position is None:
                delta = position - self.last_position
                self.pan[0] -= 2 * delta[0] / self.height * self.zoom
                self.pan[1] += 2 * delta[1] / self.height * self.zoom
            self.last_position = position

    def on_draw(self):
        """Update View and Draw Mandelbrot"""

        view = np.eye(4, 4, dtype=np.float32)
        view = np.dot(px.scale(self.zoom), view)
        view = np.dot(px.translation(self.pan), view)
        self.program.uniform('view', view)

        self.program.draw(px.DrawMode.TRIANGLES)


if __name__ == "__main__":
    with Mandelbrot() as canvas:    # Initialize Canvas
        canvas.run()                # Run Program