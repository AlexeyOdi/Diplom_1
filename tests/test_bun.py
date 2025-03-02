from bun import Bun

class TestBun:

    def test_get_name(self):
        bun = Bun('brioche', 100)
        assert bun.get_name() == 'brioche'

    def test_get_price(self):
        bun = Bun('brioche', 100)
        assert bun.get_price() == 100