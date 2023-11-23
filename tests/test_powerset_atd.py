from powerset_atd import PowerSet

def test_iter():
    s1 = PowerSet()
    s1.put('A')
    s1.put('B')
    for ch in s1:
        assert ch in ('A', 'B') 

def test_issubset():
    s1 = PowerSet()
    s2 = PowerSet()
    assert s1.issubset(s2)
    s2.put('A')
    assert not s1.issubset(s2)
    s1.put('A')
    assert s1.issubset(s2)
    s1.put('B')
    assert s1.size() == 2
    assert s2.size() == 1
    assert s1.issubset(s2)
    s2.put('C')
    assert not s1.issubset(s2)

def test_sum():
    s1 = PowerSet()
    s1.put('A')
    s1.put('B')
    s2 = PowerSet()
    s2.put('A')
    s2.put('C')
    s_intersection = s1.intersection(s2)
    assert s_intersection.size() == 1
    assert s_intersection.get('A')
    s_union = s1.union(s2)
    assert s_union.size() == 3
    assert s_union.get('A')
    assert s_union.get('B')
    assert s_union.get('C')
    s_difference = s1.difference(s2)
    assert s_difference.size() == 1
    assert s_difference.get('B')