import os


class QueueElement:
    def __init__(self, command: str, repeat: int):
        self.command = command
        self.repeat = repeat

    def execute(self):
        for _ in range(self.repeat):
            os.system(self.command)


class Queue:
    def __init__(self):
        self.elements = []
        self.count = 0

    def add_queue_element(self, element: QueueElement):
        self.elements.append(element)

    def pop_queue_element(self):
        if len(self.elements) > 1:
            self.elements = self.elements[1:]
        else:
            self.elements = []

    def execute_n_queue_elements(self, n: int):
        for _ in range(n):
            self.elements[0].execute()
            self.pop_queue_element()

    def execute_all_queue_elements(self):
        while len(self.elements) > 0:
            self.elements[0].execute()
            self.pop_queue_element()


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
