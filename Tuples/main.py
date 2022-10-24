class Tuple:
    '''
    What is Tuple
    A tuple is an immutable squence of python objects
    Tuples are also comparable and hashable
    Time - O(1)
    Space - O(n)

    Tuples in Memory
    Like arrays and list tuples are adjusted side by side in the memory location.
    Accessing Tuples
    tuple[index].tuple[start:end:step]
    Time - O(1)
    sapce - O(1)
    Traversal
    Time - O(n)
    space - O(1)
    Search
    In Operator
    Time - O(n)
    Sapce - O(1)
    Linear search - Time O(n), space O(1)
    index - Time O(n), space O(1)
    Tuple Operations and methods
    + : concatenation
    * : repeat add
    in: search
    count(): gives count of an element
    len(): gives the lenght of tuple
    max - gives maximum of the tuple
    min - gives mimimim of the tuple
    tuple - used to convert a list into tuple

    Tuple                                                                          List
    Immutable                                                                      Mutable
    We can reassign entire tuple but not change the elements in the tuple
    these methods cannot be used in tuple but list
    - append()
    - insert()
    - remove()
    - pop()
    - clear()
    - sort()
    - reverse()
    Tuples can be stored in Lists
    Lists can be stored in Tuples
    Both tuples and lists can be nested
    We generally ise tuples for hetrogeneous(different) data types and lists for homogenoues(similar) data types
    Iterating through a tuple is faster than with list
    Tuple that contain immutable elements can be used as a key for dictionary
    If you have data that doesn't change, implementing it as tuple will be  gurantee that it remains write-protected
    '''
    def __init__(self):
        self.tupl = tuple(('array','list','string'))
        self.tupl1 = 'a','b','c','d'
        self.tupl2 = ('a','b','c','d')
        self.tupl3 = (1,)
    def access(self,index,tup):
        assert index <= len(tup), "Index out of bounds"
        return tup[index]
    def trvesal(self,tup):
        for i in range(len(tup)):
            print(tup[i])

if __name__ == '__main__':
    tupl = Tuple()
    print(tupl.__doc__)