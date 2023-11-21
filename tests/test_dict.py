from dict import Dictionary

def test_init():
    d = Dictionary()
    assert d.get_get_status() == Dictionary.GET_STATUS_OK
    assert d.get_remove_status() == Dictionary.REMOVE_STATUS_OK

def test_put():
    d = Dictionary(5)
    d.remove('A')
    assert d.get_remove_status() == Dictionary.REMOVE_STATUS_ERR
    assert not d.is_key('A')
    assert d.get('A') is None
    assert d.get_get_status() == Dictionary.GET_STATUS_ERR
    d.put('A', '777')
    assert d.is_key('A')
    assert d.get('A') == '777'
    assert d.get_get_status() == Dictionary.GET_STATUS_OK
    d.remove('A')
    assert d.get_remove_status() == Dictionary.REMOVE_STATUS_OK
    assert not d.is_key('A')
    assert d.get('A') is None
    assert d.get_get_status() == Dictionary.GET_STATUS_ERR

def test_many_values():
    d = Dictionary(3)
    for i in range(10):
        d.put(str(i), 'value' + str(i))
    for i in range(10):
        assert d.get(str(i)) == 'value' + str(i)
