from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    cheese = Ingredient("queijo mussarela")
    assert cheese.name == "queijo mussarela"
    assert cheese.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    cheese_hash = Ingredient("queijo mussarela").__hash__()
    assert cheese_hash == hash("queijo mussarela")

    cheese_eq = Ingredient("queijo mussarela").__eq__(cheese)
    assert cheese_eq

    cheese_repr = Ingredient("queijo mussarela").__repr__()
    assert cheese_repr == "Ingredient('queijo mussarela')"
