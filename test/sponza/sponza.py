import pyplex as px
from pyplex import gl
import numpy as np
import os

class Sponza(px.Canvas):

    PATH = os.path.join(os.path.dirname(__file__), '../../obj/sponza/sponza.obj')

    UP = np.array([0, 1, 0], np.float32)
    RIGHT = np.array([1, 0, 0], np.float32)
    FORWARD = np.array([0, 0, -1], np.float32)

    ROTATION_SPEED = 3

    def on_start(self, ctx: gl.GL_ANY):
        self.ctx = ctx

        self.program = px.Program(ctx,
            px.VertexShader(ctx, '../../pyplex/glsl/blinn_phong/blinn_phong.vs'),
            px.FragmentShader(ctx, '../../pyplex/glsl/blinn_phong/blinn_phong.fs'))

        self.asset = px.AssetImporter(ctx, Sponza.PATH)
        self.meshes = self.asset.meshes

        self.albedos = np.random.uniform(size=(len(self.meshes), 3)).astype(np.float32)

        self.transform = px.identity()

        self.camera = px.TrackBallCamera(self.ctx, 60, 1, 1, 5000, px.vec3(0, 100, 0), px.vec3(0, 1, 0), np.pi/2, 0, 500)

        self.point_lights = [
            px.PointLight(self.ctx,
                          px.vec3(np.random.uniform(-1000, 1000),
                                  np.random.uniform(100, 500),
                                  np.random.uniform(-500, 500)),
                          px.normalize(np.random.uniform(0, 1, 3).astype(np.float32)),
                          px.float32(20), px.float32(0.001)) for i in range(12)]

        self.program['Camera'] = self.camera.buffer
        self.program['ambient'] = px.vec3(0.1, 0.1, 0.1)

        self.program['Ns'] = px.float32(8)
        self.program['Ka'] = px.vec3(1, 1, 1)
        self.program['Kd'] = px.vec3(0.5, 0.5, 0.5)
        self.program['Ks'] = px.vec3(0.5, 0.5, 0.5)

        self.program['model'] = self.transform
        self.program['model_1T'] = np.ascontiguousarray(np.linalg.inv(self.transform).T[:3,:3])

        self.program['PointLightCount'] = px.int32(len(self.point_lights))
        for i, light in enumerate(self.point_lights):
            self.program['PointLight[{}]'.format(i)] = light.buffer

        self.ctx.clear_color(0.25, 0.5, 1.0, 1.0)

        self.ctx.enable(gl.DEPTH_TEST)
        self.ctx.enable(px.gl.Enableable.CULL_FACE)
        self.ctx.cull_face(px.gl.CullFace.BACK)
        # self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)

        self.theta = self.phi = 0.0
        self.x_prev = self.y_prev = 0.0

    def on_framebuffer_resize(self, width: int, height: int):
        if width and height:
            self.camera.aspect = width / height
            self.ctx.viewport(0, 0, width, height)

    def on_mouse_move(self, x: float, y: float):
        if self.get_mouse_button(px.Button.LEFT):
            self.camera.theta = np.clip(self.camera.theta - self.ROTATION_SPEED * (y - self.y_prev) / self.framebuffer_size[0], 0.01, np.pi)
            self.camera.phi = (self.camera.phi + self.ROTATION_SPEED * (x - self.x_prev) / self.framebuffer_size[1]) % (2* np.pi)

        if self.get_mouse_button(px.Button.RIGHT) or self.get_mouse_button(px.Button.MIDDLE):
            up = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.UP)))[0]
            right = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.RIGHT)))[0]
            self.camera.pivot = self.camera.pivot - (x - self.x_prev) * right + (y - self.y_prev) * up

        self.x_prev, self.y_prev = x, y

    def on_key(self, key: px.Key, action: px.Action, modifiers: px.Modifiers):
        if key == px.Key.SPACE and (action == px.Action.PRESS or action == px.Action.REPEAT):
            for light in self.point_lights:
                light.position = px.vec3(np.random.uniform(-1000, 1000), np.random.uniform(0, 1000), np.random.uniform(-700, 700))
                light.color = px.normalize(np.random.uniform(size=3).astype(np.float32))

    def on_scroll(self, x: float, y: float):
        self.camera.radius -= self.camera.radius * y * 0.1
        self.camera.fov = np.clip(self.camera.fov + x, 10, 90)

    def on_update(self, dt: float):

        pivot = np.zeros(3, np.float32)

        multiplier = 4

        if self.get_key(px.Key.LEFT_SHIFT) == px.Action.PRESS:
            multiplier = 8

        if self.get_key(px.Key.W) == px.Action.PRESS:
            forward = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.FORWARD)))[0]
            pivot += forward * multiplier

        if self.get_key(px.Key.S) == px.Action.PRESS:
            forward = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.FORWARD)))[0]
            pivot -= forward * multiplier

        if self.get_key(px.Key.D) == px.Action.PRESS:
            right = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.RIGHT)))[0]
            pivot += right * multiplier

        if self.get_key(px.Key.A) == px.Action.PRESS:
            right = np.asarray(px.normalize(np.dot(self.camera.view[:3, :3], self.RIGHT)))[0]
            pivot -= right * multiplier

        self.camera.pivot += pivot

    def on_draw(self):
        self.ctx.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)
        for mesh, albedo in zip(self.meshes, self.albedos):
            self.program.draw_elements(mesh.vao, gl.Primitive.TRIANGLES, mesh.faces)


if __name__ == "__main__":
    Sponza().run()