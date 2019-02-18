from src.helpers.split_helper import SplitHelper


def test_split_should_not_consume_delimiters():
    original_text = "In the beginning God..."
    right_list = ["In ", "the ", "beginning ", "God..."]

    list = SplitHelper.split_with_delimiter(original_text, " ")

    assert list is not None
    assert list == right_list
