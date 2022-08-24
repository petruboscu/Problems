from utils import get_word


def count_letters_in_word(word: str) -> dict:
    letters_and_counts = {}
    for letter in word:
        letters_and_counts[letter] = word.count(letter)
    return letters_and_counts


if __name__ == '__main__':
    given_word = get_word('word: ')
    letter_counts = count_letters_in_word(given_word.lower())
    for key in letter_counts:
        print(f'Word: {key} -> Count: {letter_counts[key]}')
