class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Cell ({str(self.number)})'

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.number + other.number)

    def __sub__(self, other):
        if isinstance(other, Cell) and self.number > other.number:
            return Cell(self.number - other.number)
        print('invalid subtraction')

    def __mul__(self, other):
        if isinstance(other, Cell) and self.number != other.number != 0:
            return Cell(self.number * other.number)
        print('invalid multiplication')

    def __floordiv__(self, other):
        if isinstance(other, Cell) and other.number != 0:
            return Cell(self.number // other.number)
        print('invalid division')

    def make_order(self, cell, row_elements):
        remain, output = cell.number, ''
        for row in range(0, cell.number // row_elements + 1):
            output += f'{"*" * remain}\n' if remain < row_elements else f'{"*" * row_elements}\n'
            remain -= row_elements
        return output


if __name__ == '__main__':
    cell_1 = Cell(5)
    print(cell_1)

    cell_2 = Cell(4)
    print(cell_2)

    cell_3 = Cell(0)
    print(cell_3)

    print('add:')
    print(cell_1 + cell_2 + cell_3)

    print('sub:')
    print(cell_1 - cell_2)
    print(cell_2 - cell_1)

    print('mul:')
    print(cell_1 * cell_2)
    print(cell_1 * cell_3)

    print('floor:')
    print(cell_1 // cell_2)
    print(cell_1 // cell_3)

    print('order')
    cell_4 = Cell(10)
    print(cell_4.make_order(cell_4, 3))
