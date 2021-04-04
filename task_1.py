import re


class Date:
    re_split = re.compile(r'-')

    def __init__(self, raw_date):
        self.raw_date = raw_date
        self.date = Date.split(self.raw_date)

    @classmethod
    def split(cls, raw_date):
        return list(map(lambda x: int(x), re.split(cls.re_split, raw_date)))

    @staticmethod
    def validate(date):
        """ the number of days in each month is not checked """
        return 1 <= date[0] <= 31 and 1 <= date[1] <= 12 and isinstance(date[0], int)

    def __str__(self):
        return f'{self.date[0]}.{self.date[1]}.{self.date[2]} ({self.validate(self.date)})'


if __name__ == "__main__":
    date_1 = Date('12-04-1961')
    print(date_1)

    date_2 = Date('7-11-1917')
    print(date_2)

    date_3 = Date('01-13-2021')
    print(date_3)
