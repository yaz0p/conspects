# Связный список - динамическая структура данных. Элементы могут быть
# удалены или добавлены без необходимости в любой момент без
# необходимости переопределения структуры.
# Элементы связного списка хранятся в разных участках памяти и связаны
# друг с другом при помощи указателей

# Удаление и вставка элемента связного списка выполняется за O(1), но
# это в случае, если нам известно местоположение элемента списка.

# Поиск элемента списка линеен O(n), так как для доступа к элементу
# необходимо последовательно проходить от начала списка до нужного
# элемента


class Node(object):
    '''Некий элемент коллекции'''
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList(object):
    '''Моя имплементация связного списка'''
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return None
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return None
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return None
        prev.next = temp.next
        temp = None

    def display(self):
        element = self.head
        while element:
            print(f"{element.data} ")
            element = element.next


foo = LinkedList()
foo.append(1)
foo.append(2)
foo.append(3)
foo.display()
foo.remove(3)
foo.display()

# Таким образом я разобрал структуру данных связный список и понял
# как его реализовать. Так как удаление и вставка происходит за O(1),
# то связный список можно использовать в системах, где необходима
# частая вставка или удаление. Массив же нужно использовать в системах,
# где нужно часто получать доступ к элементам коллекции.
