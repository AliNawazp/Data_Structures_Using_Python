class Node:
    def __init__(self,a):
        self.data=a
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
    #appending1 means adding node at begining
    def append1(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
    #deleting node at 0th location because in stack we LIFO
    def delete(self):
        temp=self.head.data
        self.head=self.head.next
        return temp
    
    def __iter__(self):
        temp=self.head
        while True:
            yield temp
            if temp.next is None:
                break
            temp=temp.next
            
class Stack:
    def __init__(self):
        self.stack=LinkedList() #instance of LinkedList
    def is_empty(self):
        if self.stack.head is None:
            return True
        else:
            return False
    def Push(self,data):
        self.stack.append1(data)
    def Pop(self):
        if self.is_empty is True:
            print("the stack is empty pop operation cannot be done")
        else:
            return self.stack.delete()
    def peek(self):
        if self.stack.head is None:
            print("stack is empty")
        else:
            return self.stack.head.data
    def __str__(self):
        temp=[str(i.data) for i in self.stack]
        return "\n".join(temp)
        
a=Stack()
a.Push(1)
a.Push(2)
a.Push(3)
print(a)
print("the element we poped is",end=" ")
print(a.Pop())
print("after poping the stack is")
print(a)
