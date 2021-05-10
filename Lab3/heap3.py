from xml.dom import minidom


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


def printXML(root, fileName):
    doc = minidom.Document()
    node = doc.createElement("root")
    node.setAttribute('value', str(root[1]))
    doc.appendChild(node)
    if 2 < len(root):
        printNode(2, node, doc, root)
    if 3 < len(root):
        printNode(3, node, doc, root)
    if 4 < len(root):
        printNode(4, node, doc, root)
    xml_str = doc.toprettyxml(indent='\t')
    with open(fileName, "w") as f:
        f.write(xml_str)


def printNode(node, parent, doc, heap):
    child = doc.createElement("child")
    child.setAttribute('value', str(heap[node]))
    parent.appendChild(child)
    if 3*node < len(heap):
        printNode(3*node, child, doc, heap)
    if 3*node + 1 < len(heap):
        printNode(3*node + 1, child, doc, heap)
    if 3*node + 2 < len(heap):
        printNode(3*node + 2, child, doc, heap)
