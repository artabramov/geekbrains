class Worker:

    def __init__(self, **kwargs):
        self._income = {'wage': 0, 'bonus': 0}
        for i in kwargs:
            if i in ['wage', 'bonus']:
                self._income[i] = kwargs[i]
            elif i != '_income':
                setattr(self, i, kwargs[i])


class Position(Worker):

    def get_full_name(self):
        try:
            return f'{self.name} {self.surname}'
        except Exception:
            raise ValueError('Achtung! Name and surname must be exists!')

    def get_total_income(self):
        try:
            return f'{self._income["wage"] + self._income["bonus"]}'
        except Exception:
            raise ValueError('Achtung! Wage and bonus must be numeric!')


if __name__ == '__main__':
    user = Position(name='Stephen', surname='King', wage=100, bonus=50.5)
    print(user.get_full_name())
    print(user.get_total_income())
