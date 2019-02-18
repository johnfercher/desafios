from textwrap import wrap


class ListStringHelper(object):

    @classmethod
    def list_to_string(cls, text_list: list):
        return "\n".join(text_list)

    @classmethod
    def string_to_formated_list(cls, text: str, length: int):
        return wrap(text, length)
