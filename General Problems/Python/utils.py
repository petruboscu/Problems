import os


def get_int(input_text: str):
    os.system('cls')
    number = None
    while number is None:
        text = input(input_text)
        if text.isdigit():
            number = int(text)
        else:
            os.system('cls')
    return number


def get_word(input_text: str):
    os.system('cls')
    word = None
    while word is None:
        text = input(input_text)
        if any(char.isdigit() or char in [' ', ',', ';', '_', '-'] for char in text):
            os.system('cls')
        else:
            word = text
    return word


def get_sentence(input_text: str):
    os.system('cls')
    sentence = None
    while sentence is None:
        text = input(input_text)
        if any(char.isdigit() or char in ['_', '-'] for char in text):
            os.system('cls')
        else:
            sentence = text
    return sentence
