from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        test_dbase = Database()
        test_dbase.buns = ['red_bun', 100]
        assert test_dbase.available_buns() == ['red_bun', 100]

    def test_available_ingredients(self):
        test_dbase = Database()
        test_dbase.ingredients = ['SAUCE', "hot sauce", 100]
        assert test_dbase.available_ingredients() == ['SAUCE', "hot sauce", 100]