class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sumDeepFirstBT(tree, sum, data):
    sum += tree.value

    if tree.right is None and tree.left is None:
        data.append(sum)
        return

    if tree.right:
        sumDeepFirstBT(tree.right, sum, data)

    if tree.left:
        sumDeepFirstBT(tree.left, sum, data)


    print(sum, data)


tree = BinaryTree(12)
tree.value = 12
tree.right = BinaryTree(10)
tree.left = BinaryTree(15)
tree.left.right = BinaryTree(10)
tree.left.left = BinaryTree(15)

sumDeepFirstBT(tree, 0, [])