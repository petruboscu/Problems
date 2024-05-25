from abc import ABC, abstractmethod
import os


# Abstract Command class
class Command(ABC):
    """Abstract Command class"""
    @abstractmethod
    def run(self) -> None:
        pass


# General Command class that has one word commands
class GeneralCommand(Command):
    """General Command class that has one word commands"""

    def __init__(self, command: str):
        self.command = command.lower()

    def run(self) -> None:
        # Match the command and execute the corresponding action
        match self.command:
            case 'help':
                print('This should return a list of commands and their corresponding explanations, but ... oh Well')
            case 'nice':
                print('Wow you are really interested now Eh?')
            case 'clear':
                os.system('cls')  # Clear the console
            case 'quit':
                print('... Hello Darkness my old friend')
                quit()  # Quit the program
            case other:
                print('We do not have that here, sorry')


# File Command class that has two words commands: command, filename
class FileCommand(Command):
    """File Command class that has two words commands: command, filename """

    def __init__(self, command: str, filename: str):
        self.command = command.lower()
        self.filename = filename.lower()

    def run(self) -> None:
        # Match the command and filename, and execute the corresponding action
        match [self.command, self.filename]:
            case ['run', filename]:
                if '.py' in filename:
                    os.system(f'python {filename}')  # Run a Python file
                else:
                    print(f'{filename} is not a python executable')
            case ['create', filename]:
                if os.path.isfile(filename):
                    print(f'{filename} already exists')
                else:
                    os.system(f'type nul > {filename}')  # Create a new file
                    print(f'{filename} was created')
            case ['open', filename]:
                if os.path.isfile(filename):
                    os.system(f'vim {filename}')  # Open a file in Vim
                else:
                    print(f'{filename} does not exist')
            case ['delete', filename]:
                if os.path.isfile(filename):
                    os.system(f'del {filename}')  # Delete a file
                    print(f'{filename} was deleted')
                else:
                    print(f'{filename} does not exist')
            case _:
                print("We don't have that here, sorry")


# Complex Command class (not implemented)
class ComplexCommand(Command):
    """TBD"""
    pass


# Command Generator class
class CommandGenerator:
    def generate_general_command(self, text: str):
        return GeneralCommand(text)

    def generate_file_command(self, text: str):
        command, filename = text.split()
        return FileCommand(command, filename)

    def generate_complex_command(self, text):
        """TBD"""
        pass


# Command Executor class
class CommandExecutor:

    def __init__(self):
        self.generator = CommandGenerator()

    def execute(self, text: str):
        # Check the number of spaces in the input text
        if text.count(' ') == 0:
            # If there are no spaces, it's a general command
            self.generator.generate_general_command(text).run()
        elif text.count(' ') == 1:
            # If there is one space, it's a file command
            self.generator.generate_file_command(text).run()
        else:
            print(f'{text} was not implemented yet')


if __name__ == '__main__':
    executor = CommandExecutor()
    while True:
        # Get user input and execute the corresponding command
        executor.execute(input('$ '))
