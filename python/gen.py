def foo(bar: int):
    print("Вхождение")
    yield f'Число при первом вхождении {bar}'
    print('Следующий вызов ')
    yield f'{bar-1}'

generator_object = foo(1)
print("Я СОЗДАЛ ОБЪЕКТ-ГЕНЕРАТОР")
print("ПЕРВОЕ ВХОЖДЕНИЕ")
print(next(generator_object))
print("ВТОРОЕ ВХОЖДЕНИЕ")
print(next(generator_object))
print(next(generator_object))
