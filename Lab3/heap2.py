def insert(array, value):
    array.append(value)
    current = len(array) - 1
    while current != 0:
        if array[current] < array[current // 2]:
            array[current], array[current // 2] = array[current // 2], array[current]
        current //= 2


def remove(array):
    array[0] = array[-1]
    array.pop()
    if(len(array)):
        heapify(array, 0)


def heapify(array, index):
    temp = 1e18
    for i in range(1, 3):
        if(2 * index + i < len(array)):
            temp = min(temp, array[2 * index + i])

    if(temp < array[index]):
        for i in range(1, 3):
            if(2 * index + i < len(array)):
                if(array[2 * index + i] == temp):
                    array[index], array[2 * index + i] = array[2 * index + i], array[index]
                    heapify(array, 2 * index + i)
                    break
