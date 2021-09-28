class Node:
   
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = []

           
    # vertical order  
    def traverse(self, node, level=0):
        if node:
            self.level.append(level)
            self.traverse(node.left, level-1)
            self.traverse(node.right, level+1)
        else:
            return
           
    # level order or horizontal order
    def level_order(self, node, level):
        if node is None:
            return
        if level == 1:
            print(node.data, end=" ")
        elif level > 1:
            self.level_order(node.left, level-1)
            self.level_order(node.right, level-1)
    
    # calculate width of BT
    def display(self):
        print(self.level)
        print("min :  {}".format(min(self.level)))
        print("max :  {}".format(max(self.level)))
        width = max(self.level) - min(self.level) + 1
        print(width)
       
    def display_tree(self, node):
        if node:
            self.display_tree(node.left)
            print(node.data, end=" ")
            self.display_tree(node.right)

 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(8)
root.right.right.left = Node(6)
root.right.right.right = Node(7)

root.display_tree(root)

# root.traverse(root, 0)
# root.display()
# root.level_order(root, 2)
