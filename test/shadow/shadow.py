import pyplex as px
from pyplex import gl

import numpy as np
from time import time

import os


class ShadowTest(px.Canvas):

    CONTAINER_PATH = os.path.abspath('../../img/container.jpg')

    def on_start(self, ctx: gl.GL43):
        self.ctx = ctx

        # Camera Definition #
        self.camera_fov = 30
        self.camera_near = 0.1
        self.camera_far = 10

        self.camera_pos = np.array([1, 2, 2], np.float32)
        self.camera_center = np.array([0, 0.10, 0], np.float32)
        self.camera_up = np.array([0, 1, 0], np.float32)
        self.view = px.transform.look_at(self.camera_pos, self.camera_center, self.camera_up)

        # Light Definition #
        self.light_pos = np.array([-10, 10, 10], np.float32)

        # Plane Definition #
        plane = px.Plane()
        self.plane_transform = px.transform.identity()
        self.plane_program = px.Program(self.ctx,
                                        px.VertexShader(self.ctx, 'lambert_vertex.glsl'),
                                        px.FragmentShader(self.ctx, 'lambert_fragment.glsl'))

        self.plane_elements = px.ElementArrayBuffer(self.ctx, plane.elements)
        self.plane_vertices = px.ArrayBuffer(self.ctx, plane.vertices)
        self.plane_program['position'] = self.plane_vertices
        self.plane_program['normal'] = px.ArrayBuffer(self.ctx, plane.normals)
        self.plane_program['albedo'] = np.array([1, 0.75, 0.5], np.float32)


        # Object Definition #
        obj = px.loader.wavefront('../../obj/suzanne.obj')
        obj.recalculate_normals()
        self.cube_transform = px.transform.scale(0.2) * px.transform.translation([0, 0.1, 0]) * px.transform.rotation_x(-np.pi / 4)
        self.cube_program = px.Program(self.ctx,
                                        px.VertexShader(self.ctx, 'lambert_vertex.glsl'),
                                        px.FragmentShader(self.ctx, 'lambert_fragment.glsl'))
        self.cube_elements = px.ElementArrayBuffer(self.ctx, obj.elements)
        self.cube_vertices = px.ArrayBuffer(self.ctx, obj.vertices)
        self.cube_program['position'] = self.cube_vertices
        self.cube_program['normal'] = px.ArrayBuffer(self.ctx, obj.normals)
        self.cube_program['albedo'] = np.array([0.5, 0.75, 1.0], np.float32)

        # Shadow Definition #
        self.shadow_program = px.Program(self.ctx,
            px.VertexShader(self.ctx, 'depth_vertex.glsl'),
            px.FragmentShader(self.ctx, 'depth_fragment.glsl'))

        self.shadow_resolution = 1024
        self.shadow_area = 1
        self.shadow_near = 1
        self.shadow_far = 20
        self.shadow_bias = 0.001
        self.depth_map = px.DepthTexture2D(self.ctx, self.shadow_resolution, self.shadow_resolution, px.TextureFilter.nearest())
        self.depth_map_fbo = px.FrameBuffer(self.ctx, depth=self.depth_map)
        self.light_projection = px.transform.orthographic(-self.shadow_area, self.shadow_area,
                                                          -self.shadow_area, self.shadow_area,
                                                          self.shadow_near, self.shadow_far)

        self.light_view = px.transform.look_at(self.light_pos, self.camera_center, self.camera_up)
        self.light_space = self.light_view * self.light_projection
        self.shadow_program['light_space'] = self.light_space
        self.cube_program['light_space'] = self.light_space
        self.plane_program['light_space'] = self.light_space

        self.shadow_program['model'] = self.cube_transform
        self.shadow_program['position'] = self.cube_vertices

        self.cube_program['shadow_map'] = self.depth_map
        self.plane_program['shadow_map'] = self.depth_map

        # Texture Display Program #
        self.texture_program = px.Program(self.ctx,
            px.VertexShader(self.ctx, 'quad_vertex.glsl'),
            px.FragmentShader(self.ctx, 'quad_fragment.glsl'))

        self.texture_program['position'] = px.ArrayBuffer(self.ctx, px.Quad().vertices)
        self.texture_program['uv'] = px.ArrayBuffer(self.ctx, px.Quad().uvs)
        self.texture_program['tex'] = self.depth_map
        self.texture_program_elements = px.ElementArrayBuffer(self.ctx, px.Quad().elements)

        self._MOUSE_DRAG_SPEED = 4
        self._FRICTION = 0.95
        self._mouse_x, self._mouse_y = -1, -1
        self._delta_x, self._delta_y = 0, 0
        self._theta, self._phi = np.pi/4, np.pi/4
        self.r = 3

        self.ctx.enable(px.gl.Enableable.CULL_FACE)
        self.ctx.clear_color(0.1, 0.2, 0.4, 1)

        # self.ctx.polygon_mode(px.gl.CullFace.FRONT_AND_BACK, px.gl.PolygonMode.LINE)

    def on_framebuffer_resize(self, width: int, height: int):
        self.projection = px.transform.perspective(self.camera_fov, width / height, self.camera_near, self.camera_far)
        self.ctx.viewport(0, 0, width, height)

    def on_mouse_button(self, button: px.Button, action: px.Action, modifiers: px.Modifiers):
        if button == px.Button.LEFT and action == px.Action.PRESS:
            self._mouse_x, self._mouse_y = self.mouse_position

    def on_scroll(self, x: float, y: float):
        self.r = np.clip(self.r - y, self.camera_near * 4, self.camera_far/2)
        self._view = px.transform.translation([0, 0, self.r])

    def on_update(self):
        if self.get_mouse_button(px.Button.LEFT) == px.Action.PRESS:
            x, y = self.mouse_position

            self._delta_x = (self._mouse_x - x) / self.framebuffer_size[0] * self._MOUSE_DRAG_SPEED
            self._delta_y = (self._mouse_y - y) / self.framebuffer_size[1] * self._MOUSE_DRAG_SPEED

            self._mouse_x, self._mouse_y = x, y

        epsilon = 0.001
        self._theta = np.clip(self._theta + self._delta_y, epsilon, np.pi/2-epsilon)
        self._phi = (self._phi - self._delta_x) % (2*np.pi)

        self.camera_pos = np.array([self.r * np.sin(self._theta) * np.cos(self._phi),
                                    self.r * np.cos(self._theta),
                                    self.r * np.sin(self._theta) * np.sin(self._phi)], np.float32)

        self.view = px.transform.look_at(self.camera_pos, self.camera_center, self.camera_up)

        self._delta_x *= self._FRICTION
        self._delta_y *= self._FRICTION

        self.plane_program['MVP'] = self.plane_transform * self.view * self.projection
        self.plane_program['M1T'] = np.ascontiguousarray(np.linalg.inv(self.plane_transform).T[:3,:3])
        self.plane_program['view_pos'] = self.camera_pos

        self.cube_program['MVP'] = self.cube_transform * self.view * self.projection
        self.cube_program['M1T'] = np.ascontiguousarray(np.linalg.inv(self.cube_transform).T[:3,:3])
        self.cube_program['view_pos'] = self.camera_pos

        light_r = 10
        self.light_pos = np.array([light_r * np.sin(time()), light_r, light_r * np.cos(time())], np.float32)
        self.cube_program['light_pos'] = self.light_pos
        self.plane_program['light_pos'] = self.light_pos

        self.light_view = px.transform.look_at(self.light_pos, self.camera_center, self.camera_up)
        self.light_space = self.light_view * self.light_projection
        self.shadow_program['light_space'] = self.light_space
        self.cube_program['light_space'] = self.light_space
        self.plane_program['light_space'] = self.light_space

    def on_draw(self):
        self.ctx.enable(px.gl.Enableable.DEPTH_TEST)
        with self.depth_map_fbo:
            self.ctx.viewport(0, 0, self.shadow_resolution, self.shadow_resolution)
            self.ctx.clear(gl.BufferBit.DEPTH)
            self.ctx.disable(gl.Enableable.CULL_FACE)
            self.shadow_program.draw_elements(gl.Primitive.TRIANGLES, self.cube_elements)
            self.ctx.enable(gl.Enableable.CULL_FACE)

        self.ctx.viewport(0, 0, self.framebuffer_size[0], self.framebuffer_size[1])

        self.ctx.clear(gl.BufferBit.COLOR | gl.BufferBit.DEPTH)
        self.ctx.cull_face(px.gl.CullFace.BACK)
        self.plane_program.draw_elements(gl.Primitive.TRIANGLES, self.plane_elements)
        self.cube_program.draw_elements(gl.Primitive.TRIANGLES, self.cube_elements)

        # # Debug View :)
        # self.ctx.disable(px.gl.Enableable.DEPTH_TEST)
        # self.texture_program.draw_elements(gl.DrawMode.TRIANGLES, self.texture_program_elements)
        # self.ctx.enable(px.gl.Enableable.DEPTH_TEST)



if __name__ == "__main__":
    ShadowTest(px.CanvasConfig(samples=16)).run()