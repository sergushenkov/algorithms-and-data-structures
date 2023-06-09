import unittest
from dynarray import DynArray


class TestFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.dyn_arr = DynArray()

    def test_insert(self):
        self.assertRaises(IndexError, self.dyn_arr.insert, -1, 20)
        self.assertRaises(IndexError, self.dyn_arr.insert, 1, 20)
        self.dyn_arr.insert(0, 20)
        self.assertEqual(self.dyn_arr.count, 1)
        self.assertEqual(self.dyn_arr.capacity, 16)
        self.assertEqual(self.dyn_arr[0], 20)
        self.dyn_arr.insert(0, 10)
        self.assertEqual(self.dyn_arr.count, 2)
        self.assertEqual(self.dyn_arr.capacity, 16)
        self.assertEqual(self.dyn_arr[0], 10)
        self.assertEqual(self.dyn_arr[1], 20)
        self.assertRaises(IndexError, self.dyn_arr.insert, 3, 30)
        self.dyn_arr.insert(2, 30)
        self.assertEqual(self.dyn_arr.count, 3)
        self.assertEqual(self.dyn_arr.capacity, 16)
        self.assertEqual(self.dyn_arr[0], 10)
        self.assertEqual(self.dyn_arr[1], 20)
        self.assertEqual(self.dyn_arr[2], 30)
        for i in range(50, 180, 10):
            self.dyn_arr.append(i)
        self.assertEqual(self.dyn_arr.count, 16)
        self.assertEqual(self.dyn_arr.capacity, 16)
        self.dyn_arr.insert(3, 40)
        self.assertEqual(self.dyn_arr.count, 17)
        self.assertEqual(self.dyn_arr.capacity, 32)
        for i in range(180, 330, 10):
            self.dyn_arr.append(i)
        self.assertEqual(self.dyn_arr.count, 32)
        self.assertEqual(self.dyn_arr.capacity, 32)
        self.dyn_arr.insert(32, 330)
        self.assertEqual(self.dyn_arr.count, 33)
        self.assertEqual(self.dyn_arr.capacity, 64)
        for i in range(33):
            self.assertEqual(self.dyn_arr[i], (i + 1)*10)

    def test_delete(self):
        self.assertRaises(IndexError, self.dyn_arr.delete, 0)
        self.dyn_arr.append(0)
        self.dyn_arr.append(1)
        self.assertRaises(IndexError, self.dyn_arr.delete, -1)
        self.assertRaises(IndexError, self.dyn_arr.delete, 2)
        self.dyn_arr.delete(0)
        self.assertEqual(self.dyn_arr.count, 1)
        self.assertEqual(self.dyn_arr.capacity, 16)
        self.assertEqual(self.dyn_arr[0], 1)
        self.dyn_arr.delete(0)
        self.assertEqual(self.dyn_arr.count, 0)
        self.assertEqual(self.dyn_arr.capacity, 16)
        self.assertRaises(IndexError, self.dyn_arr.__getitem__, 0)

        for i in range(18):
            self.dyn_arr.append(i)
        self.dyn_arr.delete(1)
        self.assertEqual(self.dyn_arr.count, 17)
        self.assertEqual(self.dyn_arr.capacity, 32)
        self.dyn_arr.delete(2)
        self.assertEqual(self.dyn_arr.count, 16)
        self.assertEqual(self.dyn_arr.capacity, 32)
        cnt = 16
        for i in range(3, 8):
            self.dyn_arr.delete(i)
            cnt -= 1
            self.assertEqual(self.dyn_arr.count, cnt)
            self.assertEqual(self.dyn_arr.capacity, 21)
        self.dyn_arr.delete(8)
        self.assertEqual(self.dyn_arr.count, 10)
        self.assertEqual(self.dyn_arr.capacity, 16)
        for i in range(9):
            self.assertEqual(self.dyn_arr[i], 2 * i)
        self.assertEqual(self.dyn_arr[9], 17)
        for i in range(10):
            self.dyn_arr.delete(0)
            self.assertEqual(self.dyn_arr.count, 9 - i)
            self.assertEqual(self.dyn_arr.capacity, 16)
        self.assertRaises(IndexError, self.dyn_arr.__getitem__, 0)

    def test_delete_with_resize(self):
        for i in range(129):
            self.dyn_arr.append(i)
        self.assertEqual(self.dyn_arr.count, 129)
        self.assertEqual(self.dyn_arr.capacity, 256)
        cnt = 129
        cpct = 256
        for i in range(128, -1, -1):
            self.dyn_arr.delete(i)
            cnt -= 1
            if 24 <= cpct and cnt < cpct / 2:
                cpct = max(16, cpct // 1.5)
                self.assertEqual(self.dyn_arr.count, cnt)
                self.assertEqual(self.dyn_arr.capacity, cpct)
        self.assertRaises(IndexError, self.dyn_arr.__getitem__, 0)

        for i in range(129):
            self.dyn_arr.append(i)
        self.assertEqual(self.dyn_arr.count, 129)
        self.assertEqual(self.dyn_arr.capacity, 256)
        cnt = 129
        cpct = 256
        for i in range(129):
            self.dyn_arr.delete(0)
            cnt -= 1
            if 24 <= cpct and cnt < cpct / 2:
                cpct = max(16, cpct // 1.5)
                self.assertEqual(self.dyn_arr.count, cnt)
                self.assertEqual(self.dyn_arr.capacity, cpct)
        self.assertRaises(IndexError, self.dyn_arr.__getitem__, 0)


if __name__ == '__main__':
    unittest.main()
