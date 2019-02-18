from src.infrastructure.reader_helper import ReaderHelper
from src.services.text_formater import TextFormater

if __name__ == '__main__':
    max_length = 40
    text_formater = TextFormater()

    content = ReaderHelper.read("input.txt")
    formated_content = text_formater.format(content, max_length)

    print(content)
    print(formated_content)
