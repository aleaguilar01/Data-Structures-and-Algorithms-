# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        node = BST(value)
        current = self

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = node
                    return self
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return self
                else:
                    current = current.right

    def contains(self, value):
        current = self

        while current.value is not None:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False


