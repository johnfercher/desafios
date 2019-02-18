from src.services.newline_format_helper import NewlineFormatHelper


def test_add_newline_place_holder_should_replace_double_n_with_place_holder():
    # Arrange
    original_text = "In the beginning God created the heavens and the earth.\nNow the earth was formless and empty,\n\n" \
           "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters."

    final_text = "In the beginning God created the heavens and the earth.\nNow the earth was formless and empty," \
                 "\n**********\ndarkness was over the surface of the deep, and the Spirit of God was hovering over " \
                 "the waters."

    new_text = NewlineFormatHelper.add_newline_place_holder(original_text, 10)

    assert new_text is not None
    assert new_text == final_text


def test_rm_newline_place_holder_should_replace_place_holder_with_double_n():
    # Arrange
    original_text = "In the beginning God created the heavens and the earth.\nNow the earth was formless and empty," \
                    "\n**********\ndarkness was over the surface of the deep, and the Spirit of God was hovering over " \
                    "the waters."

    final_text = "In the beginning God created the heavens and the earth.\nNow the earth was formless and empty," \
                 "\n\ndarkness was over the surface of the deep, and the Spirit of God was hovering over the waters."

    new_text = NewlineFormatHelper.rm_newline_place_holder(original_text, 10)

    assert new_text is not None
    assert new_text == final_text
