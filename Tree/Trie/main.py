class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfString = False
class Trie:
  '''
    What is a trie?
    Creation of a trie
    Common operations on truie
    insertion in trie
    Deletion in trie
    Searching in trie

    What is a trie?
    A trie is a tree-based data structure that organizes information in hierachy
    properties
    - It is typically used to store or search stringss in a space and time efficient way.
    - Any node in trie can store non repetative multiple characters
    - Every node stores link og the next character of the string
    - Every node keep track of 'end of string'

    why we need trie?
    To solve many standard problems in efficient way
    - spell checker
    - Auto completion
              Map
    Characters | Link to trie node
                |
                |
                |
          End of string
    Common Operations on trie data structure
    - Creation of trie
    - Insertion in trie
    - Search for a string in trie
    - Deletion from trie

    Creation of trie
    Blank logical node
    Physically
              Map
    Characters | Link to trie node
               |
               |
               |
          End of string Yes/No
    Timr O(1) Space O(1)

    Insert a string in a Trie:
    Case 1: A Trie is Blank
    APP - 
        Dict                          Dict                      Dict                     Dict
    char    Link to trie         char    Link to trie      char    Link to trie     char    Link to trie
     A           ------->         p           ------->     p           ------->


     End of string - No           End of string - No       End of string - No       End of string - Yes
    Case 2: new String's prefix is common to anonther strings prefix
     - API
    Case 3: New string's prefix is already present as complete string
    - APIS
    case 4: String to be inserted is already present in Trie
    - APIS
    Time O(n) Sapce - O(n)

    Search for a string in Trie
    Case 1: String does not exist in Trie
    Return : Ther string does not exist in Trie
    Case 2: String exits in the Trie
    Return: True
    Case 3: String is a prefix of another string, but it does not exist in Trie
    Return: False
    Time O(n) Sapce - O(1)

    Delete a string from Trie
    Case 1: Some other prefix of string is asame as the one that we want to delete(API,APPLE)
    Case 2: The string is a prefix of another string(API,APIS)
    case 3: Other string is a prefix of the string(APIs,AP)
    case 4: Not any node depends on this string

    Practical use of Trie
    - Auto completion
    - spell checker
  ''' 
  def __init__(self):
    self.root = TrieNode()
  def insert(self, word):
    curr = self.root
    for i in word:
      ch = i
      node = curr.children.get(ch)
      if node is None:
        node = TrieNode()
        curr.children.update({ch:node})
      curr = node
    curr.endOfString = True
    print("Successfully Inserted")
  def search(self,search):
    curr = self.root
    for i in search:
      node = curr.children.get(i)
      if node is None:
        return False
      curr = node
    if curr.endOfString == True:
      return True
    else:
      return False
  def deleteWord(self,root,word,index):
    ch = word[index]
    curr = root.children.get(ch)
    canBeDeleted = False
    if len(curr.children) > 1:
      self.deleteWord(curr,word,index + 1)
      return False
    if index == len(word) - 1:
      if len(curr.children) >= 1:
        curr.endOfString = False
        return False
      else:
        root.children.pop(ch)
        return True
    if curr.endOfString == True:
      self.deleteWord(curr,word,index + 1)
      return False
    canBeDeleted = self.deleteWord(curr,word,index + 1)
    if canBeDeleted == True:
      root.children.pop(ch)
      return True
    else:
      return False
  def delete(self,word):
    if self.search(word):
      self.deleteWord(self.root,word,0)
      print("Deleted Successfully")
    else:
      print(word," is not there in the tire")
if __name__ == '__main__':
  trie = Trie()
  trie.insert("App")
  trie.insert("Appl")
  trie.delete("App")
  print(trie.search("App"))