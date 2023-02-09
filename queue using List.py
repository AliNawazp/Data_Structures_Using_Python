#here we are using insert for enqueue
class Queue:
    def __init__(self):
        self.List=[]
    def isEmpty(self):
        if self.List==[]:
            return True
        else:
            return False
    def isPeek(self):
        if self.isEmpty is True:
            print("Queue is empty")
        else:
            return self.List[len(self.List)-1]
    def enqueue(self,data):
        self.List.insert(0,data)
    def dequeue(self):
        if self.List==[]:
            print("The queue is empty")
        else:
            return self.List.pop()
    def delete(self):
        self.List=None
        
    def __str__(self):
        values=self.List.reverse()
        values=[str(x) for x in self.List]
        return "\n".join(values)
a=Queue()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.dequeue())

print(a.dequeue())
print("after dequeue")
print(a)
print("the peek value is {}".format(a.isPeek()))


# we can implement que as below also by using append
class Queue1:
    def __init__(self):
        self.List=[]
    def isEmpty(self):
        if self.List==[]:
            return True
        else:
            return False
    def isPeek(self):
        if self.isEmpty is True:
            print("Queue is empty")
        else:
            return self.List[0]
    def enqueue(self,data):
        self.List.append(data)
    def dequeue(self):
        if self.List==[]:
            print("The queue is empty")
        else:
            return self.List.pop(0)
    def delete(self):
        self.List=None
        
    def __str__(self):
        values=self.List.reverse()
        values=[str(x) for x in self.List]
        return "\n".join(values)

a=Queue1()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.dequeue())

print(a.dequeue())
print("after dequeue")
print(a)
print("the peek value is {}".format(a.isPeek()))
