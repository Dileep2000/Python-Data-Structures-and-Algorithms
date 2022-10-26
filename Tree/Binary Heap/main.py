class BinaryHeap:
    '''
      What is Binary Heap?
      Creation of Binary Heap
      Common operations on Binary Heap
      Insertion in Binary Heap
      Extraction from Binary Heap

      What is a Binary Heap
      A Binary Heap is a Binary tree with following properties
      - A binary head is either Min Heap or Max Heap. In a Min Binary Heap, the key at the root must be minimum among all keys present in Binary Heap. The same property must be recursively true for all nodes in Binart tree
      - It's a complete tree(All levels are completely filled except possibly the last level and the last level has all keys as left as possible). This property of Binary Heap makes them suitable to be stored in an array
      
      Why do we need a binary heap?
      Find the min or max number among a set of numbers in logN time. And also we want to make sure that inserting doesnot take more than O(logN) time.
      Possible solutions
      - Store the numbers in a sorted array
      Find Min O(1)
      Insert O(n)
      store the numbers in a sorted manner in linked listt
      Find Min O(1)
      Insert O(n)
      
      Practical Algorithm
      - Prim's algorithm
      - Heap Sort
      - Proprity Queue

      Types of binary heap
      Min Heap - the values of each node is less than or equal to the value of both its children
      max heap - it is exactly opposite of min heap that is value of each node is more than or equal to the value of both its children

      Common operations on binary heap
      - Creation of binary heap
      - peek top of binary heap
      - Extract Min ? Extract Max
      - Traversal of binary heap
      - Size of binary heap
      - Insert value in binary heap
      - Delete the entire binary heap
      Implemntaion options
      - Array Implementation
      - Reference/Pointer Implementation

      Creation of Binary heap

      initializer fixed sized list
      set size of binary heap to 0
      Time O(1) Space - O(n)

      peek of binary heap
      return list[1]
      Time O(1) Space - O(1)
      
      Size of binary heap
      Return number if filled cells
      Time O(1) Space - O(1)

      Tracversal of binary heap
      - pre order Time O(n) Space - O(n)
      - in order Time O(n) Space - O(n)
      - post order Time O(n) Space - O(n)
      - level order - Time O(n) space O(1)
    
      Insert a node in Binary Heap
      Time O(logN) space - O(logN)

      Extract a node from Binary Heap
      Time O(logN) space - O(logN)

      Delete entire Binary Heap
      Time O(1) Space - O(1)
    '''
    def __init__(self,size):
        self.heap = [None]*(size+1)
        self.heapSize = 0
        self.maxSize = size + 1
    def peek(self):
        if self.heapSize == 0:
            return
        return self.heap[1]
    def size(self):
        return self.heapSize
    def preOrderTraversal(self,index = 1):
        if index > self.heapSize:
            return
        print(self.heap[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
    def inOrderTraversal(self,index = 1):
        if index > self.heapSize:
            return
        self.preOrderTraversal(index*2)
        print(self.heap[index])
        self.preOrderTraversal(index*2 + 1)
    def postOrderTraversal(self,index = 1):
        if index > self.heapSize:
            return
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
        print(self.heap[index])
    def levelOrderTraversal(self):
        for i in range(1,self.heapSize + 1):
            print(self.heap[i])
    def heapify(self,index,type):
        parent = int(index/2)
        if index <= 1:
            return
        if type.lower() == "min":
            if self.heap[index] < self.heap[parent]:
                temp = self.heap[index]
                self.heap[index] = self.heap[parent]
                self.heap[parent] = temp
            self.heapify(parent, type)
        if type.lower() == "max":
            if self.heap[index] > self.heap[parent]:
                temp = self.heap[index]
                self.heap[index] = self.heap[parent]
                self.heap[parent] = temp
            self.heapify(parent,type)
    def insert(self,value,type):
        if self.heapSize + 1 == self.maxSize:
            return "Binary heap is full"
        self.heap[self.heapSize + 1] = value
        self.heapSize += 1
        self.heapify(self.heapSize,type)
    def extractify(self,index,type):
        left = index * 2
        right = index * 2 + 1
        swap = 0
        if self.heapSize < left:
            return
        elif self.heapSize == left:
            if type.lower() == "min":
                if self.heap[index] > self.heap[left]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left]
                    self.heap[left] =  temp
                return
            else:
                if self.heap[index] < self.heap[left]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[left]
                    self.heap[left] =  temp
                return
        else:
            if type.lower() == "min":
                if self.heap[left] < self.heap[right]:
                    swap = left
                else:
                    swap = right
                if self.heap[index] > self.heap[swap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swap]
                    self.heap[swap] =  temp
            else:
                if self.heap[left] > self.heap[right]:
                    swap = left
                else:
                    swap = right
                if self.heap[index] < self.heap[swap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[swap]
                    self.heap[swap] =  temp
            self.extractify(swap,type)
    def extract(self,type):
        if self.heapSize == 0:
            return
        else:
            extracted = self.heap[1]
            self.heap[1] = self.heap[self.heapSize]
            self.heap[self.heapSize] = None
            self.heapSize -= 1
            self.extractify(1,type)
            return extracted
    def claer(self):
        self.heap = self.maxSize*[None]
        self.heapSize = 0
if __name__ == '__main__':
    binaryHeap = BinaryHeap(10)
    binaryHeap.insert(4,'max')
    binaryHeap.insert(5,'max')
    binaryHeap.insert(2,'max')
    binaryHeap.insert(1,'max')
    binaryHeap.extract("max")
    binaryHeap.levelOrderTraversal()
