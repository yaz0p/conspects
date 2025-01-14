# В теории языка программирования и теории типов полиморфизм - это использование одного
# символа для представления нескольких различных типов. 
# В объектно-ориентированном программировании полиморфизм - это предоставление одного
# интерфейса объектам различных типов данных. 
# Концепция заимствована из принципа биологии, при котором организм или
# вид может иметь множество различных форм или стадий.
#
# Типы полиморфизма:
#
# Ad hoc полиморфизм: 
# Определяет общий интерфейс для произвольного набора индивидуально определенных типов.

# Параметрический полиморфизм: 
# Не указывать конкретные типы и вместо этого использовать абстрактные символы,
# которые могут заменить любой тип.

# Подтипирование (также называемое полиморфизмом подтипа или полиморфизмом включения):
# когда имя обозначает экземпляры многих различных классов,
# связанных с каким-то общим суперклассом.

# Так как Python язык с динамической типизацией и на нем нельзя полноценно
# продемонстрировать работу полиморфизма, то я приведу код для языка программирования 
# C++

# Ad hoc пример:

class AdHocPolymorphic {
    public String add(int x, int y) {
        return "Sum: "+(x+y);
    }

    public String add(String name) {
        return "Added "+name;
    }
}

public class adhoc {
    public static void main(String[] args) {
        AdHocPolymorphic poly = new AdHocPolymorphic();

        System.out.println( poly.add(1,2)   ); // prints "Sum: 3"
        System.out.println( poly.add("Jay") ); // prints "Added Jay"
    }
}

# В python вместо перегрузки можно использоваться диспетчиризацию: в зависимости от
# типа входящего аргумента будет выбираться конкретная реализация функционала

from functools import singledispatch

@singledispatch
def process(value):
    print(f"Default processing for {type(value).__name__}")

@process.register(int)
def _(value: int):
    print(f"Processing integer: {value}")

@process.register(str)
def _(value: str):
    print(f"Processing string: {value}")
process(42)       # Перегрузка для int — выводит "Processing integer: 42"
process("Hello")  # Перегрузка для str — выводит "Processing string: Hello"

# В примере выше мы объявляем класс с публичным методом add, который в зависимости от
# Типов переданных аргументов ведет себя по разному. 
# Данная реализация полиморфизма называется `перегрузкой`. 
# По идее, в языках программирования с динамической типизацией все функции являются функциями
# с перегрузкой, так как типы определяются в рантайме. 

# Python позволяет указать Generic тип, который будет подсвечиваться mypy, 
# так что покажу реализацию через Python и C++

# Параметрический полиморфизм пример:

# ```Python```
from typing import TypeVar, Generic

T = TypeVar('T')
class ParametricPolymorphic(Generic[T]):
    def __init__(self):
        pass

    @staticmethod
    def add(x: T, y: T) -> T:
        return x + y

ParametricPolymorphic[int].add(4, 9) # 13
ParametricPolymorphic[str].add('foo', 'bar') # foobar

# В языке программирования C++ реализация параметрического полиморфизма происходит
# Через шаблоны

#include <iostream>
using namespace std;

// Шаблон функции для сложения двух значений
template <typename T>
T add(T a, T b) {
    return a + b;
}

int main() {
    cout << add<int>(3, 4) << endl;    // вызов для целых чисел
    cout << add<double>(2.5, 4.5) << endl;  // вызов для вещественных чисел
    return 0;
}

######################################################################################

#include <iostream>
using namespace std;

// Шаблон класса для хранения пары значений
template <typename T>
class Pair {
private:
    T first, second;
public:
    Pair(T a, T b) : first(a), second(b) {}
    T getFirst() const { return first; }
    T getSecond() const { return second; }
};

int main() {
    Pair<int> intPair(1, 2);      // Экземпляр для целых чисел
    Pair<double> doublePair(3.5, 4.5);  // Экземпляр для вещественных чисел

    cout << "First: " << intPair.getFirst() << ", Second: " << intPair.getSecond() << endl;
    cout << "First: " << doublePair.getFirst() << ", Second: " << doublePair.getSecond() << endl;

    return 0;
}


# Подтипный полиморфизм:
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal: Animal):
    print(animal.speak())

make_sound(Dog())  # "Woof!"
make_sound(Cat())  # "Meow!"

