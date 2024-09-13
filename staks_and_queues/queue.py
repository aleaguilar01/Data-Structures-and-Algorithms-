class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)

        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        pop_node = self.first

        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            pop_node.next = None

        self.length -= 1

        return pop_node
