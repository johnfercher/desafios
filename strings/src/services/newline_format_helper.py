class NewlineFormatHelper(object):

    @classmethod
    def add_newline_place_holder(cls, text: str, length: int):
        return text.replace("\n\n", "\n"+"*"*length+"\n")

    @classmethod
    def rm_newline_place_holder(cls, text: str, length: int):
        return text.replace("\n" + "*" * length + "\n", "\n\n")
