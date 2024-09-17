class MaxBinaryHeap:
    def __init__(self):
        self.values = [41, 39, 33, 18, 27, 12]

    def _swap(self, index_1, index_2):
        self.values[index_1], self.values[index_2] = self.values[index_2], self.values[index_1]

    def _bubble_up(self):
        node_index = len(self.values) - 1
        node = self.values[node_index]
        parent_index = round((node_index - 1) / 2)
        parent = self.values[parent_index]

        while node > parent:
            self._swap(node_index, parent_index)
            node_index = parent_index
            parent_index = round((node_index - 1) / 2)
            node = self.values[node_index]
            parent = self.values[parent_index]

        return

    def insert(self, value):
        self.values.append(value)
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
                if left_child > element:
                    swap = left_child_index

            if right_child_index < heap_length:
                right_child = self.values[right_child_index]
                if (swap is None and right_child > element) or (swap is not None and right_child > self.values[left_child_index]):
                    swap = right_child_index

            if swap is None:
                break

            self._swap(current_index, swap)
            current_index = swap
            element = self.values[current_index]

        return

    def delete(self):

        if not self.values:
            return None

        max_value = self.values[0]
        end = self.values.pop()

        if self.values:
            self.values[0] = end
            self.sink_down()
        return max_value


heap = MaxBinaryHeap()

print(heap.insert(55))
print(heap.delete())
