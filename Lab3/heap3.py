def insert(array, value):
    array.append(value)
    current = len(array) - 1
    while current != 0:
        if array[current] < array[current // 3]:
            array[current], array[current // 3] = array[current // 3], array[current]
        current //= 3


def remove(array):
    array[0] = array[-1]
    array.pop()
    if(len(array)):
        heapify(array, 0)


def heapify(array, index):
    temp = 1e18
    for i in range(1, 4):
        if(3 * index + i < len(array)):
            temp = min(temp, array[3 * index + i])

    if(temp < array[index]):
        for i in range(1, 4):
            if(3 * index + i < len(array)):
                if(array[3 * index + i] == temp):
                    array[index], array[3 * index + i] = array[3 * index + i], array[index]
                    heapify(array, 3 * index + i)
                    break
