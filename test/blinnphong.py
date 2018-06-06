import pyplex as px
from pyplex import gl
import numpy as np


class BlinnPhongTest(px.Canvas):

    UP = np.array([0, 1, 0], np.float32)
    RIGHT = np.array([1, 0, 0], np.float32)

    ROTATION_SPEED = 3

    def on_start(self, ctx: gl.GL_ANY):
        self.ctx = ctx

        plane = px.Plane()
        sphere = px.Sphere(64, 32)

        self.meshes = [
            px.Mesh(self.ctx, plane.elements, plane.vertices, plane.uvs, plane.normals),
            px.Mesh(self.ctx, sphere.elements, sphere.vertices, normals=sphere.normals)
        ]
        self.transform = px.identity()

        self.program = px.Program(ctx,
            px.VertexShader(ctx, '../pyplex/glsl/blinn_phong/blinn_phong.vs'),
            px.FragmentShader(ctx, '../pyplex/glsl/blinn_phong/blinn_phong.fs'))

        self.camera = px.TrackBallCamera(self.ctx, 60, 1, 0.01, 10,
                                         px.vec3(0, 0, 0), px.vec3(0, 1, 0), np.pi/5, np.pi/4, 2)

        self.point_lights = [
            px.PointLight(self.ctx, px.vec3(0, 2, 0), px.vec3(1, 1, 1), px.float32(1), px.float32(0.1))
        ]

        self.program['Camera'] = self.camera.buffer
        self.program['ambient'] = px.vec3(0.025, 0.05, 0.1)

        self.program['Ns'] = px.float32(32)
        self.program['Ka'] = px.vec3(1, 1, 1)
        self.program['Kd'] = px.vec3(0.5, 0.5, 0.5)
        self.program['Ks'] = px.vec3(0.5, 0.5, 0.5)

        self.program['model'] = self.transform
        self.program['model_1T'] = np.ascontiguousarray(np.linalg.inv(self.transform).T[:3, :3])

        self.program['PointLightCount'] = px.int32(len(self.point_lights))
        for i, light in enumerate(self.point_lights):
            self.program['PointLight[{}]'.format(i)] = light.buffer

        self.ctx.clear_color(0.25, 0.5, 1.0, 1.0)

        self.ctx.enable(gl.DEPTH_TEST)
        self.ctx.enable(px.gl.Enableable.CULL_FACE)
        self.ctx.cull_face(px.gl.CullFace.BACK)

        self.theta = self.phi = 0.0
        self.x_prev = self.y_prev = 0.0

    def on_framebuffer_resize(self, width: int, height: int):
        if width and height:
            self.camera.aspect = width / height
            self.ctx.viewport(0, 0, width, height)

    def on_mouse_move(self, x: float, y: float):
        if self.get_mouse_button(px.Button.LEFT):
            self.camera.theta = np.clip(
                self.camera.theta - self.ROTATION_SPEED * (y - self.y_prev) / self.framebuffer_size[0], 0.01, np.pi)
            self.camera.phi = (self.camera.phi + self.ROTATION_SPEED * (x - self.x_prev) / self.framebuffer_size[1]) % (
                        2 * np.pi)
        if self.get_mouse_button(px.Button.RIGHT) or self.get_mouse_button(px.Button.MIDDLE):
            up = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.UP)))[0]
            right = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.RIGHT)))[0]
            self.camera.pivot += (-(x - self.x_prev) * right + (y - self.y_prev) * up) * 0.01
        self.x_prev, self.y_prev = x, y

    def on_scroll(self, x: float, y: float):
        self.camera.radius -= self.camera.radius * y * 0.1
        self.camera.fov = np.clip(self.camera.fov + x, 10, 90)

    def on_draw(self):
        self.ctx.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)

        for mesh in self.meshes:
            self.program.vao = mesh.vao
            self.program.draw_elements(gl.Primitive.TRIANGLES, mesh.faces)


if __name__ == "__main__":
    BlinnPhongTest().run()