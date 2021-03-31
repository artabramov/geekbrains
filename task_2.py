from abc import abstractmethod


class Cloth:
    def __init__(self, name):
        self.name = name
        self.cost = 0

    def __add__(self, other):
        result = Cloth('Cloth')
        result.cost = self.cost + other.cost
        return result

    @abstractmethod
    def set_cost(self, arg):
        pass

    @property
    def total(self):
        return self.cost


class Coat(Cloth):
    def set_cost(self, size):
        self.cost = size / 6.5 + 0.5


class Suit(Cloth):
    def set_cost(self, length):
        self.cost = length * 2 + 0.5


if __name__ == '__main__':
    coat = Coat('my coat')
    coat.set_cost(54)
    print(coat, type(coat), coat.total)

    suit = Suit('my suit')
    suit.set_cost(180)
    print(suit, type(suit), suit.total)

    clothes = coat + suit
    print(clothes, type(clothes), clothes.total)
