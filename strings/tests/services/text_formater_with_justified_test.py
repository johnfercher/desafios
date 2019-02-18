from src.services.text_formater_with_justified import TextFormaterWithJustified


def test_format_should_justify_text():
    original_text = "In the beginning God created the heavens\n" \
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

    text_formater = TextFormaterWithJustified()

    result_text = text_formater.format(original_text, length, justified)

    assert result_text is not None
    assert result_text == formated_text
