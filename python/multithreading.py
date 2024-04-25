# В данном конспекте будет разобрана работа Python в мультипотоком/
# мультипроцессингом на интерпретаторе CPython. 
# Данный конспект не рассматривает другие интерпретаторы, такие как:
# IronPython, Jython и PyPy
# Реализация счетчика на Python при помощи мультипоток

# Имплементация класса счетчика
import threading

class Counter(object):
    def __init__(self):
        self.val = 0

    def change(self):
        self.val += 1

def work(counter, operations_count):
    for _ in range(operations_count):
        counter.change()

def run_threads(counter, threads_count, operations_per_thread_count):
    threads = []

    for _ in range(threads_count):
        t = threading.Thread(target=work, args=(counter, operations_per_thread_count))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def stand_count():
    threads_count = 10
    operations_per_thread_count = 1000000 
    expected_counter_value = threads_count * operations_per_thread_count
    counters = [Counter()]
    
    for counter in counters:
      run_threads(counter, threads_count, operations_per_thread_count)
      print(f"{counter.__class__.__name__}: expected val: {expected_counter_value}, actual val: {counter.val}")


class CounterWithConversion:
  def __init__(self):
    self.val = 0
  
  def change(self):
    self.val += int(1) # единственное отличие - операция преобразования типа

def conversion_count():
    threads_count = 10
    operations_per_thread_count = 1000000 
    expected_counter_value = threads_count * operations_per_thread_count
    counters = [CounterWithConversion()]
    
    for counter in counters:
      run_threads(counter, threads_count, operations_per_thread_count)
      print(f"{counter.__class__.__name__}: expected val: {expected_counter_value}, actual val: {counter.val}")

stand_count()
conversion_count()

