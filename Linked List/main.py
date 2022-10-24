
class LinkedListBase:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def insert(self,value,location):
        node = Node(value)
        if self.head == None:
            self.head = node
            self.tail = node
        elif location == 0:
            node.next = self.head
            self.head = node
        elif location == -1:
            node.next = None
            self.tail.next = node
            self.tail = node
        else:
            temp = self.head
            index = 0
            while index < location - 1 and temp.next:
                temp = temp.next
                index += 1
            next = temp.next
            temp.next = node
            node.next = next
            if temp == self.tail:
                self.tail = node
    def traverse(self):
        if self.head is None:
            print("No data exists in Linked List")
        else:
            node = self.head
            while node.next is not None:
                print(node.value)
                node = node.next
    def search(self,value):
        if self.head is None:
            return ("Linked list is empty")
        else:
            node = self.head
            while node.next is not None:
                if node.value == value:
                    return node.value
                node = node.next
            return ("The value is not found in linked list")
    def delete(self,location):
        if self.head is None:
            print("The Linked list is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next.next != None:
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                node = self.head
                index = 0
                while index  < location -1:
                    node = node.next
                    index += 1
                next = node.next
                node.next = next.next
    def clear(self):
        if self.head is None:
            print("The Linked list is empty")
        else:
            self.head = None
            self.tail = None

class Node:
    def __init__(self,value=None) -> None:
        self.value = value
        self.next = None

class LinkedList:
    '''
      Linked list is a form of a sequntial collection and it does not have to be in order. A lined list is made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link.
      Head, Tail, Nodes and links
      Each node is independent
      If we need to access a node we need to traverse through all previos nodes
      node -data and reference

      Array VS Linkedlist
      Elements of linkedl list are independent objects
      Size of linked list is not predefined
      Insertion and removals in linked list are very efficient
      Random access - accessing an element is very efficient in arrays

      Different types of linked lists
      - Single linked list
      - Doubly linked list
      - Circular linked list
      - Circukar Doubly linked list

      Linked list in memory
      Not located continuously. They are stored randomly.

      Creation of Single linked lists
      - Create head and tail, initialize with null
      - Create a blank node and assign a value to it and reference to null
      - Link head and tail with these node
      Time - O(1)
      Space - O(n) based on the number of items in the linked list
      
      Insertion to linked list
      - At the beginning of the linked list Time - O(1) space - O(1)
      - After a node in the middle of lnked list Time - O(n) space - O(1)
      - At the end of the linked list Time - O(1) space - O(1)

      Insertion algorith
      (Node value,location)  -> create a node and assign value -> head = None? -Yes-> head = node tail = node -> Terminate
      -No-> Location = first -No-> location=last -No-> Find location(loop) current.next = node node.next = nextNode -> Terminate
      location = first -Yes-> node.next = head head = node -> Terminate
      location=lat -Yes-> node.next = null last.next = node tail = node -> Terminate

      Traversal
      Start -> check head -Yes-> Loop all nodes and print value -> Terminate
            -> check head -No-> Terminate
      Time - O(n) space - O(1)

      Search
      Start -> nodevalue -> check head -Yes-> if node.value == value if no repeat untill last node -> yes terminate. If head is not there terminate
      Time - O(1) Space - O(1)

      Delete
      - Deleting the first node Time O(1) Space O(1)
      - Deleting any given node Time O(N) space O(1)
      - Deleting the last node Time O(N) Space O(1)
      Algorithm
      location -> If no elements in Linked list -> Terminaten else if location = first -> if only one node head and tail = none else head = head.next. If delete last node -> if only one element present then head and tail = none else find node before last node(loop) beforelast.next= none and tail = brforelast. If delete in middle find location(loop) current.next = nextnode.
      
      Delete all elements in Linked list
      head = tail = none
      Time - O(1)
      Space - O(1)

      Time Complexity Array VS Linked List
      creation O(1) O(1)
      Insertion at 1st position O(1) O(1)
      Insertion at last position O(1) O(1)
      insertion at nth position O(1) O(n)
      Searching in unsorted data O(n) O(n)
      searching in sorted data O(logn) O(n)
      Traversing O(n) O(n)
      Deleting at 1st position O(1) O(1)
      Deleting at last position O(1) O(n)/O(1)
      Deleting at nth position O(1) O(n)
      Deleting an array/Linked list O(n) O(n)/O(1)
      Acessing nth element O(1) O(n)
    '''
    def __init__(self) -> None:
        linked_lsit_base = LinkedListBase()
        linked_lsit_base.insert(1,1)
        linked_lsit_base.insert(2,1)
        linked_lsit_base.insert(3,2)
        linked_lsit_base.insert(4,-1)
        linked_lsit_base.insert(5,10)
        linked_lsit_base.traverse()
        linked_lsit_base.delete(0)
        linked_lsit_base.delete(-1)
        linked_lsit_base.delete(1)
        linked_lsit_base.clear()
        print([node.value for node in linked_lsit_base])

if __name__ == '__main__':
    linked_lsit = LinkedList()
    # print(linked_lsit.__doc__)