from hgl.calculate import angle


def test_angle_not_45_degrees():
    assert int(angle.angle([1.0, 1.0, 1.0], [2.0, 1.0, 1.0], [1.5, 1.5, 1.0])) == 45

def test_angle_not_90_degrees():
    assert int(angle.angle([1.0, 1.0, 1.0], [2.0, 1.0, 1.0], [1.0, 2.0, 1.0])) == 90

def test_angle_not_180_degrees():
    assert int(angle.angle([1.0, 1.0, 1.0], [2.0, 1.0, 1.0], [0.0, 1.0, 1.0])) == 180
