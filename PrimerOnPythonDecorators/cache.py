import functools


def cache(func):
    """keep a cache of previous function calls"""
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache



def count_calls(func):
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls

# @count_calls
# @cache
# def fibonacci(num):
#     if num < 2:
#         return num

#     return fibonacci(num-1) + fibonacci(num-2)


@functools.lru_cache(maxsize=128)
def fibonacci(num):
    print(f"Calculating fibonacci({num})")
    if num < 2:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(10))
print(fibonacci(8))

# print(fibonacci.num_calls)
# print(fibonacci.cache)

print(fibonacci.cache_info())
