import unittest
from zad3 import isprime

class TestMyModule(unittest.TestCase):

    def test(self):
        self.assertEqual(isprime(13), True)
        self.assertEqual(isprime(19), True)
        self.assertEqual(isprime(27), False)
        


if __name__ == '__main__':
    unittest.main()
  
