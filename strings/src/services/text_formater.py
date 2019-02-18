from src.domain.TextFormater import TextFormater as ITextFormater
from src.helpers.list_string_helper import ListStringHelper
from src.helpers.newline_format_helper import NewlineFormatHelper


class TextFormater(ITextFormater):

    def format(self, text: str, length: int, justified: bool):
        text = NewlineFormatHelper.add_newline_place_holder(text=text, length=length)

        text_list = ListStringHelper.string_to_formated_list(text=text, length=length)

        formated_text_with_place_holder = ListStringHelper.list_to_string(text_list=text_list)

        formated_text = NewlineFormatHelper.rm_newline_place_holder(text=formated_text_with_place_holder, length=length)

        if not justified:
            return formated_text
        elif self._successor is not None:
            return self._successor.format(text=formated_text, length=length, justified=justified)
