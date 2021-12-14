'''

Properties of  BT:
1. left child is less than root
2. right child is more than root

           L < Root < R

3. if tree inorder form comes into ascending order then it's BST.

types of binary tree:
check : https://www.youtube.com/watch?v=HqPJF2L5h9U&list=PLDN4rrl48XKpZkf03iYFl-O29szjTrs_O&index=32
1. full BT => every node should have either 2 children nodes or 0.
2. complete Bt  => if we represent BT in array then there should be no gaps between first and 
                    last element
3. perfect BT => every parent node must have 2 children nodes
4. Balanced BT => height of left subtree and right subtree must vary by atmost 1.

rules:

      if node is at index :  i (assuming starting index is 1)
      left child will be at : 2i
      right child  : 2i+1
      parent will be at : i/2 (floor value)
'''


class Node:
      def __init__(self, data):
            self.data = data
            self.llink = None
            self.rlink = None
            print("node with data {} is created".format(data))


class BinarySearchTree:
      def __init__(self):
            print("Binary Search Tree is initilized.....")
            self.root = None


      def insert(self, node):
            if self.root is None:
                  self.root = node
            else:
                  temp = self.root
                  self.insert_into_bst(temp, node)

      def insert_into_bst(self, head, node):
            if node.data < head.data:
                  if head.llink is None:
                        head.llink = node
                  else:
                        self.insert_into_bst(head.llink, node)
            else:
                  if head.rlink is None:
                        head.rlink = node
                  else:
                        self.insert_into_bst(head.rlink, node)
      
      def display(self):
            if self.root is None:
                  print("There is no data in Binary Serach Tree .......")
            else:
                  temp = self.root
                  self.display_tree(temp)

      def display_tree(self, head):
            ## inorder traversal

            if head.llink is not None:
                  self.display_tree(head.llink)
            print("{} --->".format(head.data))
            if head.rlink is not None:
                  self.display_tree(head.rlink)

      def search(self , key):
            if self.root is None:
                  print("TRee is empty..no point of searching")
            else:
                  temp = self.root
                  self.search_tree(key, temp)

      def search_tree(self, key, head):
            if head is not None:
                  print("this is head data : ", head.data)
                  if head.data == key:
                        print("{} is present in the tree !!".format(key))
                  else:
                        if key < head.data:
                              self.search_tree(key, head.llink)
                        else:
                              self.search_tree(key, head.rlink)
            else:
                  print("No data present with key {} in tree ".format(key))
                        





if __name__ == "__main__":

    node1 = Node(15)
    node2 = Node(8)
    node3 = Node(7)
    node4 = Node(20)
    node5 = Node(17)

    ## creating BST object

    tree = BinarySearchTree()
    print("inserting root...... ")
    tree.insert(node1)
    tree.insert(node2)
    tree.insert(node3)
    tree.insert(node4)
    tree.insert(node5)

    #display tree
    print("dislay Tree .............")
    tree.display()

    #search in BST
    print("Searching................")
    tree.search(70)





            







