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


root = None
root = Insert(root, 50)
root = Insert(root, 30)
root = Insert(root, 20)
root = Insert(root, 40)
root = Insert(root, 70)
root = Insert(root, 60)
root = Insert(root, 80)

foundNode = FindValue(root, 70)
print(foundNode.value, "\n", foundNode.lChild, foundNode.rChild)
