from functools import wraps


def parent_wrapper(callback):
    @wraps(callback)
    def child_wrapper(*args):
        for arg in args:
            print(f'{callback.__name__} ({arg}: {type(arg)})')
        return callback(*args)
    return child_wrapper


@parent_wrapper
# Don't understand how it must works with multiple arguments (see the task). Get the first arg to calculate result?
def calc_cube(*x):
    return x[0]**3


if __name__ == '__main__':
    print(calc_cube.__name__)
    result = calc_cube(3, 4, 5)
    print(result)
