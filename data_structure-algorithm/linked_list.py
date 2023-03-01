from random import randint
class Node:
    #constructor
    def __init__ (self,data=None):
        self.data=data
        self.next=None

class Linked_list:
    #constructor
    def __init__(self):
        self.head=Node()

    #get length of the linked list
    def length(self):
        size=0
        cur_node=self.head
        while cur_node.next!=None:
            size+=1
            cur_node=cur_node.next
        return size

    #add a new element to the linked list
    def append(self,data):
        new_node=Node(data)
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
        cur_node.next=new_node

    #print out the linked list in order
    def display(self):
        cur_node=self.head
        lst=[]
        while cur_node.next!=None:
            cur_node=cur_node.next
            lst.append(cur_node.data)
        for x in lst:
            print(x,end=" ")

    #if an element is in the linked list,return True
    #else return False
    def find(self,data):
        cur_node=self.head
        while cur_node.next!=None:
            cur_node=cur_node.next
            if(cur_node.data==data):
                return True
        return False

    #erase an element at a specific index
    def erase(self,index):
        cur_node=self.head
        cur_index=0
        while True:
            last_node=cur_node
            cur_node=cur_node.next
            if(cur_index == index):
                last_node.next=cur_node.next
                return
            cur_index+=1
    
if __name__ == '__main__':
    ll=Linked_list()

    for i in range(12):
        ll.append(i)

    print("the linked list is:",end="")
    ll.display()
    print()
    print(ll.find(2))

    print("size of the array is: %s" %(ll.length()))

    ll.erase(2)

    print("after erase:",end="")
    ll.display()