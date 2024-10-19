"""Unit Test Examples"""

from Lessons.unit_tests.list_fns import get_first, remove_first, get_and_remove_first


def test_get_first() -> None:
    """get first should return first element"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert get_first(dog_breeds) == "husky"  # RV should be husky


# desired return value
def test_remove_first_return_value() -> None:
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    assert remove_first(dog_breeds) is None


# desired behavior
def test_remove_first_behavior() -> None:
    """remove first should remove the first elem from input list"""
    dog_breeds: list[str] = ["husky", "golden", "poodle", "lab"]
    remove_first(dog_breeds)
    assert dog_breeds == ["golden", "poodle", "lab"]


def test_get_first_edge_case() -> None:
    """get_first called on empy list should return empty string"""
    assert get_first([]) == ""
