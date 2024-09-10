# Функция-генератор позволяет объявить функцию, ведущую себя, как `итератор`
from typing import Iterator, Self

def generator() -> Iterator[int]:
    print("Сейчас отдам число")
    yield 1
    print("Сейчас отдам ещё число")
    yield 2
    print("Больше ничего нету!")


# попробуем выполнить вот такой код:
gen_o = generator()  # тут у нас будет создан и записан в переменную generator-object

print(gen_o)
print(next(gen_o))
print("Ого, мы только что получили число из объекта-генератора по запросу!")
print(next(gen_o))

# результат, который будет выведен в консоль:
# >>> generator object <name>
# >>> Сейчас отдам число
# >>> 1
# >>> Ого, мы только что получили число из объекта-генератора по запросу!
# >>> Сейчас отдам ещё число
# >>> 2

gen_o = generator()
print(next(gen_o))
print("Ого, мы только что получили число из объекта-генератора по запросу!")
print(next(gen_o))
# print(next(gen_o))

# результат, который будет выведен в консоль:
# >>> 1
# >>> Ого, мы только что получили число из объекта-генератора по запросу!
# >>> Сейчас отдам ещё число
# >>> 2
# >>> Больше ничего нету!
# >>> Traceback (most recent call last):
# >>> File "<путь исполняемого файла>", line 13, in <module>
# >>> print(next(gen_o))
# >>> StopIteration


# generator-object можно «отстрелять» только один раз и только вперёд.
# Вернуться в прошлое или каким-то образом «обнулить» его нельзя.
# Для generator-object предполагается, что при необходимости мы просто
# запустим нашу функцию generator ещё раз и получим новый объект для работы


class MyIterable:
    '''
    Custom generator class for implementation
    '''
    def __init__(this) -> None:
        this.value = 0  # правило создания экземпляра класса

    def __iter__(this) -> Self:
        print("Был получен итератор")
        return this  # возвращение числа при вызове итератора

    def __next__(this) -> int:
        this.value += 1  # возвращение значения при вызове метода next
        print("Current value", this.value)
        if this.value < 5:
            return this.value
        else:
            raise StopIteration


print("")
print("List of comprehension")
l = [a for a in MyIterable()]
print(l)
for i in l:
    print(i)


# List of comprehension проходится по списку при помощи метода next
# и добавляет полученные значения в новый список

# Current value 1
# Current value 2
# Current value 3
# Current value 4
# Current value 5
# [1, 2, 3, 4]
# 1
# 2
# 3
# 4

print("")
print("Create gen from list")
d = (a for a in MyIterable())
print(d)
for i in d:
    print(i)

# <generator object <genexpr> at 0x7093f83c9a40>
# Current value 1
# 1
# Current value 2
# 2
# Current value 3
# 3
# Current value 4
# 4
# Current value 5

# На каждой yield работа функции временно приостанавливается,
# при этом сохраняется состояние исполнения,
# включая локальные переменные, указатель на текущую инструкцию,
# внутренний стек и состояние обработки исключения.
# При последующем обращении к итератору генератора (при вызовах его методов)
# функция продолжает своё исполнение с места, на котором была приостановлена.
# Этим функции-генераторы отличаются от обычных функций, при вызове которых
# исполнение всякий раз начинается с начала.

# Если функция достигает инструкции return, либо конца
# (без указания упомянутой инструкции),
# возбуждается исключение StopIteration и итератор исчерпывает себя.

g = (x**2 for x in range(10))
print("")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
