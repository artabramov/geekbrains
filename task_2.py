class ZeroDivision(Exception):
    def __init__(self, value):
        self.txt = value


if __name__ == "__main__":
    a, b = 1, 0
    if b == 0:
        raise ZeroDivision('Division by zero!')
    print(a / b)
