from math import sqrt, ceil

from utils import get_int


def check_prime_square_or_none(number: int) -> str or None:
    limit = sqrt(number)
    if limit.is_integer():
        result = 'square'
    else:
        if number in [0, 1]:
            result = None
        elif number == 2:
            result = 'prime'
        else:
            result = 'prime'
            limit = ceil(limit)
            for i in range(2, limit + 1):
                if number % i == 0:
                    result = None
                    break
    return result


def show_primes_or_squares(numbers: list):
    squares = []
    primes = []
    for number in numbers:
        result = check_prime_square_or_none(number)
        if result == 'square':
            squares.append(str(number))
        elif result == 'prime':
            primes.append(str(number))

    print(f'Primes: {", ".join(primes)}')
    print(f'Squares: {", ".join(squares)}')


if __name__ == '__main__':
    generated_list = list(range(0, get_int('limit: ')))
    show_primes_or_squares(generated_list)
