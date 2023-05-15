import unittest
from powerset import PowerSet


class TestPowerSet(unittest.TestCase):
    def setUp(self) -> None:
        self.ps = PowerSet()

    def test_size(self):
        for i in range(10):
            self.assertEqual(self.ps.size(), i)
            self.ps.put(str(i))
        self.assertEqual(self.ps.size(), 10)

    def test_put(self):
        self.ps.put("a")
        self.ps.put("a")
        self.assertEqual(self.ps.size(), 1)

    def test_get(self):
        self.assertFalse(self.ps.get("a"), "a is not in the set")
        self.ps.put("a")
        self.assertTrue(self.ps.get("a"), "a is in the set")
        self.assertFalse(self.ps.get("b"), "b is not in the set")

    def test_remove(self):
        self.assertFalse(self.ps.remove("a"), "a is not in the set")
        self.ps.put("a")
        self.assertTrue(self.ps.remove("a"), "a is in the set")
        self.assertFalse(self.ps.remove("a"), "a is not in the set")

    def test_intersection(self):
        self.ps2 = PowerSet()
        result = self.ps.intersection(self.ps2)
        self.assertEqual(result.size(), 0)
        self.ps.put("a")
        result = self.ps.intersection(self.ps2)
        self.assertEqual(result.size(), 0)
        self.assertFalse(result.get("a"), "a is not in the set")
        self.ps2.put("a")
        result = self.ps.intersection(self.ps2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get("a"), "a is in the set")
        self.ps2.put("b")
        result = self.ps.intersection(self.ps2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get("a"), "a is in the set")
        self.assertFalse(result.get("b"), "b is not in the set")

    def test_union(self):
        self.ps2 = PowerSet()
        result = self.ps.union(self.ps2)
        self.assertEqual(result.size(), 0)
        self.ps.put("a")
        result = self.ps.union(self.ps2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get("a"), "a is in the set")
        self.ps2.put("a")
        result = self.ps.union(self.ps2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get("a"), "a is in the set")
        self.ps2.put("b")
        result = self.ps.union(self.ps2)
        self.assertEqual(result.size(), 2)
        self.assertTrue(result.get("a"), "a is in the set")
        self.assertTrue(result.get("b"), "b is in the set")

    def test_difference(self):
        self.ps2 = PowerSet()
        result = self.ps.difference(self.ps2)
        self.assertEqual(result.size(), 0)
        self.ps.put("a")
        result = self.ps.difference(self.ps2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(result.get("a"), "a is in the set")
        self.ps2.put("a")
        result = self.ps.difference(self.ps2)
        self.assertEqual(result.size(), 0)
        self.assertFalse(result.get("a"), "a is not in the set")
        self.ps.put("b")
        result = self.ps.difference(self.ps2)
        self.assertEqual(result.size(), 1)
        self.assertFalse(result.get("a"), "a is not in the set")
        self.assertTrue(result.get("b"), "b is in the set")

    def test_issubset(self):
        self.ps2 = PowerSet()
        self.assertTrue(self.ps.issubset(self.ps2), "a is in the set")
        self.assertTrue(self.ps2.issubset(self.ps), "a is in the set")
        self.ps.put("a")
        self.assertTrue(self.ps.issubset(self.ps2), "a is in the set")
        self.assertFalse(self.ps2.issubset(self.ps), "a is not in the set")
        self.ps2.put("a")
        self.assertTrue(self.ps.issubset(self.ps2), "a is in the set")
        self.assertTrue(self.ps2.issubset(self.ps), "a is in the set")
        self.ps.put("b")
        self.assertTrue(self.ps.issubset(self.ps2), "a is in the set")
        self.assertFalse(self.ps2.issubset(self.ps), "a is not in the set")


if __name__ == '__main__':
    unittest.main()
