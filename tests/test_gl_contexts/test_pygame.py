#!/usr/bin/python
# noqa: E402
# PYOPENGL_PLATFORM="osmesa"
import os
import sys
import pytest

# sys.path.append(os.path.abspath('../'))
from hgl.context.pygame_context import context
fixture_path = '/home/oly/repos/FabriCAD/tests/%s'


def test_pygame_33_context_renders():
    actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
    expected_results = '%s/fixtures/test_glut_context_renders.png' % os.path.dirname(__file__)
    context().save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


def test_pygame_40_context_renders():
    actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
    expected_results = '%s/fixtures/test_glut_context_renders.png' % os.path.dirname(__file__)
    context(version=(4, 0)).save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


def test_pygame_43_context_renders():
    actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
    expected_results = '%s/fixtures/test_glut_context_renders.png' % os.path.dirname(__file__)
    context(version=(4, 3)).save(filename=actual_results)
    assert pytest.idiff(actual_results, expected_results) is True


# def test_pygame_45_context_renders():
#     actual_results = '/tmp/%s.png' % sys._getframe().f_code.co_name
#     expected_results = '/home/oly/repos/FabriCAD/tests/fixtures/test_glut_context_renders.png'
#     context(version=(4, 5)).save(filename=actual_results)
#     assert pytest.idiff(actual_results, expected_results) is True


if __name__ == '__main__':
    test_pygame_33_context_renders()
    test_pygame_40_context_renders()
    test_pygame_43_context_renders()
    # test_pygame_45_context_renders()
