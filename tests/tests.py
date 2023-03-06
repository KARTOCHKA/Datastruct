from main.classes import Node, Stack
from main.custom_queue import Queue
import unittest


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
        self.stack.push('data1')
        self.stack.push('data2')
        self.stack.push('data3')
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)

    def test_stack_pop_add_data_one(self):
        self.stack.push('data1')
        data1 = self.stack.pop()
        self.assertEqual(data1, 'data1')
        self.assertEqual(self.stack.top, None)

    def test_stack_pop_add_data_two(self):
        self.stack.push('data1')
        self.stack.push('data2')
        data2 = self.stack.pop()
        self.assertEqual(data2, 'data2')
        self.assertEqual(self.stack.top.data, 'data1')


class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_queue(self):
        self.assertEqual(self.queue.head, None)
        self.assertEqual(self.queue.tail, None)

    def test_enqueue(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.head.data, 'data1')
        self.assertEqual(self.queue.tail.data, 'data3')
        self.assertEqual(self.queue.tail.next_node, None)

    def test_dequeue(self):
        self.queue.enqueue('data1')
        self.queue.enqueue('data2')
        self.queue.enqueue('data3')
        self.assertEqual(self.queue.dequeue(), 'data1')
        self.assertEqual(self.queue.dequeue(), 'data2')
        self.assertEqual(self.queue.dequeue(), 'data3')
        self.assertEqual(self.queue.dequeue(), None)
