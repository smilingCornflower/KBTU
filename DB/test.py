from functools import wraps

def add(x, y):
    return x + y

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result ** 2
    return wrapper

add = my_decorator(add)
