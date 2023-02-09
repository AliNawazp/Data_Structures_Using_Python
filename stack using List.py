class Stack:
    def __init__(self):
        self.List=[]
    def is_empty(self):
        if self.List==[]:
            return True
        else:
            return False
    def Length(self):
        return len(self.List)
    def Push(self,data):
        self.List.append(data)
    def Pop(self):
        if self.is_empty() is True:
            print("The Stack is already empty no pop operation takes place")
        else:
            return self.List.pop()
    def peek(self):
        return self.List[self.Length()-1]
    def __str__(self):
        values=[str(i) for i in self.List]
        values.reverse()
        for i in values:
             return "\n".join(values) 
a=Stack()
a.Push(1)
a.Push(2)
a.Push(3)
print(a)
a.Pop()
print(a)
