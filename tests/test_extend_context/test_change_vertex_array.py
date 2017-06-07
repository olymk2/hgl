#!/usr/bin/python
# noqa: E402
# PYOPENGL_PLATFORM="osmesa"
import os
import sys
import pytest

import numpy as np
# sys.path.append(os.path.abspath('../'))
from hgl import context as ctx
from hgl.context import gtkglarea_context
from hgl.context import pygame_context
from hgl.context import glut_context

from OpenGL import GL

versions = [(3, 3), (4, 0), (4, 3), (4, 5)]
contexts = [
    (gtkglarea_context.context, 'gtk'),
    (glut_context.context, 'glut'),
    (pygame_context.context, 'pygame')]


@pytest.mark.parametrize("version", versions)
@pytest.mark.parametrize("test_ctx, name", contexts)
def test_change_vertex_array(name, test_ctx, version):
    filename = '%s_%s_%d.%d.png' % (
        sys._getframe().f_code.co_name,
        name,
        version[0],
        version[1])
    actual_results = '/tmp/%s' % (filename)
    expected_results = '%s/fixtures/%s' % (
        os.path.dirname(__file__),
        filename)

    class custom_context(test_ctx):
        default_vertices = np.array([
            -0.5,  0.5, 0.0,1.0,
            -0.5,  -0.5, 0.0, 0.5,
            0.5,  0.5, 0.0, 1.0,
            0.5,  -0.5, 0.0, 1.0],
            dtype=np.float32)

        default_indicies = np.array([
            0, 1, 2, 0, 2, 3])

        def draw_data(self):
            GL.glBindVertexArray(self.vertex_array_object)
            # GL.glDrawArrays(mode=GL.GL_TRIANGLE_STRIP, first=1, count=3)
            GL.glDrawArrays(GL.GL_TRIANGLE_STRIP, 0, 4)
            GL.glBindVertexArray(0)

    new_ctx = custom_context()
    new_ctx.save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


if __name__ == '__main__':
    test_change_shaders()
