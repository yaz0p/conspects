# Дженерики -- реализация параметрического полиморфизма. 
# В случае с питоном ( типы определяются объектами во время рантайма )
# помогает отслеживать возможные ошибки в написании кода. 
from typing import TypeVar, TypeAlias, Dict, Generic

T = TypeVar('T') # определяем произвольный тип
V = TypeVar('V')

def foo(bar: list[T]) -> T:
     return bar[0]

a = foo([1,2,3])
b = foo(['a','b','c'])

print(a + 2)
print(b + 'b')

# Так же в модуле typing присутствует TypeAlias, позволяющий создавать псевдонивмы для типов

Point: TypeAlias = tuple[float, float]
Triangle: TypeAlias = tuple[Point, Point, Point]

print(type(Point))
print(type(Triangle))
print(type(T))
point: Point = (1.2, 1.3) # кастомный класс, позволяющий отслеживать состояние типов
triangle: Triangle = ((1.2, 1.3), (1.2, 1.3), (1.2, 1.3))

triangles: Triangle = ((1.2, 1.3, 4), (1.2, 1.3), (1.2, 1.3)) # mypy подсветит ошибку

MyDict: TypeAlias = Dict[V, T]
slovar: MyDict[str, int] = {'foobar': 5}
slovar['barfoo'] = 2

# Можно создавать дженерики.
# Дженерики (или обобщенные типы) в программировании — это механизм,
# позволяющий создавать классы, интерфейсы и методы с параметрами типов.

class Container(Generic[T]):
    def __init__(self, item: T):
        self.item = item

    def get_item(self) -> T:
        return self.item

int_container = Container[int](10) # Можно передавать тип явно и неявно
print(int_container.get_item())  # Вывод: 10

str_container = Container("Hello")
print(str_container.get_item())  # Вывод: Hello

