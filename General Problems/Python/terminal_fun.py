from abc import ABC, abstractmethod
import os


class Command(ABC):
    """Abstract Command class"""
    @abstractmethod
    def run(self) -> None:
        pass


class GeneralCommand(Command):
    """General Command class that has one word commands"""

    def __init__(self, command: str):
        self.command = command.lower()

    def run(self) -> None:
        match self.command:
            case 'help':
                print('This should return a list of commands and thier corresponding explications, but ... oh Well')
            case 'nice':
                print('Wow you are really intrested now Eh?')
            case 'clear':
                os.system('cls')
            case 'quit':
                print('... Hello Darknes my old friend')
                quit()
            case other:
                print('We do not have that here, sorry')


class FileCommand(Command):
    """FiLe Command class that has two words commands: command, filename """

    def __init__(self, command: str, filename: str):
        self.command = command.lower()
        self.filename = filename.lower()

    def run(self) -> None:
        match [self.command, self.filename]:
            case ['run', filename]:
                if '.py' in filename:
                    os.system(f'python {filename}')
                else:
                    print(f'{filename} is not a python executable')
            case ['create', filename]:
                if os.path.isfile(filename):
                    print(f'{filename} already exists')
                else:
                    open(filename, 'w')
                    print(f'{filename} was created')
            case ['open', filename]:
                if os.path.isfile(filename):
                    os.system(f'vim {filename}')
                else:
                    print(f'{filename} does not exists')
            case ['delete', filename]:
                if os.path.isfile(filename):
                    os.system(f'del {filename}')
                    print(f'{filename} was deleted')
                else:
                    print(f'{filename} does not exists')
            case _:
                print("We don't have that here, sorry")


class ComplexCommand(Command):
    """TBD"""
    pass


class CommandGenerator:
    def generate_general_command(self, text: str):
        return GeneralCommand(text)

    def generate_file_command(self, text: str):
        command, filename = text.split()
        return FileCommand(command, filename)

    def generate_complex_command(self, text):
        """TBD"""
        pass


class CommandExecutor:

    def __init__(self):
        self.generator = CommandGenerator()

    def execute(self, text: str):
        if text.count(' ') == 0:
            self.generator.generate_general_command(text).run()
        elif text.count(' ') == 1:
            self.generator.generate_file_command(text).run()


if __name__ == '__main__':
    executor = CommandExecutor()
    while True:
        executor.execute(input('$ '))
