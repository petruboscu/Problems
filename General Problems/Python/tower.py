class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.size = length * width


class TowerBlock:
    def __init__(self, rectangle: Rectangle, color: str):
        self.rectangle = rectangle        self.color = color

    def __str__(self):
        return f'Tower Block: Rectangle({self.rectangle.length}, {self.rectangle.width}) {self.color}'


class Tower:
    def __init__(self):
        self.blocks = []

    def add_block(self, block: TowerBlock):
        self.blocks.append(block)

    def check_construction(self):
        previous_block = blocks[0]
        for block in blocks[1:]:
            if block.rectangle.size > previous_block.rectangle.size and block.color == previous_block.color:
                return False
            previous_block = block
        return True


if __name__ == '__main__':
    lengths = [5, 6, 2, 3, 9, 1, 4, 8, 7, 10]
    widths = [13, 11, 16, 19, 15, 14, 12, 17, 18, 20]
    colors = ['red', 'blue', 'yellow', 'orange', 'black', 'red', 'blue', 'yellow', 'orange', 'black']

    blocks = [TowerBlock(Rectangle(length, width), color) for length, width, color in zip(lengths, widths, colors)]
    blocks = sorted(blocks, key=lambda block: block.rectangle.size)

    tower = Tower()
    for block in blocks[-1::-1]:
        if len(tower.blocks) == 0:
            tower.add_block(block)
        else:
            if tower.blocks[-1].color != block.color:
                tower.add_block(block)

    for block in tower.blocks:
        print(block)
    if tower.check_construction():
        print('The Tower is safe and sound.')
    else:
        print('This Tower does not look so good.')
