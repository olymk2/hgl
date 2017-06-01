#!/usr/bin/python
# noqa: E402
# PYOPENGL_PLATFORM="osmesa"
import os
import sys
import pytest

# sys.path.append(os.path.abspath('../'))
from hgl.context.gtkglarea_context import context


def test_gtkgl_33_context_renders():
    actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
    expected_results = '%s/fixtures/test_glut_context_renders.png' % os.path.dirname(__file__)
    context().save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


def test_gtkgl_40_context_renders():
    actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
    expected_results = '%s/fixtures/test_glut_context_renders.png'% os.path.dirname(__file__)
    context(version=(4, 0)).save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


def test_gtkgl_43_context_renders():
    actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
    expected_results = '%s/fixtures/test_glut_context_renders.png'% os.path.dirname(__file__)
    context(version=(4, 3)).save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


def test_gtkgl_45_context_renders():
    actual_results = '/tmp/test_gtkgl_45_context_renders.png'
    expected_results = '%s/fixtures/test_glut_context_renders.png'% os.path.dirname(__file__)
    context(version=(4, 5)).save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


if __name__ == '__main__':
    # context(version=(4, 5)).run()
    # context(version=(4, 5)).save(filename='/tmp/test.png')
    test_gtkgl_33_context_renders()
    test_gtkgl_40_context_renders()
    test_gtkgl_43_context_renders()
    test_gtkgl_45_context_renders()
