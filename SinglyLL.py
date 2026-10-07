class Node:
    def __init__(self,info,next=None):
        self.info = info
        self.next= next
    
class SinglyLl:
    def __init__(self,head=None):
        self.head = head
    
    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head !=None):
            t1 = self.head
            while(t1.next !=None):
                t1 =t1.next
            t1.next = temp
        else:
            self.head = temp
    
    
    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def insertAtMid(self,value,x):
        temp = Node(value)
        t1 = self.head
        
        while(t1.next != None):
            if(t1.info == x):
                temp.next = t1.next
                t1.next= temp
            t1 = t1.next
    
    def printLL(self):
        t1= self.head
        while(t1.next !=None):
            print(t1.info)
            t1 = t1.next
        print(t1.info)


obj = SinglyLl()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtBeg(5)
obj.insertAtMid(60,30)
obj.printLL()
