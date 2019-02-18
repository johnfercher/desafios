from src.helpers.space_justify_helper import SpaceJustifyHelper


def test_get_qtd_spaces_to_add_should_return_difference_between_string_length_and_length():
    original_text = "In the beginning God..."

    qtd = SpaceJustifyHelper.get_qtd_spaces_to_add(original_text, 30)

    assert qtd is not None
    assert qtd == 7


def test_get_qtd_spaces_in_text_should_return_number_of_spaces_with_single_space():
    original_text = "In the beginning God..."

    qtd = SpaceJustifyHelper.get_qtd_spaces_in_text(original_text)

    assert qtd is not None
    assert qtd == 3


def test_get_qtd_spaces_in_text_should_return_number_of_spaces_with_double_space():
    original_text = "In  the  beginning  God..."

    qtd = SpaceJustifyHelper.get_qtd_spaces_in_text(original_text)

    assert qtd is not None
    assert qtd == 3


def test_get_qtd_spaces_in_text_should_return_number_of_spaces_with_any_qtd_of_spaces():
    original_text = "In the  beginning    God..."

    qtd = SpaceJustifyHelper.get_qtd_spaces_in_text(original_text)

    assert qtd is not None
    assert qtd == 3


def test_get_min_spaces_to_add_should_return_the_qtd_of_spaces_to_append_in_any_space():
    original_text = "In the beginning God..."

    qtd = SpaceJustifyHelper.get_min_spaces_to_add(original_text, 30)

    assert qtd is not None
    assert qtd is 2


def test_have_to_add_spaces_should_return_true_if_string_len_is_not_length():
    original_text = "In the beginning God..."

    have_to_add = SpaceJustifyHelper.have_to_add_spaces(original_text, 23)

    assert have_to_add is not None
    assert have_to_add is False


def test_have_to_add_spaces_should_return_false_if_string_len_is_not_length():
    original_text = "In the beginning God..."

    have_to_add = SpaceJustifyHelper.have_to_add_spaces(original_text, 24)

    assert have_to_add is not None
    assert have_to_add is True


def test_get_space_size_should_return_to_number_of_spaces_size_by_size():
    original_text = "In  the  beginning  God..."

    qtd = SpaceJustifyHelper.get_space_size(original_text)

    assert qtd is not None
    assert qtd == 2
