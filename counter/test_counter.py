"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):
    def test_same_object(self):
        c1 = Counter()
        c2 = Counter()
        c3 = Counter()
        self.assertIs(c1, c2)

        self.assertIs(c2, c3)

    def test_same_count(self):
        c1 = Counter()
        c1.increment()
        c2 = Counter()
        self.assertEqual(c1.count, c2.count)
        c2.increment()
        c3 = Counter()
        self.assertEqual(c2.count, c3.count)

    def test_new_count_not_reset_zero(self):
        pass
