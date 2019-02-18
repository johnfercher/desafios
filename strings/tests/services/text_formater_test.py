from src.services.text_formater import TextFormater
from src.services.text_formater_with_justified import TextFormaterWithJustified


def test_format_should_not_have_text_with_length_greater_than_specified_when_not_justified():
    original_text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " \
                    "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. " \
                    "\n\nAnd God said, \"Let there be light,\" and there was light. God saw that the light was good, " \
                    "and he separated the light from the darkness. God called the light \"day,\" and the darkness he " \
                    "called \"night.\" And there was evening, and there was morning - the first day. "

    formated_text = "In the beginning God created the heavens\n" \
                    "and the earth. Now the earth was\n" \
                    "formless and empty, darkness was over\n" \
                    "the surface of the deep, and the Spirit\n" \
                    "of God was hovering over the waters.\n" \
                    "\n" \
                    "And God said, \"Let there be light,\" and\n" \
                    "there was light. God saw that the light\n" \
                    "was good, and he separated the light\n" \
                    "from the darkness. God called the light\n" \
                    "\"day,\" and the darkness he called\n" \
                    "\"night.\" And there was evening, and\n" \
                    "there was morning - the first day."

    length = 40
    justified = False

    text_formater = TextFormater(TextFormaterWithJustified())

    result_text = text_formater.format(original_text, length, justified)

    assert result_text is not None
    assert result_text == formated_text


def test_format_should_only_have_text_with_exactly_same_length_than_specified_when_justified():
    original_text = "In the beginning God created the heavens and the earth. Now the earth was formless and empty, " \
                    "darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. " \
                    "\n\nAnd God said, \"Let there be light,\" and there was light. God saw that the light was good, " \
                    "and he separated the light from the darkness. God called the light \"day,\" and the darkness he " \
                    "called \"night.\" And there was evening, and there was morning - the first day. "

    formated_text = "In the beginning God created the heavens\n" \
                    "and   the   earth.  Now  the  earth  was\n" \
                    "formless  and  empty,  darkness was over\n" \
                    "the  surface of the deep, and the Spirit\n" \
                    "of  God  was  hovering  over the waters.\n" \
                    "\n" \
                    "And  God said, \"Let there be light,\" and\n" \
                    "there  was light. God saw that the light\n" \
                    "was  good,  and  he  separated the light\n" \
                    "from  the darkness. God called the light\n" \
                    "\"day,\"   and   the  darkness  he  called\n" \
                    "\"night.\"  And  there  was  evening,  and\n" \
                    "there  was  morning  -  the  first  day."

    length = 40
    justified = True

    text_formater = TextFormater(TextFormaterWithJustified())

    result_text = text_formater.format(original_text, length, justified)

    assert result_text is not None
    assert result_text == formated_text
