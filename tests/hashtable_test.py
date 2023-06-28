import unittest
from hashtable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable(17, 3)

    def test_hash_fun(self):
        self.assertEqual(self.ht.hash_fun('a'), 12, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun('aa'), 7, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun(''), 0, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun(' '), 15, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun('  '), 13, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun('\t'), 9, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun('g'), 1, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun('x'), 1, 'hash_fun is not correct')
        self.assertEqual(self.ht.hash_fun('al'), 1, 'hash_fun is not correct')

    def test_seek_slot(self):
        cnt = 1
        for ch in ['al', 'bk', 'cj', 'di', 'dz', 'eh', 'ey', 'fg', 'fx', 'gf',
                   'gw', 'he', 'hv', 'id', 'iu', 'jc', 'jt']:
            i = self.ht.seek_slot(ch)
            self.assertEqual(i, cnt, 'seek_slot is not correct')
            if i is not None:
                self.ht.slots[i] = ch
            cnt = (cnt + 3) % 17
        self.assertIsNone(self.ht.seek_slot('a'), 'seek_slot is not correct')

    def test_put(self):
        cnt = 1
        for ch in ['al', 'bk', 'cj', 'di', 'dz', 'eh', 'ey', 'fg', 'fx', 'gf',
                   'gw', 'he', 'hv', 'id', 'iu', 'jc', 'jt']:
            i = self.ht.put(ch)
            self.assertEqual(i, cnt, 'put is not correct')
            cnt = (cnt + 3) % 17
        self.assertIsNone(self.ht.put('a'), 'seek_slot is not correct')

    def test_find(self):
        for ch in ['al', 'bk', 'cj', 'di', 'dz', 'eh', 'ey', 'fg', 'fx', 'gf',
                   'gw', 'he', 'hv', 'id', 'iu', 'jc', 'jt']:
            self.assertIsNone(self.ht.find(ch), 'should be none')
            i = self.ht.put(ch)
            self.assertEqual(self.ht.find(ch), i, 'put is not correct')
        self.assertIsNone(self.ht.put('a'), 'seek_slot is not correct')


if __name__ == '__main__':
    unittest.main()
