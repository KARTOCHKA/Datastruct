from classes import Node


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

    def dequeue(self):
        """Удаляет из очереди крайний левый элемент (первый добавленный)"""
        if self.head is None:
            return None
        # удаляемое значение
        deq_element = self.head
        # обновлени "хвоста"
        self.head = self.head.next_node

        return deq_element.data
