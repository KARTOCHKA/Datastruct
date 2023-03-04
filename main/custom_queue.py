class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    def __init__(self):
        # хранит ссылку на начало очереди
        self.head = None
        # хранит ссылку на конец очереди
        self.tail = None

    def enqueue(self, data):
        """Добавление элемента в очередь"""
        node = Node(data)
        if self.head is None:
            # инициализация "хвоста" и "головы"
            self.head = node
            self.tail = node
        else:
            # обновление "хвоста"
            self.tail.next_node = node
            self.tail = node
