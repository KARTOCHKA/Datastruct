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

    """Удаляет из стека верхний элемент и возвращает данные удаленного экземпляра класса Node"""

    def pop(self):
        del_data = self.top
        self.top = self.top.next_node
        return del_data.data
