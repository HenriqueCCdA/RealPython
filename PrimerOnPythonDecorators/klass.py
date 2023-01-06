import functools


class CounterCalls:

    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


# say_whee = CounterCalls(say_whee)
@CounterCalls
def say_whee():
    print("Whee!")



say_whee()
say_whee()
