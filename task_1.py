import time


class TrafficLight:

    colors = [
        ['red', 7],
        ['yellow', 2],
        ['green', 5]
    ]

    def __init__(self, color):
        for i in range(0, len(self.colors)):
            if self.colors[i][0] == color:
                self.i = i
                self._switch()
                return
        raise ValueError('Incorrect start color')

    def __next__(self):
        self.i = self.i + 1 if self.i < len(self.colors) - 1 else 0
        self._switch()

    def __str__(self):
        return f'{self.__color} ({self.pause})'

    def _switch(self):
        self.pause = self.colors[self.i][1]
        self.__color = self.colors[self.i][0]


if __name__ == '__main__':
    light = TrafficLight('yellow')
    while True:
        print(light)
        time.sleep(light.pause)
        next(light)
