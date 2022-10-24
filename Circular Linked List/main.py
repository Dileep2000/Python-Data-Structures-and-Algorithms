class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class CircularLinedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.tail.next:
                break
            node = node.next
    def create(self,value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL is created"
    def insert(self,value,location):
        if self.head is None:
            node = Node(value)
            node.next = node
            self.head = node
            self.tail = node
        else:
            node = Node(value)
            if location == 0:
                node.next = self.head
                self.head = node
                self.tail.next = node
            elif location == -1:
                node.next = self.tail.next
                self.tail.next = node
                self.tail = node
            else:
                index = 0
                temp = self.head
                while index < location -1 and temp.next != self.tail.next:
                    temp = temp.next
                    index += 1
                if temp.next == self.tail.next:
                    return self.insert(value,-1)
                next = temp.next
                temp.next = node
                node.next = next
    def traversal(self):
        node = self.head
        while node:
            print(node.value)
            node = node.next
            if node == self.tail.next:
                break
    def search(self,value):
        if self.head is None:
            return "There are no elements in linked list"
        else: 
            node = self.head
            while node:
                if node.value == value:
                    return "Found"
                node = node.next
                if node == self.tail.next:
                    break
            return "Not Found"
    def delete(self,location):
        if self.head is None:
            return "Linked List is Empty"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                    self.head.next = None
                else:
                    node = self.head
                    while node.next != self.tail:
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                index = 0
                node = self.head
                while index < location -1 and node.next != self.tail:
                    index += 1
                    node = node.next
                next = node.next
                node.next = next.next
    def clear(self):
        self.head = None
        self.tail.next = None
        self.tail = None
class Circualr:
    '''
      Creation of circular linked list
      Start -> Nodevalue -> Create Blank node, nodebalue = nodevalue -> node.next = node -> head = node;tail =node -> Terminate
      Time - O(1)
      Space - O(1)
      Insertion into Circular Linked List
      - Insert at the beginning of linked list
      - Insert at specified location of linked list
      - Insert at the end of the linekd list
      Algorithm:
      Node and location -> check linked? If no Terminate else create a node and assign value -> if location = first then newnode.next = head;head = newnode,tail.next = newnode ->terminate else if location = last -> newNode.next = tail.next;tail.next = newNode;tail = newNode -> terminate else loop to the location newnode.next = currentnode.next;currentNode.next = newNode -> Terminate
      Time - O(n) space - O(1)
      
      Traversal
      Time - O(n) space - O(1)
      Search
      Time - O(n) space - O(1)
      Delete
      - Delete the first node Time O(1) space O(1)
      - Delete any given node Time O(n) space O(1)
      - Delete the last node  Time O(1) space O(1)

      Algorithm
      location - If linked list is empty terminate else location = first if only one node in linked list them head = none;tail=none;first.next = null else head = first.next;tail.next = head terminate elif location = last then if only one node is present head = none;tail=none;first.next = null else find node before last node(loop) tail = currentNode;currentNode = head terminate else find location(loop) curent.next = nextNode.next terminate

      Clear Entire Circular Linked List
      Time - O(1)
      Space - O(1)
    '''
    def __init__(self):
        circular_linked_list = CircularLinedList()
        # circular_linked_list.create(1)
        circular_linked_list.insert(1,0)
        circular_linked_list.insert(2,1)
        circular_linked_list.insert(4,-1)
        circular_linked_list.insert(3,2)
        circular_linked_list.insert(5,10)
        # circular_linked_list.traversal()
        # print(circular_linked_list.search(3))
        circular_linked_list.delete(0)
        circular_linked_list.delete(-1)
        circular_linked_list.delete(1)
        circular_linked_list.delete(10)
        print([node.value for node in circular_linked_list])
if __name__ == '__main__':
    circualr = Circualr()