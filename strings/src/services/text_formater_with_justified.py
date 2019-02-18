from src.domain.services.TextFormater import TextFormater as ITextFormater
from src.helpers.list_string_helper import ListStringHelper
from src.helpers.space_justify_helper import SpaceJustifyHelper
from src.helpers.split_helper import SplitHelper


class TextFormaterWithJustified(ITextFormater):

    def format(self, text: str, length: int, justify: bool):
        text_list = text.split("\n")

        justified_text_list = [self.__justify(text, length) for text in text_list]

        text = ListStringHelper.list_to_string(justified_text_list)

        return text

    def __justify(self, text: str, length: int):
        min_spaces_to_add = SpaceJustifyHelper.get_min_spaces_to_add(text, length)

        # Add all spaces with same size
        text = text.replace(" ", " " + " " * min_spaces_to_add)

        # Add spaces to reach the correct length
        if SpaceJustifyHelper.have_to_add_spaces(text, length):
            text = self.__add_missing_spaces(text, length)

        return text

    def __add_missing_spaces(self, text: str, length: int):
        spaces_to_add = SpaceJustifyHelper.get_qtd_spaces_to_add(text, length)
        space_size = SpaceJustifyHelper.get_space_size(text)
        #print(space_size)
        #print(text)
        spaces_added = 0

        try:
            text_list = SplitHelper.split_with_delimiter(text, " ", space_size)

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
