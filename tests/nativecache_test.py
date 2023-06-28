import unittest
from nativecache import NativeCache


class TestNativeCache(unittest.TestCase):

    def setUp(self):
        self.nc = NativeCache(17)

    def test_hash_fun(self):
        self.assertEqual(self.nc.hash_fun('a'), 12, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('aa'), 7, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun(''), 0, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun(' '), 15, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('  '), 13, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('\t'), 9, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('g'), 1, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('bk'), 1, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('al'), 1, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('0'), 14, 'hash_fun is not correct')
        self.assertEqual(self.nc.hash_fun('1'), 15, 'hash_fun is not correct')

    def test_put(self):
        self.nc.put('a', 1)
        self.assertEqual(
            self.nc.values[self.nc.hash_fun('a')], 1, 'put is not correct')
        self.assertEqual(
            self.nc.slots[self.nc.hash_fun('a')], 'a', 'put is not correct')
        self.nc.put('a', 2)
        self.assertEqual(
            self.nc.values[self.nc.hash_fun('a')], 2, 'put is not correct')
        self.assertEqual(
            self.nc.slots[self.nc.hash_fun('a')], 'a', 'put is not correct')

    def test_get(self):
        self.assertIsNone(self.nc.get('a'), 'get is not correct')
        self.nc.put('a', 1)
        self.assertEqual(self.nc.get('a'), 1, 'get is not correct')
        self.nc.put('a', 2)
        self.assertEqual(self.nc.get('a'), 2, 'get is not correct')

    def test_is_key(self):
        self.assertFalse(self.nc.is_key('a'), 'is_key is not correct')
        self.assertFalse(self.nc.is_key('b'), 'is_key is not correct')
        self.nc.put('a', 1)
        self.assertTrue(self.nc.is_key('a'), 'is_key is not correct')
        self.assertFalse(self.nc.is_key('b'), 'is_key is not correct')
        self.nc.put('a', 2)
        self.assertTrue(self.nc.is_key('a'), 'is_key is not correct')
        self.assertFalse(self.nc.is_key('b'), 'is_key is not correct')

    def test_displacement(self):
        for i in range(17):
            self.assertEqual(self.nc.hits[i], 0, 'must be zero')
        for i in range(17):
            self.nc.put(str(i), i*10)
        for i in range(17):
            self.assertEqual(self.nc.hits[i], 0, 'must be zero')
        for i in range(2, 17):
            self.nc.get(str(i))
        for i in range(14):
            self.assertEqual(self.nc.hits[i], 1, 'must be 1')
        self.assertEqual(self.nc.hits[14], 0, 'must be zero')
        self.assertEqual(self.nc.hits[15], 0, 'must be zero')
        self.assertEqual(self.nc.hits[16], 1, 'must be 1')
        self.assertEqual(self.nc.slots[15], '1', 'must be 1')
        self.nc.put('al', 'alal')
        self.assertEqual(self.nc.values[14], 'alal', 'must be alal')
        self.assertEqual(self.nc.slots[14], 'al', 'must be al')
        self.assertFalse(self.nc.is_key('0'), 'must be false')
        self.assertTrue(self.nc.is_key('al'), 'must be true')
        self.nc.put('0', '11111')
        self.assertTrue(self.nc.is_key('0'), 'must be true')
        self.assertEqual(self.nc.values[15], '11111', 'must be 11111')
        self.assertEqual(self.nc.slots[15], '0', 'must be 0')
        self.assertFalse(self.nc.is_key('1'), 'must be false')
        for i in range(17):
            self.assertEqual(self.nc.hits[i], 1, 'must be zero')


if __name__ == '__main__':
    unittest.main()
