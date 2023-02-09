class Node:
    def __init__(self,a):
        self.data=a
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
        
    # finding length of LinkedList
    def length(self):
        if self.head is None:
            return 0
        else:
            count=1
            temp=self.head
            while True:
                if temp.next is None:
                    return count
                else:
                    count=count+1
                    temp=temp.next

    #appending means adding node at ending
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
            
    #appending1 means adding node at begining
    def append1(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
            
    
                        
    #inserting means adding node at given position
    #here inserting node at given location    
    def insert(self,loca,data):
        count=1
        leng=self.length()
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
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
                        if temp1 is None:
                            self.tail=temp.next
                        break
                    else:
                        count=count+1
                        temp=temp.next

    #inserting1 means adding node after  given data
    def insert1(self,data1,data): #data1 is data in LinkedList to find and data is data we need to add
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            temp=self.head
            while True:
                if temp.next is None:
                    if temp.data==data1:
                        self.append(data)
                        break
                    else:
                        print("the data1 you provide is not in list")
                        break
                    
                elif temp.data==data1:
                    temp1=temp.next         
                    temp.next=Node(data)
                    temp.next.next=temp1
                    break
                temp=temp.next

                
    #inserting2 means adding node before  given data
    
    def insert2(self,data1,data): #data1 is data in LinkedList to find and data is data we need to add
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            if self.head.data==data1:
                self.append1(data)
            else:
                temp=self.head
                while True:
                    if temp.next is None:
                        print("the data1 you provide is not in list")
                
                    elif temp.data==data1:
                        temp1.next=Node(data)
                        temp1.next.next=temp
                        break
                    temp1=temp
                    temp=temp.next
                    
    #deleting node at given location
    def delete(self,loca):
        count=0
        if self.head is None:
            print("the LinkedList is empty deleting wont happen")
        else:
            if loca==0:
                self.head=self.head.next
            else:
                temp=self.head
                while True:
                    if count==loca:
                        if temp.next is None:
                            self.tail=temp1
                            temp1.next=None
                            break
                        else:
                            temp1.next=temp.next
                            break
                    elif temp.next is None:
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
            
    #travesing through LinkedList to print data
    def print(self):
        if self.head is None:
            print("Linked is empty")
        else:
            temp=self.head
            while True:
                if temp.next is not None:
                    print(temp.data)
                    temp=temp.next
                else:
                    print(temp.data)
                    break
    
    #printing LinkedList using yield
    # __iter()__ is a special method that creates a iterator for instance of class so that we use instance as iterator
    def __iter__(self):
        temp=self.head
        while temp:
            yield temp
            temp=temp.next

    #__str__() is a special method
    def __str__(self):
        values=[str(x.data) for x in self]
        return "-->".join(values)
    
a=LinkedList()
a.append(2)
a.append(3)
a.append1(1)
a.insert(6,6)
a.insert(1,0)
a.insert1(2,10)
a.insert2(2,11)
a.print()
print([i.data for i in a])
a.delete(5)
print([i.data for i in a])
a.insert(0,10)
print([i.data for i in a])
a.insert(6,100)
print([i.data for i in a])
a.delete(2)
print([i.data for i in a])
print(a)





        
