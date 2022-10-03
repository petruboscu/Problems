dificulties = {'easy': 1, 'intermidiate': 2, 'hard': 3, 'complex': 4, 'master': 5}


class Order:
    def __init__(self, ID: int, time_needed: int, dificulty: str):
        self.ID = ID
        self.time_needed = time_needed
        self.dificulty = dificulty


class Cook:
    def __init__(self, name: str, handeled_dificulty: str):
        self.name = name
        self.handeled_dificulty = handeled_dificulty

    def can_prepare_order(self, order: Order) -> bool:
        if dificulties[self.handeled_dificulty.lower()] > dificulties[order.dificulty.lower()]:
            return True
        return False


class Kitchen:
    def __init__(self, cooks: list[Cook], orders: list[Order]):
        self.cooks = cooks
        self. orders = orders
