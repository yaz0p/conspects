# Декоратор - функция высшего порядка, т.е. она принимает другую функцию,
# но вообще может принимать любой callable объект
# Пример реализации декоратора
def null_decorator(func):
    return func


def greet():
    return "Hello!"


print(null_decorator(greet)())


@null_decorator
def greet():
    return "Hello from dec. func."


print(greet())

# Декоратор, изменяющий поведение функции


def uppercase(func):
    def wrapper(*args, **kwargs):
        print(*args, **kwargs)
        original_result = func(*args, **kwargs)
        modified_result = original_result.upper()
        return modified_result

    return wrapper


def greet(a=None,b=None,c=None):
    return "Hello from dec. func."


print(uppercase(greet)('foo','bar','baz'), '\n') # если писать декоратор без синтаксического сахара


@uppercase
def greet(a=None,b=None,c=None):
    return "Hello from dec. func."

print(greet('Иван', "Родил", "Дочурку")) # с синтаксическим сахаром
