from utils import get_sentence

vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowels(sentence: str) -> int:
    return sum([sentence.count(vowel) for vowel in vowels])


if __name__ == '__main__':
    # given_sentence = get_sentence('Sentence: ')
    given_sentence = 'The only way to make the world a better place is for you to be kind'
    print(f'The total count of vowels is {count_vowels(given_sentence)}')
