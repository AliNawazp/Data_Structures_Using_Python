class Circular_Queue:
    def __init__(self,n):
        self.List=[None for i in range(n)]
        self.Length=n
        self.start=-1
        self.top=-1
    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False
    def enqueue(self,data):
        if self.start==-1 and self.top==-1:
            self.start+=1
            self.top+=1
            self.List[self.top]=data
        else:
            if self.top==self.Length-1:
                    self.top=-1
            if self.top+1==self.start:
                print("queue is not empty")
            else:
                self.top+=1
                self.List[self.top]=data
                
    def dequeue(self):
        if self.start==self.Length-1:
            self.List[self.start]=None
            self.start=0
        else:
            self.List[self.start]=None
            self.start+=1

    def __str__(self):
        if self.start==-1 and self.top==-1:
            return []
        else:
            values=[str(i) for i in self.List]
            return "\n".join(values)
a=Circular_Queue(5)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
a.enqueue(5)
print(a)
a.dequeue()
print("after dequeue",a)
a.enqueue(1)
print("after enqueue")
print(a)
a.dequeue()
a.dequeue()
a.dequeue()
print(a)
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
print(a)
a.dequeue()
print(a)
a.enqueue(5)
print(a)
a.enqueue(6)
        
    
