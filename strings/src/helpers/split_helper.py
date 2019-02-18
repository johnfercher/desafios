class SplitHelper(object):

    @classmethod
    def split_with_delimiter(self, text: str, delimiter: str):
        elements = [e + delimiter for e in text.split(delimiter) if e]

        # remove o ultimo espaço
        elements[-1] = elements[-1][0:-1]

        return elements
