class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.values = []

    def _swap(self, index_1, index_2):
        self.values[index_1], self.values[index_2] = self.values[index_2], self.values[index_1]

    def _bubble_up(self):
        node_index = len(self.values) - 1
        node = self.values[node_index]

        while node_index > 0:
            parent_index = round((node_index - 1) / 2)
            parent = self.values[parent_index]

            if node.priority > parent.priority:
                break

            self._swap(node_index, parent_index)
            node_index = parent_index

        return

    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.values.append(node)
        self._bubble_up()
        return self.values

    def sink_down(self):
        current_index = 0
        heap_length = len(self.values)
        element = self.values[0]

        while True:
            left_child_index = 2 * current_index + 1
            right_child_index = 2 * current_index + 2
            swap = None

            if left_child_index < heap_length:
                left_child = self.values[left_child_index]
                if left_child.priority < element.priority:
                    swap = left_child_index

            if right_child_index < heap_length:
                right_child = self.values[right_child_index]
                if (swap is None and right_child.priority < element.priority) or (
                        swap is not None and right_child.priority < left_child.priority):
                    swap = right_child_index

            if swap is None:
                break

            self._swap(current_index, swap)
            current_index = swap
            element = self.values[current_index]

        return

    def dequeue(self):

        if not self.values:
            return None

        max_value = self.values[0]
        end = self.values.pop()

        if self.values:
            self.values[0] = end
            self.sink_down()
        return max_value.value

    def __str__(self):
        return str([(node.value, node.priority) for node in self.values])

er = PriorityQueue()

print(er.enqueue("common cold", 5))
print(er.enqueue("gunshot wound", 1))
print(er.enqueue("high fever", 4))
print(er.enqueue("broken arm", 2))
print(er.enqueue("glass in foot", 3))

print(er.__str__())
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())
print(er.dequeue())


