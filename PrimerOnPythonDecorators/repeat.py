import functools


def repeat1(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper

    return decorator_repeat


def repeat2(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper

    if _func is None:
        return decorator_repeat

    return decorator_repeat(_func)


# greet = repeat(num_times=4)(greet)
@repeat1(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet('Oi')

# 1 greet = repeat(num_times=4)(greet)
@repeat2(num_times=4)
def greet1(name):
    print(f"Hello1 {name}")

# 2 greet = repeat(greet)
@repeat2
def greet2(name):
    print(f"Hello2 {name}")

greet1('Oi')
greet2('Oi')
