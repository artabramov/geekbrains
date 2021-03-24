from functools import wraps


def outer_wrapper(negative):
    def middle_wrapper(callback):
        @wraps(callback)
        def inner_wrapper(arg):
            if negative(arg):
                raise ValueError(f'Achtung! Falsch Ausweis: {arg}')
            return callback(arg)
        return inner_wrapper
    return middle_wrapper


@outer_wrapper(lambda x: x < 0)
def cube(x):
    return x**3


if __name__ == '__main__':
    print(cube.__name__)
    print(cube(2))
    print(cube(-2))
