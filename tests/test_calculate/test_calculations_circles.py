from hgl.calculate import circle
from hgl.calculate.angle import calculate_segments
from hgl.calculate.circle import orbit


def test_interpolate_points_from_centre():
    points = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
    assert circle.interpolate_points_from_centre((0, 0, 0), points, radius=2) == [[2, 0, 0], [0, 2, 0], [-2, 0, 0], [0, -2, 0]]


def test_interpolate_between_points_from_centre():
    points = [(1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
    assert circle.interpolate_between_points_from_centre((0, 0, 0), points) == [[1.0, 1.0, 0.0], [-1.0, 1.0, 0.0], [-1.0, -1.0, 0.0], [1.0, -1.0, 0.0]]


def test_calculating_circle_segments():
    assert calculate_segments(center=(0,0,0), start_angle=0, end_angle=6.28, radius=4, segments = 6) == [(4.0, 0.0, 0), (1.2384912522280969, 3.8034378420258794, 0), (-3.2330697090772396, 2.355262247871181, 0), (-3.240555528495997, -2.3449519966801082, 0), (1.2263698718763947, -3.8073635152627427, 0), (3.9999797076535, -0.01274120717255355, 0)]


def test_circle_orbit_function():
    time_increments = [i * 0.1 for i in range(0,10)]
    generated_x_axes_test_results = [
        orbit(origin=(0,0,0), radius=10, time=t, axes=(0,1,1))
        for t in time_increments]
    expected_x_axes_results = [
        (0, 10.0, 0.0),
        (0, 8.090169943749475, 5.877852522924732),
        (0, 3.0901699437494745, 9.510565162951535),
        (0, -3.0901699437494754, 9.510565162951535),
        (0, -8.090169943749473, 5.877852522924733),
        (0, -10.0, 1.2246467991473533e-15),
        (0, -8.090169943749473, -5.877852522924734),
        (0, -3.0901699437494754, -9.510565162951535),
        (0, 3.0901699437494723, -9.510565162951536),
        (0, 8.090169943749473, -5.877852522924734)]

    generated_y_axes_test_results = [
        orbit(origin=(0,0,0), radius=10, time=t, axes=(1,0,1))
        for t in time_increments]
    expected_y_axes_results = [
        (10.0, 0, 0.0),
        (8.090169943749475, 0, 5.877852522924732),
        (3.0901699437494745, 0, 9.510565162951535),
        (-3.0901699437494754, 0, 9.510565162951535),
        (-8.090169943749473, 0, 5.877852522924733),
        (-10.0, 0, 1.2246467991473533e-15),
        (-8.090169943749473, 0, -5.877852522924734),
        (-3.0901699437494754, 0, -9.510565162951535),
        (3.0901699437494723, 0, -9.510565162951536),
        (8.090169943749473, 0, -5.877852522924734)]

    generated_z_axes_test_results = [
        orbit(origin=(0,0,0), radius=10, time=t, axes=(1,1,0))
        for t in time_increments]
    expected_z_axes_results = [
        (0.0, 10.0, 0),
        (5.877852522924732, 8.090169943749475, 0),
        (9.510565162951535, 3.0901699437494745, 0),
        (9.510565162951535, -3.0901699437494754, 0),
        (5.877852522924733, -8.090169943749473, 0),
        (1.2246467991473533e-15, -10.0, 0),
        (-5.877852522924734, -8.090169943749473, 0),
        (-9.510565162951535, -3.0901699437494754, 0),
        (-9.510565162951536, 3.0901699437494723, 0),
        (-5.877852522924734, 8.090169943749473, 0)]

    # test rotation around world origin
    assert generated_x_axes_test_results == expected_x_axes_results
    assert generated_y_axes_test_results == expected_y_axes_results
    assert generated_z_axes_test_results == expected_z_axes_results
