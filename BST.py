class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node)

def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right)        

array = [50, 20, 30, 40, 60]
r = Node(array[0])

def addArr(arr):
    for i in range(len(arr)):
        insert(r,Node(i))

addArr(array)
inorder(r) 

