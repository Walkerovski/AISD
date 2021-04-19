import bst
import avl
import random
import time
import matplotlib.pyplot as plt
from xml.dom import minidom

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
    printXML(root, "bst.xml")
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
    for i in range(10):
        root = None
        for j in range(len(numbers)):
            root = bst.Insert(root, numbers[j])
        start = time.perf_counter()
        for k in range(i*1000):
            root = bst.Delete(root, numbers[k])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testAvlInsertion():
    times = []
    for i in range(10):
        tree = avl.Tree()
        root = None
        start = time.perf_counter()
        for j in range(i*1000):
            root = tree.add(root, numbers[j])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testAvlSearch():
    times = []
    root = None
    tree = avl.Tree()
    for i in range(len(numbers)):
        root = tree.add(root, numbers[i])
    for i in range(10):
        start = time.perf_counter()
        for j in range(i*1000):
            foundNode = tree.find(root, numbers[j])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def testAvlDelete():
    times = []
    for i in range(10):
        root = None
        tree = avl.Tree()
        for j in range(len(numbers)):
            root = tree.add(root, numbers[j])
        start = time.perf_counter()
        for k in range(i*1000):
            root = tree.delete(root, numbers[k])
        stop = time.perf_counter()
        times.append(stop-start)
    return times


def printXML(root, fileName):
    doc = minidom.Document()
    node = doc.createElement("root")
    node.setAttribute('value', str(root.value))
    doc.appendChild(node)
    if root.rChild is not None:
        printNode(root.rChild, node, doc)
    if root.lChild is not None:
        printNode(root.lChild, node, doc)
    xml_str = doc.toprettyxml(indent='\t')
    with open(fileName, "w") as f:
        f.write(xml_str)


def printNode(node, parent, doc):
    child = doc.createElement("child")
    child.setAttribute('value', str(node.value))
    parent.appendChild(child)
    if node.rChild is not None:
        printNode(node.rChild, child, doc)
    if node.lChild is not None:
        printNode(node.lChild, child, doc)


if __name__ == "__main__":
    bstInsertionTimes = testInsertion()
    bstSearchTimes = testSearch()
    bstDeleteTimes = testDelete()
    avlInsertionTimes = testAvlInsertion()
    avlSearchTimes = testAvlSearch()
    avlDeleteTimes = testAvlDelete()
    plt.plot(bstInsertionTimes)
    plt.plot(avlInsertionTimes)
    plt.title("Tworzenie drzewa")
    plt.xlabel("Liczba elementów (w tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["BST", "AVL"])
    plt.savefig("insertionPlot.png")
    plt.clf()
    plt.plot(bstSearchTimes)
    plt.plot(avlSearchTimes)
    plt.title("Przeszukiwanie drzewa 10000 elementów")
    plt.xlabel("Liczba szukanych elementów (w tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["BST", "AVL"])
    plt.savefig("searchPlot.png")
    plt.clf()
    plt.plot(bstDeleteTimes)
    plt.plot(avlDeleteTimes)
    plt.title("Usuwanie elementów z drzewa 10000 elemetów")
    plt.xlabel("Liczba usuwanych elementów (w tys.)")
    plt.ylabel("Czas (w sekundach)")
    plt.legend(["BST", "AVL"])
    plt.savefig("deletePlot.png")
