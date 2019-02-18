from src.helpers.list_string_helper import ListStringHelper


def test_string_to_formated_list_should_limit_line_width_correctly_for_40():
    # Arrange
    text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " \
           "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. "

    # Act
    text_list = ListStringHelper.string_to_formated_list(text, 40)

    # Assert
    assert text_list is not None
    assert len(text_list) is 5

    for text in text_list:
        assert len(text) <= 40


def test_string_to_formated_list_should_limit_line_width_correctly_for_25():
    # Arrange
    text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " \
           "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. "

    # Act
    text_list = ListStringHelper.string_to_formated_list(text, 25)

    # Assert
    assert text_list is not None
    assert len(text_list) is 8

    for text in text_list:
        assert len(text) <= 25


def test_string_to_formated_list_should_limit_line_width_correctly_for_10():
    # Arrange
    text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " \
           "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. "

    # Act
    text_list = ListStringHelper.string_to_formated_list(text, 10)

    # Assert
    assert text_list is not None
    assert len(text_list) is 23

    for text in text_list:
        assert len(text) <= 10


def test_list_to_string_should_concat_list_and_append_newline():
    # Arrange
    original_text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " \
           "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. "

    final_text = "In the beginning God created the heavens\nand the earth. Now the earth was\nformless and empty, " \
                 "darkness was over\nthe surface of the deep, and the Spirit\nof God was hovering over the waters."

    text_list = ListStringHelper.string_to_formated_list(original_text, 40)

    # Act
    formated_text = ListStringHelper.list_to_string(text_list)

    # Assert
    assert formated_text is not None
    assert formated_text == final_text
