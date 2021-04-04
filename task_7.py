class Complex:
    def __init__(self, real, image):
        self.real = real
        self.image = image

    def __str__(self):
        return f'{self.real} + {self.image}i'

    def __add__(self, other):
        return Complex(self.real + other.real, self.image + other.image)

    def __mul__(self, other):
        return Complex(self.real * other.real + (-1) * abs(self.image * other.image),
                       self.real * other.image + self.image * other.real)


if __name__ == '__main__':
    num_1 = Complex(1, 3)
    print(num_1)

    num_2 = Complex(2, 1)
    print(num_2)

    num_3 = num_1 + num_2
    print('sum:', num_3)

    num_4 = num_1 * num_2
    print('mul:', num_4)
