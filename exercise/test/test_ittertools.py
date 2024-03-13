

class TestIttertools():
    def test_type(self):
        assert type(1.1) == float

    def test_mod(self):
        assert 1 in divmod(9,5)