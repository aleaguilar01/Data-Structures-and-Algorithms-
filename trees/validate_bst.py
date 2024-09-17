# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    min_val = float("-inf")
    max_val = float("inf")

    def transverse(node, min_val, max_val):
        if node is None:
            return True

        if node.value >= max_val or node.value < min_val:
            print("value: ", node.value)
            print("max: ", max_val)
            print("min: ", min_val)
            return False

        return transverse(node.left, min_val, node.value) and transverse(node.right, node.value, max_val)

    return transverse(tree, min_val, max_val)


# Initialize the root node
root = BST(10)

# Set up the left subtree
root.left = BST(5)
root.left.left = BST(2)
root.left.left.left = BST(1)
root.left.right = BST(5)

# Set up the right subtree
root.right = BST(15)
root.right.left = BST(13)
root.right.left.right = BST(14)
root.right.right = BST(22)

print(validateBst(root))