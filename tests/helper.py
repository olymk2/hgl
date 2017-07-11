#!/usr/bin/python
import os
import numpy
import pytest
from hgl import context as ctx
from hgl.context import gtkglarea_context
# from hgl.context import pygame_context
from hgl.context import glut_context
from hgl.context import sdl2_context
try:
    from hgl.context.pygame_context.context import pygame_context
except ImportError:
    pygame_context = None

test_root = os.path.dirname(__file__)
fixture_root = os.path.join(
    test_root,
    'fixtures')

versions = [(3, 3), (4, 0), (4, 3), (4, 5)]
contexts = [
    (gtkglarea_context.context, 'gtk'),
    (sdl2_context.context, 'sdl2'),
    (glut_context.context, 'glut')]
    # (pygame_context.context, 'pygame')]
if pygame_context:
    contexts.append((pygame_context.context, 'pygame'))


triangle = numpy.array([
    0.6,  0.6, 0.0,
    -0.6,  0.6, 0.0,
    0.0, -0.6, 0.0],
    dtype=numpy.float32)

triangle_uv = numpy.array([
    0.6,  0.6, 0.0, 1.0,
    -0.6,  0.6, 0.0, 1.0,
    0.0, -0.6, 0.0, 1.0],
    dtype=numpy.float32)

simple_texture_vs = ["""
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


simple_texture_fs = ["""
    #version 330

    in vec2 tex_coords;
    uniform sampler2D quad_texture;

    out vec4 fragColor;
    void main(){
        //fragColor = vec4(tex_coords, 0.5, 0.0);
        fragColor = texture2D(quad_texture, tex_coords);
        //fragColor = vec4(1.0, 0.0, 0.0, 1.0);
    }"""]
