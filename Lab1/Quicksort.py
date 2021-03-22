def read_from_file():
    # f = open("lorem_ipsum.txt", "r")
    # array = []
    # for x in f.read():
    #     array.append(x)
    # return(array)
    return([1,2,0,1,2,3,1231,32145,0])


def swap(series, a, b):
    series[a], series[b] = series[b], series[a]


def divide(series, l, r):
    split_position = l + (r - l) // 2
    value = series[split_position]
    swap(series, split_position, r)
    current_position = l
    for i in range(l, r - 1):
        if series[i] < value:
            swap(series, i, current_position)
            current_position += 1
    swap(series, current_position, r)
    return current_position


def quickSort(series, l, r):
    if l < r:
        i = divide(series, l, r)
        quickSort(series, l, i-1)
        quickSort(series, i+1, r)
    return series


if __name__ == "__main__":
    Input = read_from_file()
    sorted_series = quickSort(Input, 0, len(Input) - 1)
    print(sorted_series)
