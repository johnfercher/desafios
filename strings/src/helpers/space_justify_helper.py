import re


class SpaceJustifyHelper(object):

    @classmethod
    def get_min_spaces_to_add(cls, text: str, length: int):
        spaces_to_add = cls.get_qtd_spaces_to_add(text, length)
        original_spaces_qtd = cls.get_qtd_spaces_in_text(text)

        if original_spaces_qtd == 0:
            return 0

        return int(spaces_to_add / original_spaces_qtd)

    @classmethod
    def get_qtd_spaces_to_add(cls, text: str, length: int):
        return length - len(text)

    @classmethod
    def get_qtd_spaces_in_text(cls, text: str):
        # agrupa todos os espaços com caracter repetido
        return len(re.findall("\s+", text))

    @classmethod
    def have_to_add_spaces(cls, text: str, length: int):
        spaces_to_add = cls.get_qtd_spaces_to_add(text, length)

        return spaces_to_add > 0

    @classmethod
    def get_space_size(cls, text: str):
        spaces = re.findall("\s+", text)

        if len(spaces) > 0:
            return len(spaces[0])

        return 0
