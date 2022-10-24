class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    def create(self,value):
        node = Node(value)
        node.prev = node
        node.next = node
        self.head = node
        self.tail = node
    def insert(self,value,location):
        if self.head is None:
            node = Node(value)
            node.prev = node
            node.next = node
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            if location == 0:
                node.next = self.head
                node.prev = self.tail
                self.head.prev = node
                self.tail.next = node
                self.head = node
            elif location == -1:
                node.prev = self.tail
                node.next = self.head
                self.tail.next = node
                self.tail = node
                self.head.prev = node
            else:
                index = 0
                temp = self.head
                while index < location - 1:
                    temp = temp.next
                    index += 1
                if temp.next  == self.head:
                    self.insert(value,-1)
                else:
                    node.prev = temp
                    node.next = temp.next
                    temp.next.prev = node
                    temp.next = node
    def traverse(self):
        if self.head == None:
            print("There are no elements in the linked list")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break
    def reverseTraverse(self):
        if self.head == None:
            print("There are no elements in the linked list")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
                if node == self.head.prev:
                    break
    def search(self,value):
        if self.head == None:
            print("There are no elements in the linked list")
        else:
            node = self.head
            while node:
                if value == node.value:
                    return "Found"
                node = node.next
                if node == self.tail.next:
                    break
        return "Not Found"
    def clear(self):
        if self.head is None:
            print("There are no elements to delete in the Linked List")
        else:
            self.tail.next = None
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None
    def delete(self,location):
        if self.head is None:
            print("There are no elements to delete in the linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                node = self.head
                index = 0
                while index < location -1:
                    node = node.next
                    index += 1
                if node.next == self.head:
                    self.delete(-1)
                elif node.next == self.tail:
                    self.delete(-1)
                else:
                    node.next = node.next.next
                    node.next.prev = node
class CircularDouble:
    '''
      Create
      Time - O(1)
      Space - O(1)
      Algorithm -
      Start -> nodeValue -> Create a Blank node;node.value = nodeValue -> head = node;tail = node -> node.next = node;node.prev = node -> Terminate

      Insertion
      - Insertion at the beginning of the linked list - Time O(1) space O(1)
      - Insertion at the end of the linked list - Time O(1) space O(1)
      - Insertion at the middle of the linked list - Time O(n) space O(1)
      Algorithm
      Value,location -> if linked list is empty then create and insert into it else create newNode assign value -> location = first -> newNode.prev = tail;newNode.next = head;head.prev = newNode;head = newNode;tail.next = newNode -> terminate else if location == last -> newNode.next = head;newNode.prev = tail;tail.next = NewNode;head.prev = newNode;tail = newNode else loop to the location -1;newNode.prev = currNode;newNode.next = currNode.next;currNode.next = newNode;newNode.next.prev = newNode

      Traversal
      Time O(n)
      Space O(1)
      Reverse Traversal
      Time O(n)
      Space O(1)
      Search
      Time O(n)
      Space O(1)

      Delete
      - Delete first element of the linked list
      - Delete last element of the linked list
      - Delete any element of the linked list
      Algotihm
      start -> location -> If head is None -> Terminate else if location == first then if head == tail head.next = None;head.prev = None;head =None;tail=None else head=head.next;head.prev = tail;head.next = none -> terminate else if location == last then if head == tail head.next=none;head.prev=none;head=none;tail=none -> terminate else tail.prev.next = head;tail=tail.prev;head.prev = tail else find location - 1(loop) currNode.next = currNode.next.next;currNode.next.prev = currNode
      Delete enite lined list
      Time - O(n)
      Space - O(1)
    '''
    def __init__(self):
        circularDoublyLinkedList = CircularDoublyLinkedList()
        # circularDoublyLinkedList.create(1)
        circularDoublyLinkedList.insert(1,0)
        circularDoublyLinkedList.insert(2,-1)
        circularDoublyLinkedList.insert(3,-1)
        circularDoublyLinkedList.insert(4,3)
        # circularDoublyLinkedList.traverse()
        # circularDoublyLinkedList.reverseTraverse()
        # print(circularDoublyLinkedList.search(1))
        # print(circularDoublyLinkedList.search(10))
        circularDoublyLinkedList.delete(0)
        circularDoublyLinkedList.delete(-1)
        circularDoublyLinkedList.delete(1)
        print([node.value for node in circularDoublyLinkedList])
if __name__ == '__main__':
    circularDouble = CircularDouble()