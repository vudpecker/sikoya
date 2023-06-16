
import unittest

class TestCaseCollections(unittest.TestCase):

    def test_append_string(self):
        stringlonly = StringListOnly()
        stringlonly.append("Two")
        self.assertIn("Two", stringlonly)
        
    def test_append_not_string_should_raise_error(self):
        stringlonly = StringListOnly()
        with self.assertRaises(TypeError):
            stringlonly.append(["Two"])
        with self.assertRaises(TypeError):
            stringlonly.append(None)