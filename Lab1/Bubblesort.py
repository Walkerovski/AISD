def read_from_file():
    f = open("lorem_ipsum.txt", "r")
    array = []
    for x in f.read():
        array.append(x)
    return(array)


def bubbleSort(series):
    for y in range(0, len(series)):
        for x in range(0, len(series)-1-y):
            if(series[x+1] < series[x]):
                series[x], series[x+1] = series[x+1], series[x]
    return series


if __name__ == "__main__":
    Input = read_from_file()
    sorted_series = bubbleSort(Input)
    print(sorted_series)
