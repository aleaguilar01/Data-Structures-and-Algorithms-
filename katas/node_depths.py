def treeTransversal(node, depth=0, sum=0):
    sum += depth
    if node.left is None and node.right is None:
        return sum

    if node.left:
        sum = treeTransversal(node.left, depth + 1, sum)
    if node.right:
        sum = treeTransversal(node.right, depth + 1, sum)
    return sum


def nodeDepths(root):
    return treeTransversal(root)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(4)
root.left.left.left = BinaryTree(8)
root.left.left.right = BinaryTree(9)
root.left.right = BinaryTree(5)
root.right = BinaryTree(3)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)
actual = nodeDepths(root)

print(actual)