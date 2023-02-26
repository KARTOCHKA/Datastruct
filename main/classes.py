class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    """Добавление в стек"""
    def push(self, data):
        node = Node(data)
        node.next_node = self.top
        self.top = node
