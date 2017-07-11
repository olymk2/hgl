from hgl.calculate.origin import rotate, mirror


def test_mirror_point():
    assert mirror((2, 2,0), x=1, y=-1) == [2, -2, 0]


def test_rotate_around_origin():
    result = [format(n,'f') for n in rotate((5, 0, 0), angle=90)]
    assert result == ['0.000000', '5.000000', '0.000000']

    result = [format(n,'f') for n in rotate((0, 5, 0), angle=90)]
    assert result == ['-5.000000', '0.000000', '0.000000']

