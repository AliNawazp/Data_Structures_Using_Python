class Stack:
    def __init__(self):
        self.List=[]
        self.max_size=4
    def is_empty(self):
        if self.List==[]:
            return True
        else:
            return False
    def is_full(self):
        if self.Length()>=self.max_size:
            return True
        else:
            return False
    def Length(self):
        return len(self.List)
    
    def Push(self,data):
        if self.is_full() is False:
            self.List.append(data)
        else:
            print("stack is full")
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
a.Push(4)
a.Push(5)
print(a)
a.Pop()
print(a)
