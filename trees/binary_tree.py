class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return
        else:
            current = self.root

            while True:
                if value == current.value:
                    return
                if value < current.value:
                    if current.left is None:
                        current.left = node
                        return
                    else:
                        current = current.left
                if value > current.value:
                    if current.right is None:
                        current.right = node
                        return
                    else:
                        current = current.right

    def search(self, value):
        if self.root is None:
            return None

        current = self.root

        while current:
            if current.value == value:
                return current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        return None
