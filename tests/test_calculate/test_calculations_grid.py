from hgl.calculate.grid import (
    total_grid_lines, grid_snap, total_grid_lines_normalised)


def test_point_snaps_to_expected_location():
    assert grid_snap(point=[0.0, 0.0, 0.0], size=10) == [0.0, 0.0, 0.0]
    assert grid_snap(point=[5.0, 5.0, 5.0], size=10) == [10, 10, 10]
    assert grid_snap(point=[8.0, 8.0, 8.0], size=10) == [10, 10, 10]
    assert grid_snap(point=[10.0, 10.0, 10.0], size=10) == [10, 10, 10]
    assert grid_snap(point=[12.0, 12.0, 12.0], size=10) == [10, 10, 10]


def test_expected_total_grid_lines():
    assert total_grid_lines(major_scale=10, minor_scale=10, width=100, height=100, depth=100) == (10, 10, 10)

    assert total_grid_lines(major_scale=10, minor_scale=10, width=100, height=500, depth=100) == (10, 50, 10)

    assert total_grid_lines(major_scale=10, minor_scale=10, width=100, height=500, depth=0) == (10, 50, 0)


def test_expected_total_grid_lines_normalised():
    assert total_grid_lines_normalised(major_scale=10, minor_scale=10, width=100.0, height=100.0, depth=100.0) == (0.1, 0.1, 0.1)
    assert total_grid_lines_normalised(major_scale=10, minor_scale=10, width=100.0, height=500.0, depth=100.0) == (0.1, 0.02, 0.1)
    assert total_grid_lines_normalised(major_scale=10, minor_scale=10, width=100.0, height=500.0, depth=0.0) == (0.1, 0.02, 0)





