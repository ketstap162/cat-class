import pytest

from app import Cat

PARAMETERS = [
    "name,age",
    [
        pytest.param(
            "Jonny",
            "3",
            id="Cat with name Jonny and age 3"
        ),
        pytest.param(
            "Bob",
            "1",
            id="Cat with name Bob and age 1"
        ),
        pytest.param(
            "Misha",
            "4",
            id="Cat with name Misha and age 4"
        ),
    ]
]


class TestCatClass:
    @pytest.mark.parametrize(*PARAMETERS)
    def test_create_cat(self, name, age):
        cat = Cat(name, age)

        assert cat.name == name
        assert cat.age == age

    @pytest.mark.parametrize(*PARAMETERS)
    def test_info_method(self, name, age):
        cat = Cat(name, age)

        assert cat.info() == {"cat": name, "age": age}

    @pytest.mark.parametrize(*PARAMETERS)
    def test_voice_method(self, name, age):
        cat = Cat(name, age)

        assert cat.voice() == f"{name}: Meow!"
