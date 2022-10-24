class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self,value = None):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)
    def __len__(self):
        res = 0
        node = self.head
        while node:
            res += 1
            node = node.next
        return res
    def add(self,value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        return self.tail
    
    def generate(self,n):
        self.head = None
        self.tail = None
        for i in range(n):
            n = int(input("Please Enter number: "))
            self.add(n)
        return self
    def removeDuplicates(self):
        if self.head == None:
            return 
        else:
            node = self.head
            temp = set([node.value])
            while node.next is not None:
                if node.next.value in temp:
                    node.next = node.next.next
                else:
                    temp.add(node.next.value)
                    node = node.next
        return self
    def nthToLast(self, n):
        if self.head == None:
            return None
        else:
            node = self.head
            node1 = self.head
            for i in range(n):
                if node1 is None:
                    return None
                node1 = node1.next
            while node1:
                node1 = node1.next
                node = node.next
            return node
    def partition(self,x:int):
        temp = self.head
        self.tail = self.head
        while temp:
            next = temp.next
            temp.next = None
            if temp.value < x:
                temp.next = self.head
                self.head = temp
            else:
                self.tail.next = temp
                self.tail = temp
            temp = next
        if self.tail.next is not None:
            self.tail.next = None

if __name__ == '__main__':
    customLinkedList = LinkedList()
    customLinkedList.generate(int(input("Please Enter the number of elements in Linked List: ")))
    print(customLinkedList)
    print(len(customLinkedList))
    customLinkedList.removeDuplicates()
    print(customLinkedList)
    print(customLinkedList.nthToLast(2))
    customLinkedList.partition(3)
    print(customLinkedList)