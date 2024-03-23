# Декоратор - функция высшего порядка, т.е. она принимает другую функцию
# Пример реализации декоратора
def null_decorator(func):
    return func

def greet():
    return "Hello!"

example = null_decorator(greet)

print(example())

@null_decorator
def greet():
    return "Hello from dec. func."

print(greet())

# Декоратор, изменяющий поведение функции

def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

@uppercase
def greet():
    return "Hello from dec. func."

print(greet())
