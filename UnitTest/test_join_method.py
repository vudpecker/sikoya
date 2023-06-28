import unittest

class TestJoinMethod(unittest.TestCase):
    def test_join_with_space(self):
        self.assertEqual(' '.join(["Python", "3.8"]), "Python 3.8")


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOOd',"It is not upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()