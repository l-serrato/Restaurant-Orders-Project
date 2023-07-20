from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient('onion', 1, 'cup')
    assert ingredient.name == 'onion'
    assert ingredient.quantity == 1
    assert ingredient.unit == 'cup'
