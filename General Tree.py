class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
    def addchild(self,child):
        self.children.append(child)
    def __str__(self,level=0):
        ret=" "*level+self.data+"\n"
        for i in self.children:
            ret+=i.__str__(level+1)
        return ret
tree=TreeNode("Drinks")
cold=TreeNode("Cold")
hot=TreeNode("Hot")
tree.addchild(cold)
tree.addchild(hot)
tea=TreeNode("Tea")
coffee=TreeNode("Coffee")
pepsi=TreeNode("Pepsi")
fanta=TreeNode("Fanta")
hot.addchild(tea)
hot.addchild(coffee)
cold.addchild(fanta)
cold.addchild(pepsi)
print(tree)
