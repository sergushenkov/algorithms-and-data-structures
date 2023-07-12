from bbstarray import GenerateBBSTArray


def test_generate_bbst_array():
    assert GenerateBBSTArray(()) == ()
    assert GenerateBBSTArray((1,)) == (1,)
    src = (2, 1, 0)
    dst = (1, 0, 2)
    assert GenerateBBSTArray(src) == (dst)
    src = (0, 6, 1, 5, 2, 4, 3)
    dst = (3, 1, 5, 0, 2, 4, 6)
    assert GenerateBBSTArray(src) == (dst)
    src = (1, 2, 3, 7, 8, 9, 13, 14, 4, 5, 6, 10, 11, 12, 0)
    dst = (7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14)
    assert GenerateBBSTArray(src) == (dst)
