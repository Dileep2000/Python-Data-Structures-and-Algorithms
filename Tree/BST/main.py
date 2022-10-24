import queue as qu
class TreeNode:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
class BST:
    '''
      Binary Search Tree
      What is BST?
      - In the left subtree the value of a node is less than or equal to its parent node's value
      - In the right subtree the value of a node is greater than its parent node's value
      Common operations on binary search tree
      - creation of tree
      - insertion of a node
      - deletion of a node
      - search for a node
      - traversal all nodes
      - deletion of tree

      Creation of binary search tree
      Timne - O(1) Space - O(1)
      insertion
      Based on the defination of BST we need to insert a node
      Time -O(logn) space - O(logn)
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
      Time - O(logn) Space -O(logn)
      Delete a node from BST
      case 1 - The node to be deleted is a leaf node
      case 2 - The node has one child
      case 3 - The node has two children
      Time - O(logn) Space -O(logn)
      delete entire tree
      root.value = left child = right child = None
      Time - O(1) Space - O(1)
    '''
    def __init__(self):
        self.bst = TreeNode(None)
        self.insert(self.bst,70)
        self.insert(self.bst,50)
        self.insert(self.bst,90)
        self.insert(self.bst,30)
        self.insert(self.bst,60)
        self.insert(self.bst,80)
        self.insert(self.bst,100)
        self.insert(self.bst,20)
        self.insert(self.bst,40)
        self.insert(self.bst,60)
        # print(self.search(self.bst,60))
        self.delete(self.bst,100)
        self.levelorderTraversal(self.bst)
    def insert(self,root,value):
        if root.value is None:
            root.value = value
        elif value <= root.value:
            if root.leftChild is None:
                root.leftChild = TreeNode(value)
            else:
                self.insert(root.leftChild,value)
        else:
            if root.rightChild is None:
                root.rightChild = TreeNode(value)
            else:
                self.insert(root.rightChild,value)
    def preOrderTraversal(self,root):
        if root is None:
            return
        print(root.value)
        self.preOrderTraversal(root.leftChild)
        self.preOrderTraversal(root.rightChild)
    def postOrderTraversal(self,root):
        if root is None:
            return
        self.preOrderTraversal(root.leftChild)
        self.preOrderTraversal(root.rightChild)
        print(root.value)
    def inOrderTraversal(self,root):
        if root is None:
            return
        self.preOrderTraversal(root.leftChild)
        print(root.value)
        self.preOrderTraversal(root.rightChild)
    def levelorderTraversal(self,root):
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
    def search(self,root,search):
        if root.value == search:
            return True
        elif root.value < search:
            if root.rightChild.value == search:
                return True
            else:
                self.search(root.rightChild,search)
        else:
            if root.leftChild.value == search:
                return True
            else:
                self.search(root.leftChild,search)
    def minValue(self,root):
        curr = root
        while curr.leftChild is not None:
            curr = curr.leftChild
        return curr
    def delete(self,root,value):
        if root is None:
            return root
        else:
            if value < root.value:
                root.leftChild = self.delete(root.leftChild,value)
            elif value > root.value:
                root.rightChild = self.delete(root.rightChild,value)
            else:
                if root.leftChild is None:
                    temp = root.rightChild
                    root = None
                    return temp
                if root.rightChild is None:
                    temp = root.leftChild
                    root = None
                    return temp
                temp = self.minValue(root.rightChild)
                root.data = temp.data
                root.rightChild = self.delete(root.rightChild,temp.value)
        return root
    def clear(self,root):
        root.value = None
        root.leftChild = None
        root.rightChild = None
if __name__ == '__main__':
    bst = BST()