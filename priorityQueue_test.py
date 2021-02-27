##############################
# Test file for Priority Queue
##############################

from priorityQueue import PriorityQueue
from priorityQueue import PQSort
import unittest
import random


# This Priority Queue returns the min instead of max element


# Main test_class

class TestPriorityQueue(unittest.TestCase):
    
    # Testing that everything works fine when
    # we create pqueue

    def test_create(self):
        pqueue = PriorityQueue()

        self.assertTrue(pqueue.isEmpty())
        self.assertEqual(pqueue.size(), 0)


    # Testing that everything works fine when
    # we insert elements in pqueue

    def test_push(self):
        main_list = []
        for i in range(0, 1000):
            main_list.insert(i, i)
        
        random.shuffle(main_list)

        pqueue = PriorityQueue()

        for i in range(0, 1000):
            pqueue.push(main_list[i], main_list[i])
            self.assertEqual(pqueue.size(), i+1)
            self.assertFalse(pqueue.isEmpty())

        self.assertEqual(pqueue.pop(), 0)
        self.assertEqual(pqueue.pop(), 1)


    # Testing that everything works fine when
    # we remove elements in pqueue

    def test_pop(self):
        main_list = []
        pqueue = PriorityQueue()

        for i in range(0, 1000):
            main_list.insert(i, i)
        
        random.shuffle(main_list)
        for i in range(0, 1000):
            pqueue.push(main_list[i], main_list[i])

        for i in range(999, -1, -1):
            self.assertEqual(pqueue.pop(), 999-i)
            self.assertEqual(pqueue.size(), i)


    # Testing that everything works fine
    # with update() function

    def test_update(self):
        main_list = []
        pqueue = PriorityQueue()

        for i in range(0, 1000):
            main_list.insert(i, i)

        random.shuffle(main_list)

        for i in range(0, 1000):
            pqueue.push(main_list[i], i)

        for i in range(0, 1000):
            pqueue.update(main_list[i], main_list[i])
            self.assertEqual(pqueue.size(), 1000)

        self.assertFalse(pqueue.isEmpty())
        # We can't check pqueue.update() with anything else
        

    # Testing PQsort() function

    def test_PQsort(self):
        main_list = []
        for i in range(0, 1000):
            main_list.insert(i, i)

        random.shuffle(main_list)

        main_list = PQSort(main_list)

        for i in range(0, 999):
            self.assertGreater(main_list[i+1], main_list[i])


# That way tests start to run

if __name__ == '__main__':
    unittest.main()
