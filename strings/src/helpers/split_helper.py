class SplitHelper(object):

    @classmethod
    def split_with_delimiter(cls, text: str, delimiter: str, qtd: int):
        elements = [e + delimiter*qtd for e in text.split(delimiter*qtd) if e]

        # remove o ultimo espaço
        elements[-1] = elements[-1][0:-qtd]

        return elements
