class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def push_front(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.length += 1
        return self

    def pop_front(self):
        if self.length == 0:
            return None

        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        temp = self.head
        self.head = self.head.next
        self.length -= 1
        return temp

    def push_back(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def pop_back(self):
        if self.head is None:
            return None

        if self.head == self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp

        current = self.head
        while current.next.next:
            current = current.next
        temp = self.tail
        self.tail = current
        self.tail.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.head
        if index == self.length - 1:
            return self.tail

        counter = 0
        current = self.head
        while counter < self.length:
            if counter == index:
                return current
            else:
                current = current.next
                counter += 1

    def delete(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_front()

        if index == self.length-1:
            return self.pop_back()

        prev = self.get(index-1)

        prev.next = prev.next.next

    def reverse(self):
        if self.length == 0:
            return None
        if self.head == self.tail:
            return self

        prev = None
        current = self.head
        next = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next

        temp = self.head
        self.head = self.tail
        self.tail = temp
        self.tail.next = None
        return self






list = LinkedList()
list.push_back(1)
list.push_back(2)
list.push_back(3)
list.push_back(4)

print(list.get(0))
print(list.get(3))
print(list.get(1))