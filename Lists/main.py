from array import *
class Lists:
    '''
      A list is a data structure that holds an ordered collection of items.
      list - [1,'name',[30,10]]
      nested list - list inside list
      Acessing Time - O(1) space - O(1)
      Traversal Time - O(n) space - O(1)
      lis[-1] : last item in list .....
      lis[1-n] : first item in list .....
      Insertion - Time O(n) space - O(1) -insert(),  Time O(1) space - O(1)append(),  Time O(1) space - O(n)extend()
      Updation - Time O(1) space - O(1)
      Delete - remove(value) Time O(n) space - O(1), pop(index) - returns the delted item if no index delete last Time O(1) space - O(1), del lis[index], dellis[index_start:index_end]
      reverse - reverse() Time O(n) space - O(1)
      slice - slice[:] start:end:step - end exclusive
      Search - IN operator - O(N) space - O(1), Linear search - Time O(N) space - O(1)
      List Operations/Functions
      + operator: concatenate lists
      * operator: multiplying list(repitative function)
      len: count the number of items in the list
      max: to get maximum of items in the list
      min: to get minimum of items in the list
      sum: to get sum of items in the list
      Strings and Lists
      str.split() return list of strings after splitting
      Common list pitfalls and ways to avoid them
      Read the documation of list functions carefully and see if it is returning null or an modified version of list
      Similarities
      Both data structures are mutable
      Both can be indexed and iterated through
      They can be both sliced

      Arthematice operstion
      array/2 works
      list/2 - Doesn't
      Data types
      array - only same data types
      list - any data types

      Small Array project
      Get the number of days temperature is recorded
      Get the temperature recorded every day
      Give the average and number of days temperature is above average
    '''
    def __init__(self):
      self.lis = [1,2,3,4]
      self.strings = ['milk','butter']
      self.nested = [1,2,[3,'nested']]
      self.lis.remove()
    def access(self, lis, key):
      assert key < len(lis), 'key out of bound'
      return lis[key]
    def traverse(self, lis):
      for i in lis:
        print(i)
    def exits(self,lis,search):
      if search in lis:
        return True
      return False
    def insert(self,lis,n):
      lis.insert(1,1)  
    def update(self,lis,index,value):
      assert index < len(lis), 'key out of bound'
      lis[index] = value
    def search(self,lis,search):
      if search in lis:
        return lis.index(search)
      return -1
    def linearSearch(self,lis,search):
      for i in lis:
        if i == search:
          return lis.index(search)
      return -1
    def concatenate(self,lis,lis1):
      return lis+lis1
    def repeat(self,lis,times):
      return lis*times
    def lenght(self,lis):
      return len(lis)
    def maximum(self,lis):
      return max(lis)
    def minimum(self,lis):
      return min(lis)
    def summing(self,lis):
      return sum(lis)
    def average(self,lis):
      return sum(lis)/len(lis)
    def listFromString(self,str):
      return list(str)
    
    def simpleProj(self):
      days = int(input('How many day\'s temperature?'))
      temp = array('f',[])
      for i in range(0,days):
        temp.append(float(input("Day", i+1,"\'s high temperature:")))
      average = sum(temp)/len(temp)
      days_above_average = len(filter(lambda x: x > average, temp))
      print("Average = ",average)
      print(days_above_average, "day(s) above average")
      
if __name__ == '__main__':
    lists = Lists()
    print(lists.__doc__)