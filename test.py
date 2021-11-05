from main import sockmerchant
import unittest

class Test(unittest.TestCase):
    def test1(self):
        ar = [2,4,6,8,10,12,14,16,18,20,2,4,6,8,10,12,14,16,18,20,2,4,6,8,10,12,14,16,18,20]
        n = 30
        self.assertEqual(sockmerchant(n, ar), 10)

    def test2(self):
        ar = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
              3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
              4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,
              7,8,9,10,11,12,13,14]
        n = 80
        self.assertEqual(sockmerchant(n, ar), 36)

if __name__ == '__main__':
    unittest.main()