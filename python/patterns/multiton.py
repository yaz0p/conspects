# Multiton

# Для каждого уникального атрибута создается новый
# объект не более одного раза

# Реализация через декоратор
def multiton(cls):
    _instance = {}
    def get_instanse(id):
        if id not in _instance:
            _instance[id] = cls(id)
        return _instance[id]
    return get_instanse

@multiton
class Multiton(object):
    def __init__(self, foo: int) -> None:
        self.id = foo

a = Multiton(1)
b = Multiton(2)
c = Multiton(1)

print(a is b) # False
print(a is c) # # True
