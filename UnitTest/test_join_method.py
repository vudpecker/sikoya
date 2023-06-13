import unittest


class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):
        self.assertEqual(' '.join(["Python", "3.8"]), "Python 3.8")


if __name__ == '__main__':
    unittest.main()