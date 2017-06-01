#!/usr/bin/env python
import sys

from OpenGL import GLUT
from hgl.context.template import template_context


class context(template_context):
    """Basic opengl context using glut widget"""

    def __init__(self, shader_programs=None, version=(3, 3)):
        try:
            GLUT.glutInit([])
        except:
            print("freeglut missing, try "
                  "'sudo apt-get install freeglut3' or similar")
            sys.exit(1)

        # make a window
        GLUT.glutInitContextVersion(version[0], version[1])
        GLUT.glutInitContextFlags(GLUT.GLUT_FORWARD_COMPATIBLE)
        GLUT.glutInitContextProfile(GLUT.GLUT_COMPATIBILITY_PROFILE)
        GLUT.glutInitContextProfile(GLUT.GLUT_CORE_PROFILE)
        GLUT.glutInitDisplayMode(
            GLUT.GLUT_RGBA | GLUT.GLUT_DOUBLE | GLUT.GLUT_DEPTH)

        GLUT.glutInitWindowSize(self.viewport[2], self.viewport[3])
        GLUT.glutCreateWindow("pyopengl with glut")

        GLUT.glutDisplayFunc(self.render)
        GLUT.glutIdleFunc(self.render)

        self.update()

    def info(self):
        print('Created GLUT context')
        super(context, self).info()

    def render(self):
        super(context, self).render()
        GLUT.glutSwapBuffers()

    def run(self):
        GLUT.glutMainLoop()
        return True
