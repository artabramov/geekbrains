class Stationery:

    def __init__(self, name):
        self.name = name

    def draw(self, param=''):
        print(f'{param}go drawing!')


class Pen(Stationery):
    def draw(self):
        super().draw(f'{self.name} says: ')


class Pencil(Stationery):
    def draw(self):
        super().draw(f'{self.name} cries: ')


class Handle(Stationery):
    def draw(self):
        super().draw(f'{self.name} laughs: ')


if __name__ == '__main__':
    pen = Pen('my blue pen')
    pen.draw()

    pencil = Pencil('my red pencil')
    pencil.draw()

    handle = Handle('my black handle')
    handle.draw()
