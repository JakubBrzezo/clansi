import argparse
from library.clansi import Clansi


def main():
    """Demo application which show how to use Clansi library. Function works with argparse library and basing
        on given arguments it prints colored text to the console to show how it works.
    """
    parser = argparse.ArgumentParser(description='Demo application for Clansi library')
    parser.add_argument('-c', '--color', type=str, default='white', help='Color of the text')
    parser.add_argument('-t', '--text', type=str, default='Hello World!', help='Text to print')
    args = parser.parse_args()

    colour = args.color
    if 'white' == colour:
        print(Clansi.white(args.text))
    elif 'red' == colour:
        print(Clansi.red(args.text))
    elif 'green' == colour:
        print(Clansi.green(args.text))
    elif 'yellow' == colour:
        print(Clansi.yellow(args.text))
    elif 'blue' == colour:
        print(Clansi.blue(args.text))
    elif 'magenta' == colour:
        print(Clansi.magenta(args.text))
    elif 'cyan' == colour:
        print(Clansi.cyan(args.text))
    elif 'black' == colour:
        print(Clansi.black(args.text))


if __name__ == '__main__':
    main()
