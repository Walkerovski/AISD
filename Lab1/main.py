from Bubblesort import bubbleSort
from Countsort import Countsort
from Mergesort import Mergesort
from Quicksort import quickSort
import timeit
import matplotlib.pyplot as plt


def ReadFromFile(fileName, numOfCharacters):
    array = []
    f = open(fileName, "r")
    for character in f.read(numOfCharacters):
        array.append(character)
    f.close()
    return array


def TestBubblesort():
    bubblesortTime = {}
    for num in [1000, 2000, 3000, 4000, 5000, 6000, 6113]:
        text = ReadFromFile("lorem_ipsum.txt", num)
        tempTime = timeit.timeit(lambda: bubbleSort(text), number=1)
        bubblesortTime[num] = tempTime
    return bubblesortTime


def TestCountsort():
    countsortTime = {}
    for num in [1000, 2000, 3000, 4000, 5000, 6000, 6113]:
        text = ReadFromFile("lorem_ipsum.txt", num)
        tempTime = timeit.timeit(lambda: Countsort(text), number=1)
        countsortTime[num] = tempTime
    return countsortTime


def TestMergesort():
    mergesortTime = {}
    for num in [1000, 2000, 3000, 4000, 5000, 6000, 6113]:
        text = ReadFromFile("lorem_ipsum.txt", num)
        tempTime = timeit.timeit(lambda: Mergesort(text), number=1)
        mergesortTime[num] = tempTime
    return mergesortTime


def TestQuicksort():
    quicksortTime = {}
    for num in [1000, 2000, 3000, 4000, 5000, 6000, 6113]:
        text = ReadFromFile("lorem_ipsum.txt", num)
        tempTime = timeit.timeit(lambda: quickSort(text, 0, len(text)-1), number=1)
        quicksortTime[num] = tempTime
    return quicksortTime


if __name__ == "__main__":
    bubblesortTime = TestBubblesort()
    countsortTime = TestCountsort()
    mergesortTime = TestMergesort()
    quicksortTime = TestQuicksort()
    plt.plot(*zip(*bubblesortTime.items()))
    plt.plot(*zip(*countsortTime.items()))
    plt.plot(*zip(*mergesortTime.items()))
    plt.plot(*zip(*quicksortTime.items()))
    plt.title("Porównanie algorytmów sortowania")
    plt.xlabel("Długość tablicy")
    plt.ylabel("Czas potrzebny na sortowanie")
    plt.legend(["Bubblesort", "Countsort", "Mergesort", "Quicksort"])
    plt.savefig("plot.png")
