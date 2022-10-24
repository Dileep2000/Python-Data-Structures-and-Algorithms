from sys import maxsize


class Queue:
    '''
      Creating Queues
      Enqueue
      Dequeue
      peek()
      delete()
      isEmpty()
      isFull()
      What is Queue:
      Queue us a data structure that stores items in First In/First Out manner.
      Example - Customers near reception of the sotre.
      A new addition to this queue hapens at the end of the queue
      First element in the queue will be served first
      FIFO method - First In First Out
      Front, End - Insert from end and Remove from the front
      Why do we need Queue?
      Utilize  first coming data first, while others wait to their turn
      FIFO method - First In First Out
      - Point sale syestem of a restaurant
      - Printer Queue
      - Call center phone systems
      Queue operations
      - Create Queue
      - Enqueuq
      - Dequeue
      - Peek
      - isEmpty
      - isFull
      - deleteQueue

      Implementation
      1. Python List
        - Queue without capacity
        - Queue with capacity(circular queue)
      2. Linked List
      
      Creating Queue using python list no capacity
      Queue with fixed capacity(circular queue)
    '''
    def __init__(self,maxSize = None):
        self.queue = []
    def __srt__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    def isEmpty(self):
        if self.queue == []:
            return True
        return False
    def enqueue(self,value):
        self.queue.append(value)
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue[0]
    def deleteQueue(self):
        self.queue = []
class CircularQueue:
    def __init__(self,maxSize):
        self.queue = [None]*maxSize
        self.maxSize = maxSize
        self.start =  -1
        self.top = -1
    def __srt__(self):
        values = [str(x) for x in self.queue]
        return ' '.join(values)
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
    def isFull(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top == self.maxSize:
            return True
        else:
            return False
    def enqueue(self,value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.queue[self.top] = value
        return "The element is inserted at end of queue"
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            first = self.queue[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.queue[start] = None
            return first
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queue[self.start]
    def deleteStack(self):
        self.queue = [None]*self.maxSize
        self.start = -1
        self.top = -1
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
class QueueLinkedList:
    def __init__(self):
        self.linkedList = LinkedList()
    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False
    def enqueue(self,value):
        node = Node(value)
        if self.linkedList.head is None:
            node.next = None
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            node.next = None
            self.linkedList.tail.next = node
            self.linkedList.tail = node
    def  dequeue(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            temp = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return  self.linkedList.tail
    def deleteStack(self):
        self.linkedList.head = None
        self.linkedList.tail = None