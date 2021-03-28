class Car:

    def __init__(self, **kwargs):
        self.speed, self.color, self.name, self.is_police = 0, '', '', False
        for _ in kwargs:
            setattr(self, _, kwargs[_])

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        self.direction = direction

    def show_speed(self):
        try:
            print(f'Speed: {self.speed + 0}')
        except Exception:
            raise ValueError('Achtung! Car speed must exists and be numeric!')


class SlowCar(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_speed(self):
        super().show_speed()
        if self.speed > self.speed_limit:
            print(f'Please, decrease the speed to {self.speed_limit}.')


class TownCar(SlowCar):
    speed_limit = 60


class WorkCar(SlowCar):
    speed_limit = 40


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


if __name__ == '__main__':
    print('Town car')
    car = TownCar(speed=60)
    car.show_speed()

    print('\nWork car')
    car = WorkCar(speed=60)
    car.show_speed()

    print('\nSport car')
    car = SportCar()
    car.go(200)
    car.show_speed()
    car.stop()
    car.show_speed()
