from xml.dom import minidom


def insert(array, value):
    array.append(value)
    current = len(array) - 1
    while current != 0:
        if array[current] < array[current//3]:
            array[current], array[current//3] = array[current//3], array[current]
        current //= 3


def remove(array):
    array[0] = array[-1]
    array.pop()
    heapify(array, 0)


def heapify(array, index):
    if len(array) < 5 and index == 0:
        if 3*index + 3 < len(array):
            temp = min(array[3*index + 1], array[3*index + 2], array[3*index + 3])
            if array[index] > temp:
                if temp == array[3*index + 1]:
                    array[index], array[3*index + 1] = array[3*index + 1], array[index]
                    heapify(array, 3*index + 1)
                elif temp == array[3*index + 2]:
                    array[index], array[3*index + 2] = array[3*index + 2], array[index]
                    heapify(array, 3*index + 2)
                elif temp == array[3*index + 3]:
                    array[index], array[3*index + 3] = array[3*index + 3], array[index]
                    heapify(array, 3*index + 3)
    else:
        if 3*index + 2 < len(array):
            temp = min(array[3*index], array[3*index + 1], array[3*index + 2])
            if array[index] > temp:
                if temp == array[3*index]:
                    array[index], array[3*index] = array[3*index], array[index]
                    heapify(array, 3*index)
                elif temp == array[3*index + 1]:
                    array[index], array[3*index + 1] = array[3*index + 1], array[index]
                    heapify(array, 3*index + 1)
                elif temp == array[3*index + 2]:
                    array[index], array[3*index + 2] = array[3*index + 2], array[index]
                    heapify(array, 3*index + 2)


def printXML(root, fileName):
    doc = minidom.Document()
    node = doc.createElement("root")
    node.setAttribute('value', str(root[0]))
    doc.appendChild(node)
    if 1 < len(root):
        printNode(1, node, doc)
    if 2 < len(root):
        printNode(2, node, doc)
    if 3 < len(root):
        printNode(3, node, doc)
    xml_str = doc.toprettyxml(indent='\t')
    with open(fileName, "w") as f:
        f.write(xml_str)


def printNode(node, parent, doc):
    child = doc.createElement("child")
    child.setAttribute('value', str(heap[node]))
    parent.appendChild(child)
    if 3*node < len(heap):
        printNode(3*node, child, doc)
    if 3*node + 1 < len(heap):
        printNode(3*node + 1, child, doc)
    if 3*node + 2 < len(heap):
        printNode(3*node + 2, child, doc)


heap = []
insert(heap, 5)
insert(heap, 3)
insert(heap, 17)
insert(heap, 10)
insert(heap, 84)
insert(heap, 19)
insert(heap, 6)
insert(heap, 22)
insert(heap, 9)
printXML(heap, "heap3.xml")
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
