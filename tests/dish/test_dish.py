from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    ingredient = Ingredient("queijo mussarela")
    dish = Dish("Lasanha Presunto", 25.90)
    assert dish.name == "Lasanha Presunto"
    assert dish.recipe == {}

    dish.add_ingredient_dependency(ingredient, 1)
    assert dish.recipe == {ingredient: 1}
    assert dish.get_ingredients() == {ingredient}

    assert dish.__eq__(dish)

    assert dish.__hash__() == hash("Dish('Lasanha Presunto', R$25.90)")

    assert dish.get_restrictions() == ingredient.restrictions

    with pytest.raises(TypeError):
        Dish("Lasanha Presunto", "25.90")

    with pytest.raises(ValueError):
        Dish("Lasanha Presunto", -25.90)
