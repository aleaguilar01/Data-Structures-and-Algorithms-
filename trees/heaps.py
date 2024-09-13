class MaxBinaryHeap:
    def __init__(self):
        self.values = [41, 39, 33, 18, 27, 12]

    def bubble_up(self):
        index = len(self.values) - 1
        element = self.values[index]
        while True:
            parent_index = round((index - 1) / 2)
            parent = self.values[parent_index]
            if element <= parent:
                return self.values
            self.values[index] = parent
            self.values[parent_index] = element
            index = parent_index
    def insert(self, value):
        self.values.append(value)
        return self.bubble_up()

    def sink_down(self):
        parent_index = 0
        parent = self.values[parent_index]
        left_child_index = (2 * parent_index) + 1
        right_child_index = (2 * parent_index) + 2

        while left_child_index < len(self.values) and right_child_index < len(self.values):

            left_child = self.values[left_child_index]
            right_child = self.values[right_child_index]

            largest_node = max(parent, left_child, right_child)

            if largest_node == parent:
                return self.values
            if largest_node == left_child:
                temp = left_child
                self.values[left_child_index] = parent
                self.values[parent_index] = temp
                parent = self.values[left_child_index]
                parent_index = left_child_index
            else:
                temp = right_child
                self.values[right_child_index] = parent
                self.values[parent_index] = temp
                parent = self.values[right_child_index]
                parent_index = right_child_index

            left_child_index = (2 * parent_index) + 1
            right_child_index = (2 * parent_index) + 2



    def remove(self):
        max_value = self.values[0]
        self.values[0] = self.values[len(self.values)-1]
        self.values.pop()
        self.sink_down()
        print(self.values)
        return max_value




heap = MaxBinaryHeap()

print(heap.values)
print(heap.insert(55))
print(heap.insert(1))
print(heap.insert(45))
print(heap.remove())
print(heap.remove())
print(heap.insert(600))

