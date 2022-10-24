import queue as qu
class Tree:
    '''
      A Tree is a non linear data structure with hirearchial relation between its elements without having any cycle, it is basically reversed from a real life tree.
      Hirearchie of drinks in a cafe.
      Driinks are two types Hot and Cold
      Hots drinks are two types Tea and coffee
      Tea has ttwo types - Green and black
      coffe have three types amjericano latte cappuccino
      Cold drinks are two types - Alchoholic and non-alchoholic
      alchoholic drinks are two types wine and beer
      non-alchoholic are two three types coke fanta and soda

      Properties
      - Represents hirearchial data
      - Each node has two components - data and a link to its sub category
      - Base category and sub categories under it

      why tree?
      - Quicker and Easier access to the data
      - Store Hierarchical data, like folader structure, organization structure, XML/HTML data
      - There are many types of data structures which performs better in various situatuions
        - Binary search tree, AVL, Read Black Tree, Trie
      
      Tree terminology
      Root - Top node with out parent
      Edge - A link between parent and child
      leaf - A node which doesnot have children
      sibling - children of same parent
      ancestor - parent,grandparent,great grandparent of a node
      Depth of node - a length of the path from root to node
      Heignt of the node - a length of the path from the node to depest node
      Defth of tree - depth of root node - it is always 0
      Height of tree - height of root node
      
      Binary Tree
      - Binary trees are the data structures in which each node has at most two children, offen refered to as the left and right children
      - Birany is a family data strucure(BST,Head tree,AVL,red black tree,Syntax tree)

      why binary tree?
      - Binary trees are a prerequisite for more advanced trees like BST, AVL, Red Black Trees
      - Huffman coding problem, heap priority problem and expression parsing problem can be solved efficiently using binary trees
      
      Types of Binary trees
      - Full binary tree : either 2 or 0 children
      - perffect binary tree : 2 childrens and have same level
      - complete binary tree
      - Balanced binary tree - all leafs have same depth

      How to create basic binary tree in python?
      - Linked list - data, left-child ref, right-child ref
      - Python list(array) - left child = cell[2X] right child = cell[2x+2]

      Creation of Binary tree using linked list
      - creation of tree Time and Sapce O(1)
      - insertion of a node
      - deletion of a node
      - search for a value
      - traverse all nodes
      - deletion of tree

      Traversal
      Depth First Search
      - PreOrder traversal
      - InOrder traversal
      - Post order traversal
      Breadth first search
      - Level order travesal

      Pre Order - Root node -> left subtree -> right subtree
      Time O(n) space - O(n)
      In order - left subtree -> root -> right subtree
      Time O(n) space - O(n)
      Post Order - left subtree -> right subtree -> root
      Time O(n) space - O(n)
      level order - traverse by level
      Time O(n) space - O(n)
      Search
      Use leavelorder traversal
      Time O(n) space - O(n)
      Insertion of a node
      - A root node is blank
      - The tree exisrs and we have to look for a first vacant place
      level order traversal
      Time O(n) space - O(n)
      
      Delete
      Replace the node to be deleted with the deepest node and then delete the deepest node
      Time O(n) space - O(n)

      Delete entire binary tree
      root = None
      root.left = None
      root.right = None
      Time O(1) space - O(1)

      Binary Tree using  List
      []
      index 1 - root node
      left child = cell[2X]
      right child = cell[2x+1]
      Creation - Time O(1) Space - O(n)
      Insertion
      - Bnary tree is full
      - We have to look for a fist vacant place
      Time O(1) Space - O(1)
      Search
      Linear search through list
      Time O(n) Space - O(1)
      Traversal
      - pre order Time O(n) Space - O(n)
      - in order Time O(n) Space - O(n)
      - post order Time O(n) Space - O(n)
      - level order - Time O(n) space O(1)
    Delete
    Time - O(N) Space - O(1)
    Delete entire binary tree
    Time - O(n) space - O(1)

    
    '''
class TreeNode:
  def __init__(self,value,children = []):
    self.value = value
    self.children = children
  def __str__(self,level=0):
    res = " " * level + str(self.value) + "\n"
    for child in self.children:
      res += child.__str__(level+1)
    return res
  def addChild(self,child):
    self.children.append(child)
class TreeNodeLinkedList:
  def __init__(self,value):
    self.value = value
    self.leftChild = None
    self.rightChild = None
class BinaryTree:
  def __init__(self,size):
    self.list_tree = size*[None]
    self.index = 0
    self.maxSize = size
  def insert(self,value):
    if self.index == self.maxSize:
      return "Binmary Tree is Full"
    else:
      self.list_tree[self.index + 1] = value
      self.index += 1
      return "Success"
  def search(self,value):
    for i in range(len(self.list_tree)):
      if value == self.list_tree[i]:
        return "Found"
    return "Not Found"
  def preOrderTraversal(self,index = 1):
    if index > self.index:
      return
    print(self.list_tree[index])
    self.preOrderTraversal(index*2)
    self.preOrderTraversal(index*2 + 1)
  def inOrderTraversal(self,index = 1):
    if index > self.index:
      return
    self.preOrderTraversal(index*2)
    print(self.list_tree[index])
    self.preOrderTraversal(index*2 + 1)
  def postOrderTraversal(self,index = 1):
    if index > self.index:
      return
    self.preOrderTraversal(index*2)
    self.preOrderTraversal(index*2 + 1)
    print(self.list_tree[index])
  def levelOrderTraversal(self):
    for i in range(1,self.index + 1):
      print(self.list_tree[i])
  def delete(self,value):
    if self.index == 0:
      return "Binary tree is empty"
    for i in range(1,self.index + 1):
      if self.list_tree[i] == value:
        self.list_tree[i] = self.list_tree[self.index]
        self.list_tree[self.index] = None
        self.index -= 1
        return "Success"
    return "Failed"
  def clear(self):
    for i in range(1,self.index + 1):
      self.list_tree[i] = None
    self.index = 0


