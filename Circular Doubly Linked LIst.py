class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class Circular_Doubly_Linked_List:
    def __init__(self):
        self.head=None
        self.tail=None

    def Length(self):
        leng=0
        if self.head is None:
            return Leng
        else:
            temp=self.head
            leng=leng+1
            while True:
                if temp.next is self.head:
                    return leng
                else:
                    leng=leng+1
                    temp=temp.next
            

    #adding node to end of LinkedList
    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=self.tail
            self.tail.next=Node(data)
            self.tail=self.tail.next
            self.tail.prev=temp
            self.tail.next=self.head
            self.head.prev=self.tail

    #adding node at begining of LinkedList
    def append1(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        else:
            temp=self.head
            self.head=Node(data)
            self.head.next=temp
            temp.prev=self.head
            self.tail.next=self.head
            self.head.prev=self.tail

    #inserting node at given position
    def insert(self,loca,data):
        leng=self.Length()
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
            self.tail.next=self.head
            self.head.prev=self.tail
        elif loca>leng:
            print("the given location is out of index please provide index below {}".format(leng))
        else:
            if loca==0:
                self.append1(data)
            else:
                count=1
                temp=self.head
                while True:
                    if count>leng:
                        print("the given location is out of index so please provide index below {}".format(leng))
                        break
                    else:
                        if temp.next is self.head and count==loca:
                            temp.next=Node(data)
                            temp.next.next=self.head
                            temp.next.prev=temp
                            self.tail=temp.next
                            self.head.prev=self.tail
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
    def delete(self,loca):
        if self.head is None:
            print("the LinkedList is empty so deletion is not possible")
        else:
            if loca==0:
                self.head=self.head.next
                self.tail.next=self.head
                self.head.prev=self.tail
            else:
                count=1
                leng=self.Length()
                temp=self.head.next
                while True:
                    if count<leng:
                        if temp.next is self.head and count==loca:
                           self.tail=temp.prev
                           self.tail.next=self.head
                           self.head.prev=self.tail
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
                

                        
            

    # __iter__() is a special method that creates a iterator for class instance
    def __iter__(self):
        temp=self.head
        while True:
            if temp.next is self.head:
                yield temp
                break
            else:
                yield temp
                temp=temp.next
            
    #traversing through LinkedList to print values
    def print(self):
        temp=self.head
        while True:
            if temp.next is self.head:
                print(temp.data)
                break
            else:
                print(temp.data)
                temp=temp.next
                


    
a=Circular_Doubly_Linked_List()
a.append(0)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append1(-1)
a.append1(-2)
a.append(5)
a.print()
print([x.data for x in a])
a.insert(0,-3)
print([x.data for x in a])
a.insert(1,10)
print([x.data for x in a])
a.insert(9,11)
print([x.data for x in a])
a.delete(0)
print([x.data for x in a])
a.delete(10)
print([x.data for x in a])
a.delete(9)
print([x.data for x in a])



