import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for argument in sys.argv[1:]:
            if argument.isdigit():
                for i in range(int(argument)):
                    print(i, end=" ")
                print()
            else:
                print(f'{argument} is not an integer')
    else:
        print('You did not give Task One any arguments.')
