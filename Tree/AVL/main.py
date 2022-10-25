import queue as qu

class AVLNode:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.height = 1
class AVL:
    '''
      what is AVL trees?
      why AVL trees?
      creatio of AVL trees
      common operations on AVL trees
      Balancing of AVL trees
      Rotation of AVL trees

      what is AVL trees?
      An AVL tree is a self balnacing Binary Search Tree where the difference between hights of left and right subtrees cannot be more than one for all nodes in the tree.
      If at any time heights of left and right subtrees differe by more than one, then rebalancing is done to restore the AVL property, this process is called rotation

      why do we need AVL tree?
      If there are more numbers greater than root the  tree height becomes very long and searching and other operations are performed lower than expected so to overcome this difficulty AVL comes into picture

      commonn operations on AVL tree
      - Creation of AVL tree
      - search for a node in AVL tree
      - traversal of AVL tree
      - insertion of a node in AVL tree
      - deletion of a node in AVL tree
      - delete the entire AVL tree

      create a new AVL tree
      newAVL = AVL()
      rootNode = None
      leftChild = None
      rightChild = None
      Time - O(1) Space - O(1)
      
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
      Time O(logn) space - O(logn)

      Insert a node in AVL tree
      case 1: Rotation is not required
      case 2: Rotation is required

      Rotation is required
      LL - Left left comdition
      LR - Left right comdition
      RR  - Right right comdition
      RL - Right left comdition

      LL condiition
      Rignt rotation
      Alogrithm
      rightRotation(disbalancedNode):
        newRoot = disbalancedNode.leftChild
        disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
        newRoot.rightChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
      Time O(1) Space - O(1)

      LR condiition
      Left Rotation then
      Right Rotation
      Alogrithm
      Step 1: rotate left disabledNode.leftChild
      step 2: rotate right disabledNode
      rotateLeft(disbalancedNdoe):
        newRoot = disbalancedNdoe.rightChild
        disbalancedNdoe.rightChild = disbalancedNdoe.rightChild.leftChild
        newRoot.leftChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
      rightRotation(disbalancedNode):
        newRoot = disbalancedNode.leftChild
        disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
        newRoot.rightChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
      Time O(1) Space - O(1)

      RR condition
      Left Rotation
      Algorithm
      rotateLeft(disbalancedNdoe):
        newRoot = disbalancedNdoe.rightChild
        disbalancedNdoe.rightChild = disbalancedNdoe.rightChild.leftChild
        newRoot.leftChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
      Time O(1) Space - O(1)
      
      RL condition
      Right rotation then
      Left rotation
      AQlgorithm
      Step 1: rotate left disbalancedNode.leftChild
      step 2: rotate right disbalancedNode
      rightRotation(disbalancedNode):
        newRoot = disbalancedNode.leftChild
        disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
        newRoot.rightChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
      rotateLeft(disbalancedNdoe):
        newRoot = disbalancedNdoe.rightChild
        disbalancedNdoe.rightChild = disbalancedNdoe.rightChild.leftChild
        newRoot.leftChild = disbalancedNode
        update height of disbalancedNode and newRoot
        return newRoot
      Time O(1) Space - O(1)
      All together Insertion takes O(logn) space and time complexity

      Delete a node
      case 1: the tree does not exists
      case 2: Rotation is not required
      case 3: Rotation is required(LL,LR,RR,LL)
      All together Insertion takes O(logn) space and time complexity
      Delete entire AVL tree
      - Make the root, left child and right child to None
    '''
    def __init__(self):
        avl = AVLNode(5)
        avl = self.insert(avl,10)
        avl = self.insert(avl,15)
        avl = self.insert(avl,20)
        avl = self.delete(avl,15)
        self.levelorderTraversal(avl)
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
    def getHeight(self,root):
        if not root:
            return 0
        return root.height
    def rightRotate(self,root):
        new = root.leftChild
        root.leftChild = root.leftChild.rightChild
        new.rightChild = root
        root.height = 1 + max(self.getHeight(root.leftChild), self.getHeight(root.rightChild))
        new.height = 1 + max(self.getHeight(new.leftChild),  self.getHeight(new.rightChild))
        return new
    def leftRotate(self,root):
        new = root.rightChild
        root.rightChild = root.rightChild.leftChild
        new.leftChild = root
        root.height = 1 + max(self.getHeight(root.leftChild), self.getHeight(root.rightChild))
        new.height = 1 + max(self.getHeight(new.leftChild),  self.getHeight(new.rightChild))
        return new
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.leftChild) - self.getHeight(root.rightChild)
    def insert(self,root,value):
        if not root:
            return AVLNode(value)
        elif value <= root.value:
            root.leftChild = self.insert(root.leftChild,value)
        else:
            root.rightChild = self.insert(root.rightChild,value)
        root.height = 1 + max(self.getHeight(root.leftChild), self.getHeight(root.rightChild))
        balance = self.getBalance(root)
        if balance > 1 and value < root.leftChild.value:
            return self.rightRotate(root)
        if balance > 1 and value > root.leftChild.value:
            root.leftChild = self.leftRotate(root.leftChild)
            return self.rightRotate(root)
        if balance < -1 and value > root.rightChild.value:
            return self.leftRotate(root)
        if balance < -1 and value < root.rightChild.value:
            root.rightChild = self.rightRotate(root.rightChild)
            return self.leftRotate(root)
        return root
    def getMinimum(self,root):
        if root is None or root.leftChild is None:
            return root
        return self.getMinimum(root.leftChild)
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
                temp = self.getMinimum(root.rightChild)
                root.data = temp.data
                root.rightChild = self.delete(root.rightChild,temp.value)
        balance = self.getBalance(root)
        if balance > 1 and self.getBalance(root.leftChild) >= 0:
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.rightChild) <= 0:
            return self.leftRotate(root)
        if balance > 1 and self.getBalance(root.leftChild) < 0:
            root.leftChild = root.leftRotate(root.leftChild)
            return self.rightRotate(root)
        if balance < -1 and self.getBalance(root.rightChild) > 0:
            root.rightChild = root.rightRotate(root.rightChild)
            return self.leftRotate(root)
        return root
    def clear(self,root):
        root.value = None
        root.rightChild = None
        root.leftChild = None

if __name__ == '__main__':
    avl = AVL()