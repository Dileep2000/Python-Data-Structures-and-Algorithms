class Questions:
    '''
      Question 1: Describe how you could use a single python liat to implement three stacks(3 in one)
      n-elements list
      For stack 1 - [0,n/3)
      For stack 2 - [n/3,2n/3)
      for stack 3 - [2n/3,n)
      Question 2: Stack min
      How would you design a stack which in addition to push and pop has a function min which retturns the minimum element?push,pop and min all operate in O(1)

      Question 3: Stack of plates
      Imagine a stack of plates. If the stack gets too high it might topple. Therefore in real life we would likely to start a new stack when the previos stack exceeds the threshold
      Implement a data structure setOfStacks that mimics this. setOfStacks should be composed of several stacks and should create a new stack once the previos one exceeds the capacity, setOfStacks.push() and setOfStacks.pop() should behave identically to a single stack(that is pop() should return the same values as it were just a single stack).
      Follow Up:
      Implement a function popAt(int index) which performs a pop operation on a specific sub - stack

      Question 4: Implement Queue class which implemnts a queue using two stacks
    '''
    def __init__(self,stackSize):
        self.stacks = 3
        self.list = [0]*(stackSize*self.stacks)
        self.sizes = [0]*self.stacks
        self.stackSize = stackSize
    def isFull(self,stack):
        if self.sizes[stack] == self.stackSize:
            return True
        return False
    def isEmpty(self,stack):
        if self.sizes[stack] == 0:
            return True
        return False
    def top(self,stack):
        offset = stack * self.stackSize
        return offset + self.sizes[stack] - 1
    def push(self,value,stack):
        if self.isFull(stack):
            return "Stack is Full"
        else:
            self.sizes[stack] += 1
            self.list[self.top(stack)] = value
    def pop(self,stack):
        if self.isEmpty(stack):
            return "Stack is Empty"
        else:
            value = self.list[self.top(stack)]
            self.list[self.top(stack)] = 0
            self.sizes[stack] -= 1
            return value
    def peek(self,stack):
        if self.isEmpty(stack):
            return "Stack is Empty"
        else:
            return self.list[self.top(stack)]
class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ',' + str(self.next)
        return string
class LinkedList:
    def __init__(self):
        self.head = None
class StackMin:
    def __init__(self):
        self.stack = LinkedList()
        self.minNode = None
    def min(self):
        if not self.minNode:
            return None
        return self.minNode.value
    def push(self,value):
        if self.minNode and (self.minNode.value < value):
            self.minNode = Node(self.minNode.value,self.minNode)
        else:
            self.minNode = Node(value,self.minNode)
        self.stack.head = Node(value,self.stack.head)     
    def pop(self):
        if not self.stack.head:
            return None
        self.minNode = self.minNode.next
        item = self.stack.head.value
        self.stack.head = self.stack.head.next
        return item
class Question3:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []
    def __str__(self):
        return self.stacks
    def push(self,value):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(value)
        else:
            self.stacks.append([value])
    def pop(self):
        while len(self.stacks) > 0 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
    def pop_at(self,stack):
        if len(self.stacks[stack]) > 0:
            return self.stacks[stack].pop()
        return None
class Stack:
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def push(self,value):
        self.list.append(value)
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
class Question4:
    def __init__(self):
        self.inStaclk = Stack()
        self.outStack  = Stack()
    def enqueue(self,value):
        self.inStaclk.push(value)
    def dequeue(self):
        while len(self.inStaclk):
            self.outStack.push(self.inStaclk.pop())
        res = self.outStack.pop()
        while len(self.outStack):
            self.inStaclk.push(self.outStack.pop())
        return res
class Question5:
    def __init__(self):
        self.cats = []
        self.dogs = []
    def enqueue(self,value,type='Dog'):
        if type == 'Cat':
            self.cats.append(value)
        self.dogs.append(value)
    def dequeuedog(self):
        if len(self.dogs) == 0:
            return None
        return self.dogs.pop()
    def dequeuecat(self):
        if len(self.cats) == 0:
            return None
        return self.cats.pop()
    def dequeuAny(self):
        if len(self.dogs) != 0:
            return self.dogs.pop()
        elif len(self.cats) != 0:
            return self.cats.pop()
        return None
if __name__ == '__main__':
    threeInOne =  Questions(6)
    print(threeInOne.isFull(0))
    print(threeInOne.isEmpty(1))
    print(threeInOne.isFull(2))
    threeInOne.push(1,0)
    threeInOne.push(2,1)
    threeInOne.push(3,2)
    print(threeInOne.peek(1))

    stackMin = StackMin()
    stackMin.push(11)
    print(stackMin.__getattribute__('minNode'))
    stackMin.push(10)
    stackMin.push(12)
    print(stackMin.min())
    stackMin.push(5)
    stackMin.push(4)
    stackMin.push(2)
    stackMin.push(20)
    print(stackMin.min())
    stackMin.pop()
    print(stackMin.min())

    multiStack = Question3(2)
    multiStack.push(1)
    multiStack.push(2)
    multiStack.push(3)
    multiStack.push(4)
    print(multiStack.pop())
    print(multiStack.stacks)
