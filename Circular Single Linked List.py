class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class circular_singly_LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    # finding length of LinkedList
    def length(self):
        if self.head is None:
            return 0
        else:
            count=1
            temp=self.head
            while True:
                if temp.next is self.head:
                    return count
                else:
                    count=count+1
                    temp=temp.next
        
    #append is to add value at end of LinkedList   
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
            self.tail.next=self.head
            
            
    #append1 is to add value at begining of LinkedList
    def append1(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
            self.tail.next=self.head
            

    #inserting means adding node at given position
    #here inserting node at given location
    def insert(self,loca,data):
        count=1
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            
        else:
            if loca==0:
                self.append1(data)#while location is one we call append1 method to add at begining 
            else:
                temp=self.head
                leng=self.length()
                while True:
                    if loca>leng:
                        print("the location you provided is exceeded LinkedList so provide value below {}".format(leng))
                        break
                    
                    elif count==loca:    
                        temp1=temp.next         #here we are adding at location
                        temp.next=Node(data)
                        temp.next.next=temp1
                        if temp1 is self.head:
                            self.tail=temp.next
                        
                        break
                    else:
                        count=count+1
                        temp=temp.next

    #deleting node at given location
    def delete(self,loca):
        count=0
        if self.head is None:
            print("the LinkedList is empty deleting wont happen")
        else:
            if loca==0:
                self.head=self.head.next
                self.tail.next=self.head
                
            else:
                temp=self.head
                while True:
                    if count==loca:
                        if temp.next is self.head:
                            self.tail=temp1
                            temp1.next=self.head
                            self.head.prev=self.tail
                            break
                        else:
                            temp1.next=temp.next
                            break
                    elif temp.next is self.head:
                        print("the location you provide is out of range")
                        break
                    
                    count=count+1        
                    temp1=temp
                    temp=temp.next
    #deleting entire LinkedList
    def delete_entire(self):
        if self.head is None:
            print("the LinkedList has no values already empty")
        else:
            self.head=None
            self.tail=None
            
    # __iter__ is a method defined in class it creates a iterator of instance so that we can iterate
    # he we traverse and create generator to iterate
    def __iter__(self):
        temp=self.head
        while temp:
            if self.head is None:
                return []
            if temp.next ==  self.head:
                yield temp.data
                break
            else:
                yield temp.data
                temp=temp.next

    # her we are traversing though LinkedList to print values            
    def print(self):
        temp=self.head
        while True:
            if self.head is None:
                print("LinkedList is empty")
                break
            if temp.next ==  self.head:
                print(temp.data,end=" ")
                break
            else:
                print(temp.data,end=" ")
                temp=temp.next
            

a=circular_singly_LinkedList()
a.append(0)
a.append(1)
a.append(2)
a.append(3)
print([i for i in a])
a.insert(1,10)
print([i for i in a])
a.delete(5)
print([i for i in a])
a.delete_entire()
print([i for i in a])

            
