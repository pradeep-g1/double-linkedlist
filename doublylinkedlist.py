class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def traversal(self): #forward traversal
        if self.head is None:
            print("the linkedlist is empty: ")
        else:
            node=self.head
            while node:
                print(node.data,"->",end=" ")
                node=node.next
            print()
    def btraversal(self):
        if self.tail is None:
            print("the linkedlist is empty")
        else:
            n=self.tail
            while n:
                print(n.data,"-->",end=" ")
                n=n.prev
            print()
    def insertion(self,item,location):
        newnode=Node(item)
        if self.head is None:
            self.head=self.tail=newnode
        else:
            if location == 0:
                newnode.next=self.head
                newnode.prev=None
                self.head.prev=newnode
                self.head=newnode
            elif location == 1:
                newnode.next=None
                newnode.prev=self.tail
                self.tail.next=newnode
                self.tail=newnode
            else:
                index=0
                currnode=self.head
                while index < location - 1:
                    currnode=currnode.next
                    index+=1
                newnode.next=currnode.next
                newnode.prev=currnode
                newnode.next.prev=newnode
                currnode.next=newnode
    def searching(self,itemvalue):
        if self.head is None:
            print("Linked list is empty: ")
        else:
            node=self.head
            while node:
                if node.data == itemvalue:
                    print("yes the value found")
                node=node.next
    def deletion(self,location):
        if self.head is None:
            print("the linked list is empty: ")
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            if location == 0:
                self.head=self.head.next
                self.head.prev=None
            elif location == 1:
                self.tail=self.tail.prev
                self.tail.next=None
            else:
                index=0
                node=self.head
                while index < location-1:
                    node=node.next
                    index+=1
                nextnode=node.next.next
                nextnode.prev=node
                node.next=nextnode
            
dll=linkedlist()
num=list(map(int,input("enter the numbers: ").split(" ")))
for i in num:
    dll.insertion(i,1)
dll.traversal()
ele=int(input("enter the element for searching: "))
dll.searching(ele)
el=int(input("enter the element for deleting location: "))
dll.deletion(el)
dll.traversal()
dll.btraversal()
