from xml.dom import minidom


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


def printXML(root, fileName):
    doc = minidom.Document()
    node = doc.createElement("root")
    node.setAttribute('value', str(root[1]))
    doc.appendChild(node)
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
    if 2*node < len(heap):
        printNode(2*node, child, doc)
    if 2*node + 1 < len(heap):
        printNode(2*node + 1, child, doc)


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
printXML(heap, "heap2.xml")
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
