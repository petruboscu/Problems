def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').replace(',', '').replace(':', '').replace(';', '').replace('.', '').replace('?', '')
    reversed_string = string[-1::-1]
    if string.lower() == reversed_string.lower():
        return True
    else:
        return False


if __name__ == '__main__':
    input_string = input('Input string: ')
    print(is_palindrome(input_string))
