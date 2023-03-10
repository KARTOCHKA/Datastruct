from main.classes import Node


class LinkedList:
    """Класс односвязанный список"""

    def __init__(self):
        # хранит ссылку на начало списка
        self.head = None
        # хранит ссылку на конец списка
        self.tail = None

    def insert_beginning(self, data):
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node = Node(data)
        if self.head is None:
            # инициализация "хвоста" и "головы"
            self.head = node
            self.tail = node
        else:
            # обновление "головы"
            node.next_node = self.head
            self.head = node

    def insert_at_end(self, data):
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node = Node(data)
        if self.tail is None:
            # инициализация "хвоста" и "головы"
            self.head = node
            self.tail = node
        else:
            # обновление "хвоста"
            self.tail.next_node = node
            self.tail = node

    def print_ll(self):
        """Выводит в консоль данные из односвязанного списка:"""
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        return ll_string
