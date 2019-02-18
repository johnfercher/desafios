from src.services.list_string_helper import ListStringHelper
from src.services.newline_format_helper import NewlineFormatHelper


class TextFormater(object):

    def format(self, text: str, length: int, justified: bool):
        text = NewlineFormatHelper.add_newline_place_holder(text=text, length=length)

        text_list = ListStringHelper.string_to_formated_list(text=text, length=length)

        formated_text = ListStringHelper.list_to_string(text_list=text_list)

        return NewlineFormatHelper.rm_newline_place_holder(text=formated_text, length=length)
