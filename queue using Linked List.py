class Node:
    def __init__(self,a):
        self.data=a
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
    #appending1 means adding node at begining
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
    #deleting node at 0th location because in stack we LIFO
    def delete(self):
        if self.head is self.tail:
            temp=self.head.data
            self.head=None
            self.tail=None
        else:
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
            
class Queue:
    def __init__(self):
        self.queue=LinkedList() #instance of LinkedList
    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False
    def Enqueue(self,data):
        self.queue.append(data)
    def Dequeue(self):
        if self.is_empty is True:
            print("the stack is empty pop operation cannot be done")
        else:
            return self.queue.delete()
    def peek(self):
        if self.queue.head is None:
            print("queue is empty")
        else:
            return self.queue.head.data
    def __str__(self):
        temp=[str(i.data) for i in self.queue]
        return "\n".join(temp)
if __name__=="__main__":      
    a=Queue()
    a.Enqueue(1)
    a.Enqueue(2)
    a.Enqueue(3)
    print(a)
    print("the element we removed is",end=" ")
    print(a.Dequeue())
    print("after removing queue is")
    print(a)
    a.Enqueue(4)
    print(a.Dequeue())
    print("after removing queue is")
    print(a)
    print(a.peek())

