from email import header
from tkinter.tix import Tree


class Stack:
    '''
      What is a Stack?
      Creating Stacks using Python lost7s and linked lists
      Operations(pi=ush,pop,peek,isEmpty,isFull)

      Stack is a data structure that stores items in a Last-In/First Out manner.
      Examples - Pile of plates, Pile of books etc
      LIFO method(Last In first Out)
      why do we need it?
      To use the data in LIFO way
      Stack Operations
      - create stack
      - push
      - pop
      - peek
      - isEmpty
      - isFull
      - deleteStack
      Creating stack using list without size Limit Time O(1) space - O(1)
      Stack using list
      - Easy to implement
      - Speed problems when it grows
      Stack using Linked list
      - Fast performance
      - Implementation is not easy
      Stack operations
      isEmpty - Time O(1) Space O(1)
      push - Time O(1) Space O(1)
      pop - Time O(1) Space O(1)
      peek - Time O(1) Space O(1)
      deleteStack - Time O(1) Space O(1)

      Stack with size limitations
      Isfull - Time O(1) Space O(1)
      push - Time O(1) Space O(1)

      Stack using Linked list
      Create
      - Create am object of linked list class
      push
      - create a blank node and reference to the head
      - if you want to add another value just add the value at the start of the linked list
      pop
      - remove fist element from the linked list
      peek
      - return the value at the head of the linked list
      isEmpty
      - if head is none return true else false
      deleteStack
      - head = none will remove the ref to the linked list
      All operations have O(1) sapce and time complexity

      When to use/avoid stack
      use
      - When you want to use LIFO functionality
      - The chance of data corroption is minimum
      Avoid
      - Random access is not possible
    '''
    def __init__(self, maxSize=None):
        self.maxSize = maxSize
        self.list = []
    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    def push(self,value):
        if self.maxSize:
            if len(self.list) == self.maxSize:
                return "Stack is full"
        else:
            self.list.append(value)
    def pop(self):
        if self.isEmpty():
            return "There is no element in the Stack"
        return self.list.pop()
    def peek(self):
        if self.isEmpty():
            return "There is no element in the Stack"
        return self.list[len(self.list)-1]
    def deleteStack(self):
        self.list = []
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        return False
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
class StackLinedList:
    def __init__(self):
        self.linkedList = LinkedList()
    def __str__(self):
        values = [str(x.value) for x in self.linkedList]
        return '\n'.join(values)
    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        return False
    def push(self,value):
        node = Node(value)
        node.next = self.linkedList.head
        self.linkedList.head = node
    def  pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            value = self.linkedList.head.value
            self.linkedList.head = self.linkedList.head.next
            return value
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.linkedList.head.value
    def deleteStack(self):
        self.linkedList.head = None