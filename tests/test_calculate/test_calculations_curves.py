from hgl.calculate.curve import generate_quadratic_bezier_curve_points, generate_cubic_bezier_curve_points, de_casteljau, generate_bezier
from hgl.calculate.misc import interleave, interleave_uneven


def test_generate_quadratic_bezier_curve():
    control_points = [(0,0,0), (20,0,0), (20,20,0)]

    expected_result_1 = [(0, 0, 0), (15.0, 5.0, 0.0), (20, 20, 0)]
    quadratic_result_1 = generate_quadratic_bezier_curve_points(control_points, 2)
    assert quadratic_result_1 == expected_result_1

    expected_result_2 = [(0, 0, 0), (11.11111111111111, 2.222222222222222, 0.0), (17.77777777777778, 8.888888888888888, 0.0), (20, 20, 0)]
    quadratic_result_2 = generate_quadratic_bezier_curve_points(control_points, 3)
    assert quadratic_result_2 == expected_result_2

#TODO use assert 
def bezier_test_two():
            # test 2 for cubic bezier curve
    phase1_expected = [[15.0, 5.0, 0.0], [30.0, 17.5, 0.0], [15.0, 30.0, 0.0]]
    phase2_expected = [[22.5, 11.25, 0.0], [22.5, 23.75, 0.0]]
    phase3_expected = [[22.5, 17.5, 0.0]]

    control_points = [(2,0,0), (2,17,0), (14,32,0), (25,32,0)]
    result_step1 = de_casteljau(control_points, 0.5)
    result_step2 = de_casteljau(result_step1, 0.5)
    result_step3 = de_casteljau(result_step2, 0.5)

    tests = testset(self.name)

    tests.append(
        result_step1 == phase1_expected,
        "de causteljau phase one has calculated incorrectly")
    tests.append(
        result_step2 == phase2_expected,
        "de causteljau phase one has calculated incorrectly")
    tests.append(
        result_step3 == phase3_expected,
        "de causteljau phase one has calculated incorrectly")
    tests.append(
        generate_bezier(control_points, 0.5) == phase3_expected,
        "de causteljau phase one has calculated incorrectly")
