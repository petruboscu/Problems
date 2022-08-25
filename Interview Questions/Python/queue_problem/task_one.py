import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print('You gave Task One the following arguments:')
        for index, argument in enumerate(sys.argv[1:]):
            print(f'{index + 1}: {argument}')
    else:
        print('You did not give Task One any arguments.')
