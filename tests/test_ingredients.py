from ingredient import Ingredient


class TestIngredients:
    def test_get_price(self):
        test_ingredient = Ingredient('meat','saturn_meat', 100)
        assert test_ingredient.get_price() == 100

    def test_get_name(self):
        test_ingredient = Ingredient('meat','saturn_meat', 100)
        assert test_ingredient.get_name() == "saturn_meat"

    def test_get_type(self):
        test_ingredient = Ingredient('meat','saturn_meat', 100)
        assert test_ingredient.get_type() == 'meat'