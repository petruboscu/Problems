import os


class QueueElement:
    def __init__(self, action: str, arguments: list, repeat: int):
        self.action = action
        self.arguments = arguments
        self.repeat = repeat

    def execute(self):
        for _ in range(self.repeat):
            if self.action == 'log':
                print(' '.join(self.arguments))
            elif self.action == 'run':
                os.system(f'python {" ".join(self.arguments)}')


class Queue:
    def __init__(self):
        self.elements = []
        self.count = 0

    def add_queue_element(self, element: QueueElement):
        self.elements.append(element)

    def pop_queue_element(self):
        if len(self.elements) > 1:
            self.elements = self.elements[1:]
        else:
            self.elements = []

    def execute_n_queue_elements(self, n: int):
        for _ in range(n):
            self.elements[0].execute()
            self.pop_queue_element()

    def execute_all_queue_elements(self):
        while len(self.elements) > 0:
            self.elements[0].execute()
            self.pop_queue_element()


if __name__ == '__main__':
    queue = Queue()
    first_queue_element = QueueElement('log', ['Hello', 'World'], 3)
    second_queue_element = QueueElement('run', ['task_one.py', 'Petru', 'Boscu'], 1)
    third_queue_element = QueueElement('run', ['task_two.py', '3', '50', 'hey', '4'], 1)

    queue.add_queue_element(first_queue_element)
    queue.add_queue_element(second_queue_element)
    queue.add_queue_element(third_queue_element)
    queue.execute_all_queue_elements()
