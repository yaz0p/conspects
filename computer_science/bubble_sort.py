'''Смысл сортировки пузырьком в том, что наибольшие значения "всплывают" наверх
   Сложность: O(n^2)
   Память: O(1)
'''
def swap(collection: list[int], index1: int, index2: int):
    collection[index1], collection[index2] = collection[index2], collection[index1]
    return collection


def bubble_sort(arr):
    end = len(arr)
    for i in range(end - 1):
        swapped = False

        for j in range(end - i - 1): # каждый шаг итерируемся на i элементов меньше, чтобы не делать лишнюю работу
            if arr[j] > arr[j + 1]: # поменяв знак равенства здесь можно поменять сортировку с desc на asc
                swap(arr, j, j + 1)
                swapped = True

        if not swapped:
            break

    return arr


if __name__ == "__main__":
    collection = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    print(bubble_sort(collection))
