from utils import get_sentence

if __name__ == '__main__':
    sentence = get_sentence('sentence:')

    special_characters = ['.', '!', ',', ';', '?']
    for special_character in special_characters:
        sentence = sentence.replace(special_character, '')

    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[-1::-1])

    reversed_sentence = ' '.join(reversed_words)

    print(f'Sentence: {sentence}')
    print(f'Reversed Sentence: {reversed_sentence}')
