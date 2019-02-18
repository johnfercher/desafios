from src.domain.TextFormater import TextFormater as ITextFormater
from src.services.list_string_helper import ListStringHelper
import re


class TextFormaterWithJustified(ITextFormater):

    def format(self, text: str, length: int, justified: bool):
        text_list = text.split("\n")

        justified_text_list = [self.__justify(text, length) for text in text_list]

        text = ListStringHelper.list_to_string(justified_text_list)

        return text

    def __justify(self, text: str, length: int):
        min_spaces_to_add = self.__get_min_spaces_to_add(text, length)

        text = text.replace(" ", " " + " " * min_spaces_to_add)

        if self.__have_to_add_spaces(text, length):
            text = self.__add_missing_spaces(text, length)

        return text

    def __get_min_spaces_to_add(self, text: str, length: int):
        spaces_to_add = self.__get_qtd_spaces_to_add(text, length)
        original_spaces_qtd = self.__get_qtd_spaces_in_text(text)

        if original_spaces_qtd == 0:
            return 0

        return int(spaces_to_add / original_spaces_qtd)

    def __get_qtd_spaces_to_add(self, text: str, length: int):
        return length - len(text)

    def __get_qtd_spaces_in_text(self, text: str):
        # agrupa todos os espaços com caracter repetido
        return len(re.findall("\s+", text))

    def __have_to_add_spaces(self, text: str, length: int):
        spaces_to_add = self.__get_qtd_spaces_to_add(text, length)

        return spaces_to_add > 0

    def __add_missing_spaces(self, text: str, length: int):
        spaces_to_add = self.__get_qtd_spaces_to_add(text, length)
        space_size = self.__get_space_size(text)
        spaces_added = 0

        try:
            text_list = self.__split_with_delimiter(text, " "*space_size)

            for i in range(0, len(text_list)):
                if text_list[i][-1] == " ":
                    text_list[i] = text_list[i] + " "
                    spaces_added = spaces_added + 1

                if spaces_added >= spaces_to_add:
                    break

            text = "".join(text_list)

        except:
            return text

        return text

    def __get_space_size(self, text: str):
        spaces = re.findall("\s+", text)

        if len(spaces) > 0:
            return len(spaces[0])

        return 0

    def __split_with_delimiter(self, text: str, delimiter: str):
        return [e + delimiter for e in text.split(delimiter) if e]
