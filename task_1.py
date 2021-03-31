class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        output = ''
        for row in self.matrix:
            output += f'{str(row)}\n'
        return output

    def __add__(self, other):
        if not all(list(map(lambda x, y: len(x) == len(y), self.matrix, other.matrix))):
            raise ValueError('matrices length are not the same')

        result = []
        for i, j in zip(self.matrix, other.matrix):
            result.append(list(map(lambda x, y: x + y, i, j)))
        return Matrix(result)


if __name__ == '__main__':
    m = Matrix([[1, 2, 3], [4, 5, 6]])
    print(type(m), m, sep='\n')

    n = Matrix([[7, 8, 9], [3, 6, 1]])
    print(type(n), n, sep='\n')

    p = m + n
    print(type(p), p, sep='\n')
