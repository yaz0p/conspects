# Singleton

# Для создания синглтона нужно переопределить конструктор и сохранять
# объект в атрибут класса

class Foo(object):
    _isinstance = None

    def __new__(cls, *args, **kwargs):
        if not cls._isinstance:
            cls._isinstance = super().__new__(cls)
        
        return cls._isinstance

    def __init__(self, a: int, b: int) -> None:
        self.a = a
        self.b = b

foo1 = Foo(1, 2)
print(foo1.a)
foo2 = Foo(3, 4) 
print(foo2.a)

# Должно быть True, т.к. ссылается на один и тот же объект
print(foo1 is foo2) 
