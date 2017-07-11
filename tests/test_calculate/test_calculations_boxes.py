from hgl.calculate import box
from hgl.calculate.box import is_point_in_box, external_point_direction


def test_cordinate_outside_box():
    box = [
        [50,  50], [150, 50], 
        [150, 50], [150, 150]]

    assert is_point_in_box(point=[0,0,0], box=box) == False
    assert is_point_in_box(point=[100,100,0], box=box) == True


def test_points_are_outside_box_return_side():
    box = [
        [50,  50], [150, 50], 
        [150, 50], [150, 150]]

    assert external_point_direction(point=[100,100,0], box=box) == (0, 0)
    assert external_point_direction(point=[0,0,0], box=box) == (-1, -1)
    assert external_point_direction(point=[200,100,0], box=box) == (1, 0)
    assert external_point_direction(point=[200,200,0], box=box) == (1, 1)

    box=[
        [ 20,  20], [760,  20],
        [ 20, 611], [760, 611]]

    assert external_point_direction(box=box, point = (10, 50))


def test_normal_offsets():
    assert box.box_normalized_tile_offset(x_norm=0.0, y_norm=1.0, x_tile=0, y_tile=0, size=6) == (0.0, 0.16666666666666666)

    assert box.box_normalized_tile_offset(x_norm=1.0, y_norm=1.0, x_tile=0, y_tile=0, size=6) == (0.16666666666666666, 0.16666666666666666)

    assert box.box_normalized_tile_offset(x_norm=0.0, y_norm=1.0, x_tile=1, y_tile=1, size=6) == (0.16666666666666666, 0.3333333333333333)
    assert box.box_normalized_tile_offset(x_norm=1.0, y_norm=1.0, x_tile=1, y_tile=1, size=6) == (0.3333333333333333, 0.3333333333333333)

    assert box.box_normalized_tile_offset(x_norm=0.0, y_norm=1.0, x_tile=5, y_tile=5, size=6) == (0.8333333333333333, 0.9999999999999999)
    assert box.box_normalized_tile_offset(x_norm=1.0, y_norm=1.0, x_tile=5, y_tile=5, size=6) == (0.9999999999999999, 0.9999999999999999)

    assert box.box_normalized_tile_offset(x_norm=0.0, y_norm=1.0, x_tile=6, y_tile=6, size=6) == None
    assert box.box_normalized_tile_offset(x_norm=1.0, y_norm=1.0, x_tile=6, y_tile=6, size=6) == None
