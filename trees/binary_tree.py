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

    def deep_first_search(self):
        if self.root is None:
            return None

        data = []
        def transverse(node):
            data.append(node.value)
            if node.left is None and node.right is None:
                return

            if node.left:
                transverse(node.left)
            if node.right:
                transverse(node.right)

        transverse(self.root)
        return data

    def breadth_first_search(self):
        queue = []
        current = self.root
        queue.append(current)
        results = []

        while queue:
            current = queue[0]
            results.append(current.value)
            queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return results


def sum_all_nodes(node):
    if node is None:
        return 0

    return node.value + sum_all_nodes(node.left) + sum_all_nodes(node.right)


tree = BinarySearchTree()
tree.insert(12)
tree.insert(25)
tree.insert(120)
tree.insert(1)
tree.insert(39)
tree.insert(45)
tree.insert(50)
tree.insert(3)
tree.insert(5)
tree.insert(9)
tree.insert(2)

print(sum_all_nodes(tree.root))

print(tree.deep_first_search())
print(tree.breadth_first_search())