class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Double_Linked_List:
    def __init__(self):
        self.head=None
        self.tail=None
    #length of LinkedList
    def Length(self):
        leng=0
        if self.head is None:
            return 0
        else:
            temp=self.head
            while True:
                leng=leng+1
                if temp.next is None:
                    return leng
                temp=temp.next
                
    #append is to add value at ending        
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail.next.prev=self.tail
            self.tail=self.tail.next
    
    #append1 is to add at begining
    def append1(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
            temp.prev=self.head
            
    #inserting value at given locaion
    def insert(self,loca,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            if loca==0:
                self.append1(data)
            else:
                count=1
                leng=self.Length()
                temp=self.head
                while True:
                    if count<=leng:
                        if temp.next is None and count==loca:
                           temp.next=Node(data)
                           temp.next.prev=temp
                           self.tail=temp.next
                           break
                        elif count==loca:
                            temp1=temp.next
                            temp.next=Node(data)
                            temp.next.prev=temp
                            temp.next.next=temp1
                            temp.next.next.prev=temp.next
                            break
                        else:
                            count=count+1
                            temp=temp.next
                    else:
                        print("the location you provided is out of range so provide below {}".format(leng))
                        break                    
                
    #deleting node at given position
    def delete(self,loca):
        if self.head is None:
            print("the LinkedList is empty so deletion is not possible")
        else:
            if loca==0:
                self.head=self.head.next
                self.head.prev=None
            else:
                count=1
                leng=self.Length()
                temp=self.head.next
                while True:
                    if count<leng:
                        if temp.next is None and count==loca:
                           self.tail=temp.prev
                           self.tail.next=None
                           break
                        elif count==loca:
                            temp.prev.next=temp.next
                            temp.next.prev=temp.prev
                            break
                        else:
                            count=count+1
                            temp=temp.next
                    else:
                        print("the location you provided is out of range so provide below {}".format(leng))
                        break
                
            
        


        
    #delete entire LinkedList
    def delete_entire(self):
        if self.head is None:
            print("the LinkedList is already empty")
        else:
            self.head=None
            self.tail=None
            
            
    #__iter__() creates a iterator of instance of class
    def __iter__(self):
        if self.head is None:
            return []
        else:
            temp=self.head
            while True:
                if temp.next is None:
                    yield temp
                    break
                else:
                    yield temp
                    temp=temp.next
    
    #traversing throuugh LinkedList and printing the values
    def print(self):
        if self.head is None:
            print("the LinkedList is empty")
        else:
            temp=self.head
            while True:
                if temp.next is None:
                    print(temp.data)
                    break
                else:
                    print(temp.data)
                    temp=temp.next
                
                
    
a=Double_Linked_List()
a.append(0)
a.append(1)
a.append1(-1)
a.append(2)
a.append1(-2)
a.append(3)
print(a.Length())
print([i.data for i in a])
a.append(4)
a.append1(-3)
print([i.data for i in a])
a.print()
a.insert(1,2)
print([i.data for i in a])
a.insert(0,10)
print([i.data for i in a])
a.delete(0)
print([i.data for i in a])
a.delete(2)
print([i.data for i in a])
a.delete(8)



            
