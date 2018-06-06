import pyplex as px
from pyplex import gl
import numpy as np


class ModelTest(px.Canvas):

    MODEL_PATH = '../../obj/suzanne.obj'

    def on_start(self, ctx: gl.GL_ANY):
        self.ctx = ctx

        self.asset = px.AssetImporter(ctx, self.MODEL_PATH)
        self.mesh, = self.asset.meshes

        self.transform = px.transform.identity()

        self.albedo = px.vec3(1, 0.75, 0.5)
        self.specular = px.float32(0.5)
        self.shininess = px.float32(32)

        self._MOUSE_DRAG_SPEED = 4
        self._FRICTION = 0.95
        self._mouse_x, self._mouse_y = -1, -1
        self._delta_x, self._delta_y = 0, 0
        self._theta, self._phi = 0, 0
        self._r = -200

        self.fov = 60

        self.camera = px.PerspectiveCamera(ctx, self.fov, 1, 0.1, 100, px.look_at(px.vec3(0, 0, -self._r / self.fov ), px.vec3(0, 0, 0), px.vec3(0, 1, 0)))

        self.ambient = px.vec3(0.1, 0.1, 0.1)
        self.key_light = px.DirectionalLight(ctx, px.vec3(-1, 0, 1), px.vec3(1, 1, 1), px.float32(1))
        self.fill_light = px.DirectionalLight(ctx, px.vec3(1, 0, 0), px.vec3(0.5, 0.5, 1), px.float32(0.5))
        self.rim_light = px.DirectionalLight(ctx, px.vec3(-1, 1, -2), px.vec3(1, 1, 1), px.float32(4))

        self.point_light = px.PointLight(ctx, px.vec3(0, 0, 10), px.vec3(1, 0, 0), px.float32(1), px.float32(0.1))

        # self.program = px.Program(ctx,
        #     px.VertexShader(ctx, '../../pyplex/glsl/lambert/lambert.vs'),
        #     px.FragmentShader(ctx, '../../pyplex/glsl/lambert/lambert.fs'),
        #     vao=self.mesh.vao)

        self.program = px.Program(ctx,
            px.VertexShader(ctx, '../../pyplex/glsl/blinn_phong/blinn_phong.vs'),
            px.FragmentShader(ctx, '../../pyplex/glsl/blinn_phong/blinn_phong.fs'),
            vao=self.mesh.vao)

        self.program['albedo'] = self.albedo
        self.program['specular'] = self.specular
        self.program['shininess'] = self.shininess

        self.program['Camera'] = self.camera.buffer

        self.program['ambient'] = self.ambient

        self.program['DirectionalLightCount'] = px.int32(3)
        self.program['DirectionalLight[0]'] = self.key_light.buffer
        self.program['DirectionalLight[1]'] = self.fill_light.buffer
        self.program['DirectionalLight[2]'] = self.rim_light.buffer

        self.program['PointLightCount'] = px.int32(1)
        self.program['PointLight[0]'] = self.point_light.buffer

        self.ctx.clear_color(0.1, 0.2, 0.4, 1.0)

        self.ctx.enable(px.gl.Enableable.DEPTH_TEST)
        # self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)

    def on_framebuffer_resize(self, width: int, height: int):
        self.camera.aspect = width / height
        self.ctx.viewport(0, 0, width, height)

    def on_mouse_button(self, button: px.Button, action: px.Action, modifiers: px.Modifiers):
        if button == px.Button.LEFT and action == px.Action.PRESS:
            self._mouse_x, self._mouse_y = self.mouse_position

    def on_scroll(self, x: float, y: float):
        self._r += y * self._r / 10
        self.camera.fov = max(min(self.camera.fov + x, 90), 10)
        self.camera.view = px.transform.translation([0, 0, self._r / self.camera.fov])

    def on_update(self):
        if self.get_mouse_button(px.Button.LEFT) == px.Action.PRESS:
            x, y = self.mouse_position

            self._delta_x = (self._mouse_x - x) / self.framebuffer_size[0] * self._MOUSE_DRAG_SPEED
            self._delta_y = (self._mouse_y - y) / self.framebuffer_size[1] * self._MOUSE_DRAG_SPEED

            self._mouse_x, self._mouse_y = x, y

        self._theta = np.clip(self._theta - self._delta_y, -np.pi / 2, np.pi / 2)
        self._phi = (self._phi - self._delta_x) % (2 * np.pi)

        self._delta_x *= self._FRICTION
        self._delta_y *= self._FRICTION

        self.transform = px.transform.rotation([self._theta, self._phi, 0])

        self.program['model'] = self.transform
        self.program['model_1T'] = np.ascontiguousarray(np.linalg.inv(self.transform).T[:3,:3])

    def on_draw(self):
        self.ctx.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT)

        self.program['albedo'] = self.albedo
        self.ctx.polygon_offset(0, 0)
        self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.FILL)
        self.program.draw_elements(gl.Primitive.TRIANGLES, self.mesh.faces)

        self.program['albedo'] = px.vec3(0, 0, 0)
        self.ctx.polygon_offset(1, 1)
        self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)
        self.program.draw_elements(gl.Primitive.TRIANGLES, self.mesh.faces)


if __name__ == "__main__":
    ModelTest(px.CanvasConfig(samples=32)).run()