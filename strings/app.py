from src.infrastructure.text_reader import TextReader
from src.services.text_formater import TextFormater

if __name__ == '__main__':
    length = 40
    justified = False
    text_formater = TextFormater()

    text = TextReader.read("input.txt")

    formated_text = text_formater.format(text=text, length=length, justified=justified)

    print(formated_text)
