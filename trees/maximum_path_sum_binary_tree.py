class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_max_path(node):
    max_path = [float("-inf")]

    def helper(node):
        if node is None:
            return 0

        left_sum = max(helper(node.left), 0)
        right_sum = max(helper(node.right), 0)

        current_sum = node.value + left_sum + right_sum

        max_path[0] = max(max_path[0], current_sum)

        return node.value + max(left_sum, right_sum)

    helper(node)
    return max_path[0]


root = Node(-10)
root.left = Node(-2)
root.right = Node(-25)
root.left.left = Node(-20)
root.left.right = Node(-1)
root.right.left = Node(-3)
root.right.right = Node(-4)

max_sum = find_max_path(root)
print("Maximum Path Sum:", max_sum)