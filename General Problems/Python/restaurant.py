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
        self.orders = []

    def can_prepare_order(self, order: Order) -> bool:
        if dificulties[self.handeled_dificulty.lower()] >= dificulties[order.dificulty.lower()]:
            return True
        return False


class Kitchen:
    def __init__(self, cooks: list[Cook], orders: list[Order]):
        self.cooks = cooks
        self.orders = sorted(orders, key=lambda order: dificulties[order.dificulty.lower()], reverse=True)
        self.times = [0 for _ in range(len(cooks) + 1)]

    def prepare_orders(self):
        added = False
        for order in self.orders:
            able_cooks = [(index, cook) for index, cook in enumerate(self.cooks) if cook.can_prepare_order(order)]
            for index, cook in able_cooks:
                able_cooks_times = [self.times[index] for index, _ in able_cooks]
                to_add_index = able_cooks_times.index(min(able_cooks_times))
                to_add_index, _ = able_cooks[to_add_index]
                self.times[to_add_index] += order.time_needed
                self.cooks[to_add_index].orders.append(order.ID)
                break
        for index, cook in enumerate(self.cooks):
            print(cook.name, self.times[index], cook.orders)
        print(max(self.times))


if __name__ == '__main__':
    kitchen = Kitchen([Cook('Alex', 'complex'), Cook('Hiko', 'easy'), Cook('Lewis', 'master')], [Order(1, 15, 'hard'), Order(2, 30, 'easy'), Order(3, 20, 'complex'), Order(4, 20, 'master'), Order(5, 10, 'intermidiate'), Order(6, 15, 'easy'), Order(7, 45, 'master'), Order(8, 30, 'hard')])
    kitchen.prepare_orders()
