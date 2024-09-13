import random
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, value):
        node = Node(value)

        if self.root is None:
            self.root = node
            return

        current = self.root

        while True:
            choice = random.choice([True, False])

            if choice:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    def display(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.value))  # Indent by level
            self.display(node.left, level + 1, "L--- ")
            self.display(node.right, level + 1, "R--- ")


def max_branch_sum(tree):
    node = tree.root
    current_max = float("-inf")

    def transverse(node, current_max):

        if node.left is None and node.right is None:
            return node.value

        left_sum = float("-inf")
        right_sum = float("-inf")
        max_path = float("-inf")

        if node.left:
            left_sum = node.value + transverse(node.left, current_max)
        if node.right:
            right_sum = node.value + transverse(node.right, current_max)

        if left_sum > right_sum:
            max_path = left_sum
        else:
            max_path = right_sum

        print(max_path, node.value)

        if current_max < left_sum + right_sum - node.value:
            current_max = left_sum + right_sum - node.value

        return max_path
    transverse(node, current_max)
    return current_max


tree = Tree()

tree.add(10)
tree.add(50)
tree.add(100)
tree.add(-50)
tree.add(88)
tree.add(55)
tree.add(11)
tree.add(12)
tree.add(1)
tree.add(15)
tree.add(42)
tree.add(-3)


print(tree.display(tree.root))

print("here", max_branch_sum(tree))