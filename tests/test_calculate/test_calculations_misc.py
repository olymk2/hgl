from hgl.calculate.misc import interleave, interleave_uneven


def test_interleaved_results():
    list1 = range(0, 6)
    list2 = range(10, 16)
    assert [i for i in interleave(list1,list2)] == [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15]


def test_interleaved_results_with_steps():
    list1 = range(0, 6)
    list2 = range(10, 16)
    list3 = range(0, 12)
    assert [i for i in interleave(list1,list2,list2_start=2, step=2)] == [0, 1, 12, 13, 2, 3, 14, 15, 4, 5, 10, 11]

    assert [i for i in interleave(list1,list2,list1_start=2, step=2)] == [2, 3, 10, 11, 4, 5, 12, 13, 0, 1, 14, 15]

    assert [i for i in interleave(list1,list2,list1_start=2, step=3)] == [2, 3, 4, 10, 11, 12, 5, 0, 1, 13, 14, 15]
    assert [i for i in interleave_uneven(list1,list3, list1_step=1, list2_step=2)] == [0, 0, 1, 1, 2, 3, 2, 4, 5, 3, 6, 7, 4, 8, 9, 5, 10, 11]
