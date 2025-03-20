def swap(collection: list[int], index1: int, index2: int):
    collection[index1], collection[index2] = collection[index2], collection[index1]
    return collection


def selection_sort(arr: list):
    end = len(arr)

    for i in range(end):
        current_min = arr[i]
        min_index = i
        for j in range(i, end):
            if arr[j] < current_min:
                current_min = arr[j]
                min_index = j
        swap(arr, i, min_index)
    return arr


if __name__ == "__main__":
    collection = [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]
    print(selection_sort(collection))
