from login import login

import unittest


def add_numbers(a, b):
  return a + b

class testModule(unittest.TestCase):
  def test_add_numbers(self):
    self.assertEqual(add_numbers(2, 5), 7)
    self.assertEqual(add_numbers(1, -1), 0)
    self.assertEqual(add_numbers(2, 2), 4)

def test_login(self):
  self.assertEqual(login(), 2)


if __name__ == '__main__':
  unittest.main()