if __name__=='__main__':
  tree = TreeNode('Drinks',[])
  cold = TreeNode('Cold',[])
  hot = TreeNode('Hot',[])
  tree.addChild(cold)
  tree.addChild(hot)
  fanta = TreeNode("Fanta",[])
  cola = TreeNode("Cola",[])
  tea = TreeNode("Tea",[])
  coffee = TreeNode("Coffee",[])
  hot.addChild(tea)
  hot.addChild(coffee)
  cold.addChild(fanta)
  cold.addChild(cola)
  # print(tree)
  
  binaryTree = TreeNodeLinkedList("Drinks")
  left = TreeNodeLinkedList("Hot")
  right = TreeNodeLinkedList("Cold")
  binaryTree.leftChild = left
  binaryTree.rightChild = right
  
  def preOrderTraversal(root):
    if root is None:
      return
    print(root.value)
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)
  # preOrderTraversal(binaryTree)
  def inOrderTraversal(root):
    if root is None:
      return
    inOrderTraversal(root.leftChild)
    print(root.value)
    inOrderTraversal(root.rightChild)
  # inOrderTraversal(binaryTree)
  def postOrderTravesal(root):
    if root is None:
      return
    postOrderTravesal(root.leftChild)
    postOrderTravesal(root.rightChild)
    print(root.value)
  # postOrderTravesal(binaryTree)
  def levelorderTraversal(root):
    if root is None:
      return
    else:
      queue = qu.Queue()
      queue.put(root)
      while not(queue.empty()):
        r = queue.get()
        print(r.value)
        if r.leftChild is not None:
          queue.put(r.leftChild)
        if r.rightChild is not None:
          queue.put(r.rightChild)
  # levelorderTraversal(binaryTree)
  def search(root,value):
    if root is None:
      return "No values in the tree"
    else:
      queue = qu.Queue()
      queue.put(root)
      while not(queue.empty()):
        r = queue.get()
        if r.value == value:
          return "Found"
        if r.leftChild is not None:
          queue.put(r.leftChild)
        if r.rightChild is not None:
          queue.put(r.rightChild)
    return "Not Found"
  # print(search(binaryTree,"Cold"))
  def insert(root,node):
    if not root:
      root = node
    else:
      queue = qu.Queue()
      queue.put(root)
      while not queue.empty():
        r = queue.get()
        if r.leftChild is not None:
          queue.put(r.leftChild)
        else:
          r.leftChild = node
          return
        if r.rightChild is not None:
          queue.put(r.rightChild)
        else:
          r.rightChild = node
          return
  insert(binaryTree,TreeNodeLinkedList("Tea"))
  insert(binaryTree,TreeNodeLinkedList("Coffee"))
  insert(binaryTree,TreeNodeLinkedList("Fanta"))
  insert(binaryTree,TreeNodeLinkedList("Cola"))
  # levelorderTraversal(binaryTree)
  def getDeepestNode(root):
    if not root:
      return
    else:
      queue = qu.Queue()
      queue.put(root)
      r = None
      while not queue.empty():
        r = queue.get()
        if r.leftChild is not None:
          queue.put(r.leftChild)
        if r.rightChild is not None:
          queue.put(r.rightChild)
      return r
  def deleteDeepestNode(root,node):
    if not root:
      return
    else:
      queue = qu.Queue()
      queue.put(root)
      while not queue.empty():
        r = queue.get()
        if r is node:
          r = None
      if r.rightChild:
        if r.rightChild is node:
          r.rightChild = None
          return
        else:
          queue.put(r.rightChild)
      if r.leftChild:
        if r.leftChild is node:
          r.leftChild = None
          return
        else:
          queue.put(r.leftChild)
  def delete(root,node):
    if not root:
      return
    else:
      queue = qu.Queue()
      queue.put(root)
      while not queue.empty():
        r = queue.get()
        if r.value == node:
          dele = getDeepestNode(root)
          r.value = dele.value
          deleteDeepestNode(root,dele)
          return "Success"
        if r.leftChild is not None:
          queue.put(r.leftChild)
        if r.rightChild is not None:
          queue.put(r.rightChild)
      return "Failed"
  # delete(binaryTree,'Hot')
  # levelorderTraversal(binaryTree)
  def clear(root):
    root.value = None
    root.leftChild = None
    root.rightChild = None
  
  binaryTreeList = BinaryTree(8)
  binaryTreeList.insert("Drinks")
  binaryTreeList.insert("Hot")
  binaryTreeList.insert("Cold")
  # print(binaryTreeList.search("Tea"))
  # binaryTreeList.preOrderTraversal()
  # binaryTreeList.inOrderTraversal()
  # binaryTreeList.postOrderTraversal()
  # binaryTreeList.levelOrderTraversal()
  binaryTreeList.delete("Hot")