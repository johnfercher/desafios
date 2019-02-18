from textwrap import wrap
from src.domain.formated_text import FormatedText


class TextFormater(object):

    def format(self, text: str, length: int):
        formated_text = FormatedText()

        lines = wrap(text, length)

        formated_text.extend(lines)

        for text in formated_text:
            print(text)

        return text
