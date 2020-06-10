import unittest

from queue import Queue


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.q = Queue()

    def test_len_returns_0_for_empty_queue(self):
        self.assertEqual(len(self.q), 0)

    def test_len_returns_correct_length_after_enqueue(self):
        self.assertEqual(len(self.q), 0)
        self.q.enqueue(2)
        self.assertEqual(len(self.q), 1)
        self.q.enqueue(4)
        self.assertEqual(len(self.q), 2)
        self.q.enqueue(6)
        self.q.enqueue(8)
        self.q.enqueue(10)
        self.q.enqueue(12)
        self.q.enqueue(14)
        self.q.enqueue(16)
        self.q.enqueue(18)
        self.assertEqual(len(self.q), 9)

    def test_empty_de_queue(self):
        self.assertIsNone(self.q.de_queue())
        self.assertEqual(len(self.q), 0)

    def test_de_queue_respects_order(self):
        self.q.enqueue(100)
        self.q.enqueue(101)
        self.q.enqueue(105)
        self.assertEqual(self.q.de_queue(), 100)
        self.assertEqual(len(self.q), 2)
        self.assertEqual(self.q.de_queue(), 101)
        self.assertEqual(len(self.q), 1)
        self.assertEqual(self.q.de_queue(), 105)
        self.assertEqual(len(self.q), 0)
        self.assertIsNone(self.q.de_queue())
        self.assertEqual(len(self.q), 0)


if __name__ == '__main__':
    unittest.main()
