import bst
import random
import time
import matplotlib.pyplot as plt

numbers = random.sample(range(0, 30000), 10000)


def testInsertion():
    times = []
    for i in range(10):
        root = None
        start = time.perf_counter()
        for j in range(i*1000):
            root = bst.Insert(root, numbers[j])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testSearch():
    times = []
    root = None
    for i in range(len(numbers)):
        root = bst.Insert(root, numbers[i])
    for i in range(10):
        start = time.perf_counter()
        for j in range(i*1000):
            foundNode = bst.FindValue(root, numbers[j])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testDelete():
    times = []
    root = None
    for i in range(10):
        for j in range(len(numbers)):
            root = bst.Insert(root, numbers[j])
        start = time.perf_counter()
        for k in range(i*1000):
            root = bst.Delete(root, numbers[k])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


if __name__ == "__main__":
    bstInsertionTimes = testInsertion()
    bstSearchTimes = testSearch()
    bstDeleteTimes = testDelete()
    plt.plot(bstInsertionTimes)
    plt.title("Tworzenie drzewa")
    plt.xlabel("Liczba elementów (w tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["BST", "AVL"])
    plt.savefig("insertionPlot.png")
    plt.clf()
    plt.plot(bstSearchTimes)
    plt.title("Przeszukiwanie drzewa 10000 elementów")
    plt.xlabel("Liczba szukanych elementów (w tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["BST", "AVL"])
    plt.savefig("searchPlot.png")
    plt.clf()
    plt.plot(bstDeleteTimes)
    plt.title("Usuwanie elementów z drzewa 10000 elemetów")
    plt.xlabel("Liczba usuwanych elementów (w tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["BST", "AVL"])
    plt.savefig("deletePlot.png")
