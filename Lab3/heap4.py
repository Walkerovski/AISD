from xml.dom import minidom


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
    if 5 < len(root):
        printNode(5, node, doc, root)
    xml_str = doc.toprettyxml(indent='\t')
    with open(fileName, "w") as f:
        f.write(xml_str)


def printNode(node, parent, doc, heap):
    child = doc.createElement("child")
    child.setAttribute('value', str(heap[node]))
    parent.appendChild(child)
    if 4*node < len(heap):
        printNode(4*node, child, doc, heap)
    if 4*node + 1 < len(heap):
        printNode(4*node + 1, child, doc, heap)
    if 4*node + 2 < len(heap):
        printNode(4*node + 2, child, doc, heap)
    if 4*node + 2 < len(heap):
        printNode(4*node + 3, child, doc, heap)
