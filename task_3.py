class IntegerException(Exception):
    def __init__(self, value):
        self.txt = value

    @staticmethod
    def is_int(value):
        if not value.isnumeric():
            raise IntegerException('value is not integer')

    def __str__(self):
        return self.txt


if __name__ == '__main__':
    print('input numbers ("stop" to exit)')
    numbers = []
    while True:
        tmp = input('>')
        if tmp == 'stop':
            break
        try:
            IntegerException.is_int(tmp)
            numbers.append(tmp)
        except IntegerException as e:
            print(e)

    print(numbers)
