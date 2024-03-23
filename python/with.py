# Инструкция позволяет задействовать менеджер контекста 
# для исполнения кода, находящего в её теле. Это, в частности,
# позволяет обособить блоки, использующие try except finally
# и повысить шансы их повторного использования.

class MyContextManager(object):
    
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit")

with MyContextManager(): # enter 
    print("FOO") # FOO 
# exit 

# Выражение после with вычисляется для получения менеджера контекста;
# Для последующего использования запоминается метод менеджера __exit__();
# Вызывается метод менеджера __enter__();
# Если после as указана цель, то в неё помещается результат __enter__();
# Выполняется тело инструкции;
# Вызывается метод __exit__(). 
# Если выход обусловлен исключением, то данные о нём передаются в метод.
# Если __exit__() вернул ложь, то по выходу из контекстного менеджера 
# исключение продолжит своё восхождение по стеку. 
# В случае истины, исключение будет подавлено.

#   with manager1() as one, manager2() as two:
#   do()
        
# То же самое, вложенно:
#   with manager1() as one:
#   with manager2() as two:
#       do()
