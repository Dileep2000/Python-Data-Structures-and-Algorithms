from array import *
import numpy as np
class Array:
    """
      Array is most used data structure. An array is simply collection of objections ot things. Very power full data structure that store list of elements. end less applications.
      Properties:
      - Array can store data of specific type
      - Elements of array are located in a contiguous memory location
      - Each element of an array has a unique index
      - The size of array is predefined and connnot be modified
      An array is a data structure consisting of a collection of elements,each identified by at lease one array index or key. An array is stored such that position of each element can be computed from its index by a mathematical fromula.
      why do we need an array?
      3 varaibles easy to declare, but to store 500 values we cannot declare 500 variables. Then comes array to help. All the 500 varaibles can be stored in a array.

      Types of array
      One Dimensional - an array with a bunch of values haveing been declared with a single index
      a[i] -> i between 0 and n
      [1,2,3,4,5]
      Multi Dimensional
      Two Dimensional am array with a bunch of values having been decided with double index
      a[i][j] - i and j between 0 and n
      Arrays in memory
      one Dimensional
      [1,2,3,4,5]
      Memory
      stored in continuos location
      two Dimensional
      [[1,2,3],[4,5,6],[7,8,9]]
      Memory
      stored in continuos location
      three Dimensional
      [[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]],[[12,13,14]]]
      Memory
      stored in continuos location next to each other
      Create an array
      - Assign it to a variable
      - Define the type of elements that it will store
      - Define the size(Maximim number of elements)
      from array import *
      arr = array(typecode,[initializers])
      typecode  C Type              Python type   Mimimum Size in bytes  Notes
      'b'       Signed char         int           1
      'B'       Unsigned char       int           1
      'h'       signed short        int           2
      'H'       Unsigned short      int           2
      'i'       signed int          int           2
      'I'       Unsigned int        int           2
      'l'       signed long         int           4
      'L'       Unsigned long       int           4
      'q'       signed long long    int           8
      'Q'       Unsigned long long  int           8
      'f'       float               float         4
      'd'       double              float         8
      'u'       Py_UNICODE          Unicode character 2                     (1)
      Time - O(1)
      Space - O(n)
      Insertion
      arr[index] = value
      Insert at begenning
      Move all elements one to right and insert at start
      What if array is full
      we need to craete a new array and copy then perform the operation
      Time - O(N) at begenning or middle and O(1) at end
      Space - O(1)
      Traversal
      visiting all cells of array till the end
      for i in array:
        print(i)
      Time - O(N)
      space - O(1)
      Access array element
      How can we tell the computer which particular value we would like to access?
      Index - array[index]
      Time - O(1)
      Space - O(1)
      Finding an element
      Time - O(n)
      Space - O(1)
      Deletion of an element
      time - O(n)
      space - O(1)

      Arrays Practice
      1. Create an array amd traverse
      2. Access individaul elements through indexes
      3. Append any value to the array using append() method
      4. Insert value to the array using insert() method
      5. Extend python array using extend() method
      6. Add items from list into array using fromlist() method
      7. Remove any array element using remove() method
      8. Remove last array element using pop() method
      9. Fetch any element through its index using index() method
      10. Reverse a python array using reverse() method
      11. get attay buffer information through buffer_info() method
      12. check for number of occurances of an element using count() method
      13. convert array to string using tostring() method
      14. convert array to a python list with same elements using tolist() method
      15. Append a string to char array using fromstring() method
      16. Slice elements from an array
      Two Dimensional arrays
      numpy module
      Rows and columns
      arr[i][j]
      Create
      Time - O(1)
      Space - O(mn)
      Insertion
      Time - O(mn)/O(1)
      space - O(1)
      Accessing
      arr[row][column]
      time - O(1)
      space - O(1)
      Traversal
      Time - O(mn)
      sapce - O(1)
      Search
      Time - O(mn)
      Space - O(1)
      Delete
      Time - O(mn)
      space - O(1)

      When to use/avoid arrays
      use
      - To store multiple values of same data type
      - Random access
      Avoid
      - Same data type elements
      - Reserve memory
    """
    def __init__(self):
        self.arr = array('i',[1,2,3,4,5,6])
        print(self.arr)
        self.insertarr(0,0)
        self.trverse(self.arr)
        self.getelement(self.arr,4)
        self.search(self.arr,3)
    def insertarr(self,index,n):
        self.arr.insert(index,n)
        print(self.arr)
    def trverse(self,arr):
        for i in arr:
            print(i)
    def getelement(self,arr,index):
        assert index < len(arr), "index out of range"
        return arr[index]
    def search(self,arr,n):
        for i in arr:
            if i == n:
                return arr.index(i)
        return -1
    def delete(self,arr,value):
        return arr.remove(value)
    def practice(self):
        arr = array('i',[1,2,3,4,5,6,7,8,9,10])
        for i in arr:
            print(i)
        for i in range(0,len(arr)):
            print(arr[i])
        arr.append(11)
        arr.insert(11,12)
        arr.extend(array('i',[13,14,15]))
        arr.fromlist([16,17])
        arr.remove(17)
        arr.pop()
        arr.index(15)
        arr.reverse()
        arr.buffer_info()
        arr.count(1)
        arr.tostring()
        arr.tobytes()
        arr.tolist()
        arr.fromstring()
        arr[1:3]

if __name__ == '__main__':
    # array =Array()
    # print(array.__doc__)
    array2D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
    array2D = np.insert(array2D,1,[13,14,15,16],axis=1)
    array2D = np.insert(array2D,0,[17,18,19,20],axis=0)
    array2D = np.delete(array2D,0,axis=0)
    array2D = np.delete(array2D,1,axis=1)
    print(array2D)
    