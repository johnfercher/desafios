from src.infrastructure.text_reader import TextReader
from src.services.text_formater import TextFormater
from src.services.text_formater_with_justified import TextFormaterWithJustified
import argparse


def main():
    args = get_inputs()

    input = args.file
    length = args.length
    justify = args.justify

    text_formater = TextFormater(TextFormaterWithJustified())

    text = TextReader.read(input)

    formated_text = text_formater.format(text=text, length=length, justify=justify)

    print(formated_text)


def get_inputs():
    parser = argparse.ArgumentParser(description='Format text file with max line length, may be justified.')

    parser.add_argument('--file', type=str,
                        help='file to format', default="input.txt")

    parser.add_argument('--length', type=int, default=40,
                        help='max line length')

    parser.add_argument('--justify', type=bool, default=False,
                        help='justify text')

    args = parser.parse_args()

    return args


if __name__ == '__main__':
    main()

