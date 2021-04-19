class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class Tree(object):
    def add(self, root, key):
        if not root:
            root = Node(key)

        elif root.value > key:
            root.left = self.add(root.left, key)

        else:
            root.right = self.add(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.check_balance(root)

        # R L
        if balance < -1 and key < self.get_value(root.right):
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # R R
        if balance < -1 and key > self.get_value(root.right):
            return self.rotate_left(root)

        # L L
        if balance > 1 and key < self.get_value(root.left):
            return self.rotate_right(root)

        # L R
        if balance > 1 and key > self.get_value(root.left):
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        elif key < root.value:
            root.left = self.delete(root.left, key)

        elif key > root.value:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.getMinValueNode(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if root is None:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.check_balance(root)

        # L L
        if balance > 1 and self.check_balance(root.left) >= 0:
            return self.rotate_right(root)

        # R R
        if balance < -1 and self.check_balance(root.right) <= 0:
            return self.rotate_left(root)

        # L R
        if balance > 1 and self.check_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # R L
        if balance < -1 and self.check_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_value(self, root):
        if not root:
            return 0
        return root.value

    def check_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def getMinValueNode(self, root):
        if not root or not root.left:
            return root
        return self.getMinValueNode(root.left)

    # root
    #    new_root
    # new_root_baby
    def rotate_left(self, root):
        new_root = root.right
        new_root_baby = new_root.left

        new_root.left = root
        root.right = new_root_baby

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    #    root
    # new_root
    #    new_root_baby
    def rotate_right(self, root):
        new_root = root.left
        new_root_baby = new_root.right

        new_root.right = root
        root.left = new_root_baby

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))

        return new_root

    def find(self, root, key):
        if not root:
            return None
        if self.get_value(root) == key:
            return root
        if key > self.get_value(root):
            return self.find(root.right, key)
        if key < self.get_value(root):
            return self.find(root.left, key)

    def preOrder(self, root):

        if not root:
            print("{0} ".format("None"), end="")
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)


if __name__ == "__main__":
    Tree = Tree()
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]
    for x in nums:
        root = Tree.add(root, x)
    # Preorder Traversal
    print("Preorder visited nodes:")
    Tree.preOrder(root)
    print()

    # Delete
    key = 10
    root = Tree.delete(root, key)

    # Preorder Traversal
    print("Preorder visited nodes:")
    Tree.preOrder(root)
    print()
