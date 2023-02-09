import queue as qu







class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def preorder(tree):
    if tree is None:
        return
    print(tree.data)
    preorder(tree.left)
    preorder(tree.right)

def inorder(tree):
    if tree is None:
        return
    inorder(tree.left)
    print(tree.data)
    inorder(tree.right)
    
def postorder(tree):
    if tree is None:
        return
    postorder(tree.left)
    postorder(tree.right)
    print(tree.data)

def Levelorder(tree):
    if tree is None:
        return
    else:
        q=qu.Queue()
        q.Enqueue(tree)
        while not (q.is_empty()):
            temp=q.Dequeue()
            print(temp.data)
            if temp.left is not None:
                q.Enqueue(temp.left)
            if temp.right is not None:
                q.Enqueue(temp.right)

            
    
    
root=Tree("Drinks")
hot=Tree("Hot")
cold=Tree("Cold")
root.left=hot
root.right=cold
tea=Tree("Tea")
coffee=Tree("Coffee")
hot.left=tea
hot.right=coffee
pepsi=Tree("Pepsi")
fanta=Tree("Fanta")
cold.left=pepsi
cold.right=fanta
print("preorder of tree is \n")
preorder(root)
print("\n")
print("inorder of tree is")
inorder(root)
print("\n")
print("postorder of tree is")
postorder(root)
print("\n")
print("Levelorder of tree is")
Levelorder(root)
