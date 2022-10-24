class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def create(self,value):
        node = Node(value)
        node.next = None
        node.prev = None
        self.head = node
        self.tail = node
    def insert(self,value,location):
        node = Node(value)
        if self.head is None:
            node.next = None
            node.prev = None
            self.head = node
            self.tail = node
        else:
            if location == 0:
                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head = node
            elif location == -1:
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            else:
                index = 0
                temp = self.head
                while temp.next != None and index < location -1:
                    temp = temp.next
                    index += 1
                if temp.next is None:
                    self.insert(value,-1)
                else:
                    node.next = temp.next
                    node.prev = temp
                    node.next.prev = node
                    temp.next = node
    def traverse(self):
        if self.head is None:
            print("There are no elements in Doubly Linked List")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
    def reverseTraversal(self):
        if self.tail is None:
            print("There are no elements in the Doubly linked list")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
    def search(self,value):
        if self.tail is None:
            print("There are no elements in the Doubly linked list")
            return -1
        else:
            node = self.tail
            while node:
                if node.value == value:
                    return 1
                node = node.prev
            return -1
    def delete(self,location):
        if self.head is None:
            return "There are no elements in the Doubly Linked List to Delete"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                node = self.head
                index = 0
                while index < location -1 and node.next is not None:
                    index += 1
                    node = node.next
                if node.next is None:
                    self.delete(-1)
                else:
                    node.next = node.next.next
                    node.next.prev = node
    def clear(self):
        if self.head is None:
            print("The Linked list is empty")
        else:
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None
class DoubleLink:
    '''
      Creating a Doubly Linked List
      Start -> nodeValue -> Create blank node;nod.value = nodeValue -> node.next = Null-;node.prev = Null --> head = node tail = node -> terminate
      Time O(1) Space O(1)
      Insertion
      - Insertion at the beginning of the linked list  Time - O(1) Space - O(1)
      - Insertion at the end of the linked list Time - O(1) Space - O(1)
      - Insertion at the any position of the linked list Time - O(n) space - O(1)
      Alogrithm
      nodeValue,location -> check head if no terminate else create new node, assign value -> location = first if yes newNode.prev = None; newNodw.next = head; head.prev = newNode;head=newNode -> terminate else if location - last newNode.next = null;newNode.prev = tail;tail.next = newNode;tail=newNode else find location -1(loop) newNode.next = currentNode.next;newNode.prev = currentNode;newNode.next.prev = newNode;currentNode.next = newNode

      Traversal
      Time - O(n)
      Space - O(1)
      Reverse Traversal
      Time - O(n)
      Space - O(1)
      Search
      Time - O(n)
      Space - O(1)

      Deletion
      Delete first element in the Doubly linked list Time O(1) space O(1)
      Delete last element in the Doubly linked list Time O(1) space O(1)
      Delete any element in the Doubly linked list Time O(n) space O(1)

      Algorithm
      location -> if head is none -> terminate else if location = first then if only one element head=tail=None head = head.next;head.prev = null -> terminate else if location = last if only one element head = tail = none else tail=tail.prev;tail.next = null -> terminate else find location-1(loop) currNode.next = currNode.next.next;currNode.next.prev = currNode -> terminate

      Deletion of entire List
      Time O(n)
      Space O(1)
    '''
    def __init__(self):
        doublyLinkedList = DoublyLinkedList()
        doublyLinkedList.insert(1, 0)
        doublyLinkedList.insert(2, 1)
        doublyLinkedList.insert(4, -1)
        doublyLinkedList.insert(3, 2)
        # doublyLinkedList.traverse()
        # doublyLinkedList.reverseTraversal()
        # print(doublyLinkedList.search(2))
        doublyLinkedList.delete(0)
        doublyLinkedList.delete(-1)
        doublyLinkedList.delete(2)
        doublyLinkedList.delete(1)
        print([node.value for node in doublyLinkedList])
if __name__ == '__main__':
    double = DoubleLink()