from collections import deque
import queue
from multiprocessing import Queue as multiqueue
class Queue:
    '''
      Collection Module
      Queue Module
      Multiprocessing Module

      The collections.deque class -> Double liinked list
      It is best for using queues
      Methods
      - deque()
      - append()
      - popleft()
      - clear()

      Queue Modal
      FIFO Queue - Queue(maxsize = 0)
      LIFO Queue - Stack
      Priority Queue 

      Methods
      - qsize()
      - empty()
      - full()
      - put()
      - get()
      -task_done()
      - join()

      Multiprocessing Module
      multiprocessing.Queue()
    '''
    def __init__(self) -> None:
        self.collectionQueue = deque(maxlen=3)
        self.collectionQueue.append(1)
        self.collectionQueue.append(2)
        self.collectionQueue.append(3)
        self.collectionQueue.append(4)
        print(self.collectionQueue.popleft())
        self.collectionQueue.clear()
        print(self.collectionQueue)

        self.queueModal = queue.Queue(maxsize=3)
        print(self.queueModal.empty())
        self.queueModal.put(1)
        self.queueModal.put(2)
        self.queueModal.put(3)
        print(self.queueModal.empty())
        print(self.queueModal.full())
        print(self.queueModal.get())
        print(self.queueModal.qsize())

        self.multiQueue = multiqueue(maxsize=3)
        self.multiQueue.put(1)
        print(self.multiQueue.get())


if __name__ == '__main__':
    queue = Queue()