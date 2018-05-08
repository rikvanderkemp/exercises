import random

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def search(self, value):
        if (self.value == value):
            return self
        
        if (value < self.value and self.left is not None):
            return self.left.search(value)
        
        if (value > self.value and self.right is not None):
            return self.right.search(value)

        return None

    def add(self, node):
        if (node.value < self.value):
            if (self.left is not None):
                self.left.add(node)
            else:
                self.left = node
        
        if (node.value > self.value):
            if (self.right is not None):
                self.right.add(node)
            else:
                self.right = node

    def __str__(self):
        out = ''
        if (self.left is not None):
            out += str(self.left)
        
        out += str(self.value) + ' '

        if (self.right is not None):
            out += str(self.right)

        return str(out)

class Tree():
    def __init__(self, *args, **kwargs):
        self.root = None

    def add(self, value):
        node = Node(value)

        if (self.root is None):
            self.root = node
        else:
            self.root.add(node)
    
    def printTree(self):
        if (self.root != None):
            print(self.root)

    def search(self, value):
        return self.root.search(value)
                
"""Use the tree to prove workings....
"""
tree = Tree()
max = 15

for i in range(1, max):
    tree.add(random.randint(1, 100))
    

tree.printTree()

for i in range(1, max):
    print('Searching for {}: {}'.format(i, 'Found! 🎉' if tree.search(i) else 'no' ))