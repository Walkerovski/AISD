def insert(array, value):
    array.append(value)
    current = len(array) - 1
    while array[current] < array[current//2]:
        array[current], array[current//2] = array[current//2], array[current]
        current //= 2


def remove(array):
    array[1] = array[len(array) - 1]
    array.pop()
    heapify(array, 1)


def heapify(array, index):
    if 2*index + 1 < len(array):
        if array[index] > array[2*index] or array[index] > array[2*index + 1]:
            if array[2*index] < array[2*index + 1]:
                array[index], array[2*index] = array[2*index], array[index]
                heapify(array, 2*index)
            else:
                array[index], array[2*index + 1] = array[2*index + 1], array[index]
                heapify(array, 2*index + 1)


heap = [-1]
insert(heap, 5)
insert(heap, 3)
insert(heap, 17)
insert(heap, 10)
insert(heap, 84)
insert(heap, 19)
insert(heap, 6)
insert(heap, 22)
insert(heap, 9)
print(heap)
remove(heap)
print(heap)
remove(heap)
print(heap)
remove(heap)
print(heap)
remove(heap)
print(heap)
remove(heap)
print(heap)
