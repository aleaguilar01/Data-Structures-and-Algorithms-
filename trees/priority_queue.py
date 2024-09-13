class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class priority_queue:
    def __init__(self):
        self.values = []

    def bubble_up(self):
        index = len(self.values) - 1
        element = self.values[index]

        while index > 0:
            parentIndex = round((index - 1)/2)
            parent = self.values[parentIndex]

            if element.priority <= parent.priority:
                break
            self.values[parentIndex] = element
            self.values[index] = parent
            index = parentIndex



    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.values.append(node)
        self.bubble_up()


    def sink_down(self):
        index = 0
        length = len(self.values)
        element = self.values[0]
        while True:
            left_child_index = (2*index) + 1
            right_child_index = (2 * index) + 2

    def dequeue(self):
        min = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0:
            self.values[0] = end
            self.sink_down()
        return min
