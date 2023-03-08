from main.classes import Node, Stack
from main.custom_queue import Queue
from main.linked_list import LinkedList
import unittest


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_ll_init(self):
        self.assertEqual(self.ll.head, None)
        self.assertEqual(self.ll.tail, None)

    def test_insert_beginning(self):
        self.ll.insert_beginning({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})
        self.ll.insert_beginning({'id': 2})
        self.assertEqual(self.ll.head.data, {'id': 2})
        self.assertEqual(self.ll.tail.data, {'id': 1})

    def test_insert_at_end(self):
        self.ll.insert_at_end({'id': 1})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 1})

        self.ll.insert_at_end({'id': 69})
        self.assertEqual(self.ll.head.data, {'id': 1})
        self.assertEqual(self.ll.tail.data, {'id': 69})

    def test_print_ll(self):
        self.ll.insert_beginning({'id': 1})
        self.ll.insert_at_end({'id': 2})
        self.ll.insert_at_end({'id': 3})
        self.ll.insert_beginning({'id': 0})

        self.assertEqual(self.ll.print_ll(), " {'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node(69)

    def test_node_init(self):
        self.assertEqual(self.node.data, 69)
        self.assertEqual(self.node.next_node, None)

    def test_node_next_node(self):
        node2 = Node(1, self.node)
        self.assertEqual(node2.next_node, self.node)


class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_stack_init(self):
        self.assertEqual(self.stack.top, None)

    def test_stack_push(self):
        self.stack.push('test_data1')
        self.stack.push('test_data2')
        self.stack.push('test_data3')
        self.assertEqual(self.stack.top.data, 'test_data3')
        self.assertEqual(self.stack.top.next_node.data, 'test_data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'test_data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)

    def test_stack_pop_add_data_one(self):
        self.stack.push('test_data1')
        data1 = self.stack.pop()
        self.assertEqual(data1, 'test_data1')
        self.assertEqual(self.stack.top, None)

    def test_stack_pop_add_data_two(self):
        self.stack.push('test_data1')
        self.stack.push('test_data2')
        data2 = self.stack.pop()
        self.assertEqual(data2, 'test_data2')
        self.assertEqual(self.stack.top.data, 'test_data1')


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_queue(self):
        self.assertEqual(self.queue.head, None)
        self.assertEqual(self.queue.tail, None)

    def test_enqueue(self):
        self.queue.enqueue('test_data1')
        self.queue.enqueue('test_data2')
        self.queue.enqueue('test_data3')
        self.assertEqual(self.queue.head.data, 'test_data1')
        self.assertEqual(self.queue.tail.data, 'test_data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_dequeue(self):
        self.queue.enqueue('test_data1')
        self.queue.enqueue('test_data2')
        self.queue.enqueue('test_data3')
        self.assertEqual(self.queue.dequeue(), 'test_data1')
        self.assertEqual(self.queue.dequeue(), 'test_data2')
        self.assertEqual(self.queue.dequeue(), 'test_data3')
        self.assertEqual(self.queue.dequeue(), None)
