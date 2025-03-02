from burger import Burger
from bun import Bun
from ingredient import Ingredient

class TestBurger:
    def test_set_bun(self):
        test_burger = Burger()
        test_bun = Bun('black_bun', 100)
        test_burger.set_buns(test_bun)
        assert test_burger.bun == test_bun

    def test_add_ingredient(self):
        test_burger = Burger()
        test_ingredient = Ingredient('sauce', 'ketchup', 100)
        test_burger.add_ingredient(test_ingredient)
        assert test_burger.ingredients == [test_ingredient]

    def test_remove_ingredient(self):
        test_burger = Burger()
        test_ingredient = Ingredient('sauce', 'ketchup', 100)
        test_burger.add_ingredient(test_ingredient)
        test_burger.remove_ingredient(0)
        assert test_burger.ingredients == []

    def test_move_ingredient(self):
        test_burger = Burger()
        test_ingredient = Ingredient('sauce', 'ketchup', 100)
        test_burger.add_ingredient(test_ingredient)
        test_ingredient_2 = Ingredient('filling', 'cutlet', 100)
        test_burger.add_ingredient(test_ingredient_2)
        test_burger.move_ingredient(0,1)
        assert test_burger.ingredients[1] == test_ingredient

    def test_get_price(self):
        test_burger = Burger()
        test_bun = Bun('black_bun', 100)
        test_burger.set_buns(test_bun)
        test_ingredient = Ingredient('sauce','ketchup', 100)
        test_burger.add_ingredient(test_ingredient)
        assert test_burger.get_price() == 300

    def test_get_receipt(self):
        test_burger = Burger()
        test_bun = Bun('black_bun', 100)
        test_burger.set_buns(test_bun)
        test_ingredient = Ingredient('sauce', 'ketchup', 100)
        test_burger.add_ingredient(test_ingredient)
        assert test_burger.get_receipt() == '(==== black_bun ====)\n= sauce ketchup =\n(==== black_bun ====)\n\nPrice: 300'


