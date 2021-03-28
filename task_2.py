class Road:

    #  asphalt gravity per 1 cubic meter in tonnes
    gravity = 1.5

    # length and width in meters (!)
    def __init__(self, length, width, **kwargs):
        self._length, self._width = length, width
        self.depth = kwargs['depth'] if 'depth' in kwargs else None

    # depth in centimeters (!), result in tonnes (!)
    def get_weight(self):
        if not hasattr(self, 'depth'):
            raise ValueError('Achtung! You must set the road depth!')
        try:
            return self._length * self._width * self.depth * self.gravity / 100
        except Exception:
            raise ValueError('Achtung! Road params are incorrect!')


if __name__ == '__main__':
    road = Road(5000, 20, depth=5)
    print(f'{road.get_weight()} tonnes')
