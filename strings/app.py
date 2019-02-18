from src.infrastructure.text_reader import TextReader
from src.services.text_formater import TextFormater
from src.services.text_formater_with_justified import TextFormaterWithJustified


def main():
    length = 40
    justified = True
    text_formater = TextFormater(TextFormaterWithJustified())

    text = TextReader.read("input.txt")

    formated_text = text_formater.format(text=text, length=length, justified=justified)

    print(formated_text)


if __name__ == '__main__':
    main()

