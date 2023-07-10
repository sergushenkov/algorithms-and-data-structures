from abst import aBST
import pytest


def test_init():
    tree_0 = aBST(0)
    tree_0.size == 1
    assert tree_0.Tree[0] is None
    tree_0.Tree[0] = 1
    assert tree_0.Tree[0] == 1
    with pytest.raises(IndexError):
        tree_0.Tree[1]
    tree_3 = aBST(3)
    tree_3.size == 15
    assert tree_3.Tree[0] is None
    assert tree_3.Tree[14] is None
    with pytest.raises(IndexError):
        tree_3.Tree[15]


def test_find_key_index():
    tree_3 = aBST(3)
    i = 0
    for key in (50, 25, 75, None, 37, 62, 84, None, None, 31, 43, 55, None, None, 92):
        tree_3.Tree[i] = key
        i += 1
    assert tree_3.FindKeyIndex(44) is None
    assert tree_3.FindKeyIndex(37) == 4
    assert tree_3.FindKeyIndex(43) == 10
    assert tree_3.FindKeyIndex(50) == 0
    assert tree_3.FindKeyIndex(84) == 6
    assert tree_3.FindKeyIndex(74) == -12
    assert tree_3.FindKeyIndex(10) == -3


def test_add_key():
    tree_3 = aBST(3)
    key =   (50, 50, 25, 75, 50, 25, 37, 31, 43, 62, 84, 55, 92, 55, 30, 100)
    answer = (0,  0,  1,  2,  0,  1,  4,  9, 10,  5,  6, 11, 14, 11, -1,  -1)
    for key, answer in zip(key, answer):
        assert tree_3.AddKey(key) == answer
