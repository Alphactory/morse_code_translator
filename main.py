from MorseTranslator import MorseTranslator
from MorseListener import MorseListener


def main():
    ml = MorseListener()
    mt = MorseTranslator()
    print(mt.translate(ml.morse_string))


main()
