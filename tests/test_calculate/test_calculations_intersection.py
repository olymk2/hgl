from hgl.calculate.line import line_plane_intersection


def test_line_plane_intersection_point():
    point1 = (0.0, 0.0, 0.0)
    point2 = (0.0, 0.0, 80.0)

    assert line_plane_intersection(
        line_start=point1,
        line_end=point2,
        point_on_plane=(0.0, 0.0, 20.65975),
        direction_vector=(0, 0, 1)) == 0.258246875

    assert line_plane_intersection(
        line_start=point1,
        line_end=point2,
        point_on_plane=(0.0, 0.0, 79.65975),
        direction_vector=(0, 0, 1)) == 0.995746875


def test_line_plane_intersection_point_does_not_intersect():
    assert line_plane_intersection(
        line_start=(0, 0, 5),
        line_end=(0, 0, 10),
        point_on_plane=(0, 0, 0),
        direction_vector=(0, 0, 1)) is None

    assert line_plane_intersection(
        line_start=(0, 0, -10),
        line_end=(0, 0, 10),
        point_on_plane=(0, 0, 0),
        direction_vector=(0, 0, 1)) is not None
