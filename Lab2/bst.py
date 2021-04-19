class Node:
    def __init__(self, value):
        self.value = value
        self.lChild = None
        self.rChild = None


def Insert(node, value):
    if node is None:
        return Node(value)
    if value < node.value:
        node.lChild = Insert(node.lChild, value)
    if value >= node.value:
        node.rChild = Insert(node.rChild, value)
    return node


def FindValue(node, value):
    if node is None:
        return None
    if value == node.value:
        return node
    if value > node.value:
        return FindValue(node.rChild, value)
    if value < node.value:
        return FindValue(node.lChild, value)


def Delete(node, value):
    if node is None:
        return node
    if value < node.value:
        node.lChild = Delete(node.lChild, value)
    elif value > node.value:
        node.rChild = Delete(node.rChild, value)
    else:
        if node.lChild is None:
            temp = node.rChild
            node = None
            return temp

        elif node.rChild is None:
            temp = node.lChild
            node = None
            return temp
        temp = node.rChild
        while(temp.lChild is not None):
            temp = temp.lChild
        node.value = temp.value
        node.rChild = Delete(node.rChild, temp.value)
    return node
