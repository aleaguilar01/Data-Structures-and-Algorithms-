class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)

        if self.head == None:
            self.head = node
            return self

        current = self.head
        while True:
            if node.value < current.value:
                if current.left is None:
                    current.left = node
                    return self
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return self
                current = current.right

    def search(self, value):
        current = self.head

        while current is not None:
            if current.value == value:
                return current

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return None

    def transverse_top_to_bottom(self, node, values):
        values.append(node.value)
        if node.left is None and node.right is None:
            return

        if node.left:
            self.transverse_top_to_bottom(node.left, values)
        if node.right:
            self.transverse_top_to_bottom(node.right, values)



    def transverse_bottom_up(self, node, values):
        if node is None:
            return

        self.transverse_bottom_up(node.left, values)
        self.transverse_bottom_up(node.right, values)

        values.append(node.value)

    def deep_first_transversal(self, cb):
        current = self.head
        values = []

        cb(current, values)

        return values




tree = BinaryTree()

tree.add(12)
tree.add(15)
tree.add(8)
tree.add(150)
tree.add(0)
tree.add(27)
tree.add(36)
tree.add(20)


print(tree.deep_first_transversal(tree.transverse_top_to_bottom))
print(tree.deep_first_transversal(tree.transverse_bottom_up))





