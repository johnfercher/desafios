class ReaderHelper(object):

    @classmethod
    def read(cls, filename: str):
        with open(filename, 'r') as opened_file:
            content = opened_file.read()

        return content
