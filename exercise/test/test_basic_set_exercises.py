import unittest

class BasicSetExercisesTest(unittest.TestCase):
    def test_positive_one(self):
        self.assertEqual(3,4)

    def test_positive_two(self):
        self.assertTrue("PYthon".isupper)


if __name__ == '__main__':
    unittest.main()