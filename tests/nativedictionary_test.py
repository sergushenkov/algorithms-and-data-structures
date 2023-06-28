import unittest
from nativedictionary import NativeDictionary


class TestNativeDictionary(unittest.TestCase):

    def setUp(self):
        self.nd = NativeDictionary(17)

    def test_hash_fun(self):
        self.assertEqual(self.nd.hash_fun('a'), 12, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun('aa'), 7, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun(''), 0, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun(' '), 15, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun('  '), 13, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun('\t'), 9, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun('g'), 1, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun('bk'), 1, 'hash_fun is not correct')
        self.assertEqual(self.nd.hash_fun('al'), 1, 'hash_fun is not correct')

    def test_put(self):
        self.nd.put('a', 1)
        self.assertEqual(
            self.nd.values[self.nd.hash_fun('a')], 1, 'put is not correct')
        self.assertEqual(
            self.nd.slots[self.nd.hash_fun('a')], 'a', 'put is not correct')
        self.nd.put('a', 2)
        self.assertEqual(
            self.nd.values[self.nd.hash_fun('a')], 2, 'put is not correct')
        self.assertEqual(
            self.nd.slots[self.nd.hash_fun('a')], 'a', 'put is not correct')

    def test_get(self):
        self.assertIsNone(self.nd.get('a'), 'get is not correct')
        self.nd.put('a', 1)
        self.assertEqual(self.nd.get('a'), 1, 'get is not correct')
        self.nd.put('a', 2)
        self.assertEqual(self.nd.get('a'), 2, 'get is not correct')

    def test_is_key(self):
        self.assertFalse(self.nd.is_key('a'), 'is_key is not correct')
        self.assertFalse(self.nd.is_key('b'), 'is_key is not correct')
        self.nd.put('a', 1)
        self.assertTrue(self.nd.is_key('a'), 'is_key is not correct')
        self.assertFalse(self.nd.is_key('b'), 'is_key is not correct')
        self.nd.put('a', 2)
        self.assertTrue(self.nd.is_key('a'), 'is_key is not correct')
        self.assertFalse(self.nd.is_key('b'), 'is_key is not correct')


if __name__ == '__main__':
    unittest.main()
