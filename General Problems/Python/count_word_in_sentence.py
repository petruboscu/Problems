from utils import get_sentence


def count_words_from_sentence(sentence: str) -> dict:
    words = [word.replace('.', '').replace(',', '').replace('?', '').replace('!', '').lower()
             for word in sentence.split(' ')]
    words_and_counts = {}
    for word in words:
        words_and_counts[word] = sentence.count(word)
    return words_and_counts


if __name__ == '__main__':
    given_sentence = get_sentence('sentence: ')
    word_counts = count_words_from_sentence(given_sentence.lower())
    for key in word_counts:
        print(f'Word: {key} -> Count: {word_counts[key]}')
