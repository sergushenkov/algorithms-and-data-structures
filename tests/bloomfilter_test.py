import unittest
from bloomfilter import BloomFilter


class TestBloomFilter(unittest.TestCase):

    def setUp(self):
        self.bf = BloomFilter(32)

    def test_add(self):
        nums = ["0123456789", "1234567890", "2345678901", "3456789012", "4567890123",
                "5678901234", "6789012345", "7890123456", "8901234567" "9012345678"]
        for num in nums:
            self.bf.add(num)
            self.assertTrue(self.bf.is_value(num))
        for num in nums:
            self.assertTrue(self.bf.is_value(num))    


if __name__ == '__main__':
    unittest.main()
