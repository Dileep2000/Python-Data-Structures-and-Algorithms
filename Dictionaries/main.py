class Dictionary:
    '''
      A Dictionary is a collection which is unordered, changeable and indexed.
      Key value pair. Miller: a person who works or own a mill
      dict = {'name': 'John', 'age': 18, 'gender': 'male'}
      dict['name'] - John
      Creating a Dictionary
      dict() fuction gives an empty dictionary initalized
      {} also initalizes dictionary
      Time - O(1)
      Space - O(n)
      Dictionaries in Memory
      A hash table is a way of doing key-value lookups. You store the values in an array abd then use a hash function ti find the index of the array cell that corresponds to your key-value pair.Key array and hash function.

      Insert/Update an element in the dictionary
      dict['key'] = 'value' It will update if the key already exists or adds the new key value to the dictionary if it doesn't already exists.
      Time - O(1)

      Traversal
      Time - O(n)
      Space - O(1)

      Search
      Time - O(n)
      Space - O(1)

      Delete/Remove an element from the dictionary
      pop() - removes the element from the dictionary based on its key and returns the value
      popitem() - deletes random element from the dictionary and return key and value
      clear() - clears the dictionary
      del - deletes the Dictionary based on the key
      Time - O(1)-Average/Amoritized O(n)
      Space - O(1)

      Dictionary Methods:
      clear()
      cop()
      fromkeys(squence[],value) - new dictionary
      get(key,value)
      items()
      keys()
      popitem()
      setDefault(key,default_value)
      pop(key,default_value)
      values()
      update(other_dict)

      Dictionary operations/Built in Functions
      in operator - checks if key exists in the dictionary
      for operator - loop through dictionary
      all(dictionary) - If all elements in the dictionary are true
      any(dict)  - Empty/All values are false False others true
      len(dict) no of pairs in the dictionary
      sorted(dict,reverse,key)

      Dictionary                                   List
      Unordered                                    Ordered
      Access via keys                              Access via indes
      collection of key value pairs                collection of elements
      preffered when you have unique key values    Preffered when you have ordered data
      No duplicate members                         Allow duplicate members

      
    '''
    def __init__(self,name=None,age=None,gender=None):
        self.user_dict = {'name':name, 'age':age, 'gender':gender}
        print(self.user_dict)
    def update(self,key,value,dic):
        dic[key]=value
    def add(self,key,value,dic):
        dic[key]=value
    def traverse(self,dic):
        for key in dic:
            print(key,dic[key])
        for key,value in dic.items():
            print(key,value)
    def find(self,dic,val):
        for key in dic:
            if val == dic[key]:
                return key,dic[key]
        return None
    def removes(self,dic,key):
        return dic.pop(key)
    def remove(self,dic):
        return dic.popitem()
    def clear(self,dic):
        dic.clear()
    def deletes(self,dic,key):
        del dic[key]
    
if __name__ == '__main__':
    dictionary = Dictionary('Dileep',22,'Male')