import os
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
# from hgl.context.gtkglarea_context import context
from hgl.context.gtkglarea_context import context
from hgl.libs.textures import load_texture


class custom_context(context):
    vertex_list = np.array([
      0.6,  0.6, 0.0, 0.0, 1.0,
      -0.6,  0.6, 0.0, 1.0, 0.0,
      0.0, -0.6, 0.0, 0.0, 0.0],
        dtype=np.float32)
    vertex_size = 5
    vertex_stride = 4 * vertex_size


    default_vertex_shader= ["""
        #version 330

        in vec3 vertex_pos;
        in vec2 texture_pos;

        uniform mat4 modelview_mat;
        uniform mat4 projection_mat;

        out vec2 tex_coords;

        void main(){
            //# vec4 pos = modelview_mat * vec4(vertex_pos, 1.0);
            //# gl_Position = projection_mat * pos;
            gl_Position = vec4(vertex_pos, 1.0);
            tex_coords = texture_pos;
        }"""]


    default_fragment_shader = ["""
        #version 330

        in vec2 tex_coords;
        uniform sampler2D quad_texture;

        out vec4 fragColor;
        void main(){
            //fragColor = vec4(tex_coords, 0.5, 0.0);
            fragColor = texture2D(quad_texture, tex_coords);
            //fragColor = vec4(1.0, 0.0, 0.0, 1.0);
        }"""]

    def update(self):
        self.texture_id = load_texture(filename=os.path.abspath('./tests/textures/testing.png'))
        super(custom_context, self).update()
        print(self.texture_id)

    # def draw_data(self):
    #     glActiveTexture(GL_TEXTURE0)
    #     glBindTexture(GL_TEXTURE_2D, self.texture_id)
    #     glUniform1i(self.tex_uniform, 0)

    #     glBindVertexArray(self.vertex_array_object)
    #     glDrawArrays(GL_TRIANGLES, 0, 3)
    #     glBindVertexArray(0)
        
    # def compare(p1, p2):
    #     if p1<p2:
    #         return p1
    #     return p2

    # a = line_step(l1)
    # b = line_step(l2)
    # o1 = next(a)
    # o2 = next(b)


my_ctx = custom_context(version=(4,5))
# my_ctx.load_texture(filename=os.path.abspath('./tests/textures/testing.png'))
# my_ctx.run()
my_ctx.save(filename='/tmp/example_texture_context.png')
