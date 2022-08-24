from utils import get_int


def show_indexes_and_elements(elements: list):
    text = '[ '
    for index, element in enumerate(elements):
        text += f'{index}:({element}), '
    text = text[:-2]
    text += ' ]'

    print(text)


if __name__ == '__main__':
    limit = get_int('limit: ')
    multiplier = get_int('multiplier: ')
    generated_elements = [x * multiplier for x in range(1, limit + 1)]
    show_indexes_and_elements(generated_elements)
