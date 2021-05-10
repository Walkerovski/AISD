def insert(array, value):
    array.append(value)
    current = len(array) - 1
    while current != 0:
        if array[current] < array[current // 4]:
            array[current], array[current // 4] = array[current // 4], array[current]
        current //= 4


def remove(array):
    array[0] = array[-1]
    array.pop()
    if(len(array)):
        heapify(array, 0)


def heapify(array, index):
    temp = 1e18
    for i in range(1, 5):
        if(4 * index + i < len(array)):
            temp = min(temp, array[4 * index + i])

    if(temp < array[index]):
        for i in range(1, 5):
            if(4 * index + i < len(array)):
                if(array[4 * index + i] == temp):
                    array[index], array[4 * index + i] = array[4 * index + i], array[index]
                    heapify(array, 4 * index + i)
                    break
