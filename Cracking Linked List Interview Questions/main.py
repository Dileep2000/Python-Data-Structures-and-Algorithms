from LinkedList import *


class Questions:
    '''
      Question 1: Linked List class -> LinkedList.py file
      Question 2: Write code to remove duplicates from an unsorted linked list. - Time O(n) Space - O(n)
      Question 3: Implement an algorithm to find the nth to last element of a singly linked list. Time - O(n) Space - O(1)
      Question 4: write code to partion a linked list around a value x such that all nodes less than x comes before all nodes greater than equal to x. Time - O(n) Space - O(1)
      Question 5: You have two numbers represented by a linked list where each node contains a single digit. The digits are stored in reverse order such that 1's digit is ar the head of the list. write a function that adds the two numbers and return the sum as a linked list - Time O(max(m,n)) space - O(max(m,n))
      Question 6: Given two (singly) linkde lists, determine if the two lists intersect. Return the intersection node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first list is the exact same node(by reference) as the jth node of the second linked list, then they are intersecting - Time O(m+n) Space  O(1)
    '''
    def __init__(self):
        ll1 = LinkedList()
        ll1.add(7)
        ll1.add(1)
        ll1.add(6)
        ll2 = LinkedList()
        ll2.add(5)
        ll2.add(9)
        ll2.add(3)
        print(ll1)
        print(ll2)
        print(self.add(ll1,ll2))
        ll2.add(2)
        self.addSameNode(ll1,ll2,7)
        self.addSameNode(ll1,ll2,1)
        self.addSameNode(ll1,ll2,2)
        print(self.intersection(ll1,ll2))

    def add(self,linked_list1,linked_list2):
        ll1 = linked_list1.head
        ll2 = linked_list2.head
        ll3 = LinkedList()
        carry = 0
        while ll1 or ll2:
            res = carry
            if ll1:
                res += ll1.value
                ll1 = ll1.next
            if ll2:
                res += ll2.value
                ll2 = ll2.next
            ll3.add(int(res%10))
            carry = res / 10
        if carry != 0:
            ll3.add(int(carry))
        return ll3
    def intersection(self,ll1,ll2):
        if ll1.tail is not ll2.tail:
            return False
        len1 = len(ll1)
        len2 = len(ll2)
        linked_list1 = ll1.head
        linked_list2 = ll2.head
        if len1 > len2:
            diff = len1 - len2
            for i in range(0,diff):
                linked_list1 = linked_list1.next
        elif len2 > len1:
            diff = len2 - len1
            for i in range(0,diff):
                linked_list2 = linked_list2.next
        while linked_list1 is not linked_list2:
            linked_list1 = linked_list1.next
            linked_list2 = linked_list2.next
        return linked_list1
    def addSameNode(self,llA,llB,value):
        temp = Node(value)
        llA.tail.next = temp
        llA.tail = temp
        llB.tail.next = temp
        llB.tail = temp

if __name__ == '__main__':
    questions = Questions()