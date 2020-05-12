# -*- coding: utf-8 -*-
"""
Created on Tue May 12 08:37:18 2020

@author: ITACHI
"""
import random
class Node:  
    def __init__(self, data): 
        self.data = data 
        self.next = None
class LinkedList:
    def __init__(self):
        self.head=None
        self.length=0
    def add(self,data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
        self.length+=1
    def display(self):
        temp=self.head
        while(temp is not None):
            print(temp.data,end=" ")
            temp=temp.next
        print()
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
    
    def check_for_delete(self):
        n=self.length
        pos=random.randint(0,n-2)+1     # min 3 element should be in the list 
                                        # because we have to select the  middle node 
                                        # not end nodes
        curr=self.head
        while(pos>0):
            curr=curr.next
            pos-=1
        return curr
    # DELETE THE NODE Whose address is given or pointer is given without  using head
    # that node is neither head nor last of linked list
    def delete_without_head_pointer(self,node):
        temp=node.next
        node.data,temp.data=temp.data,node.data
        node.next=temp.next
l1=LinkedList()
choice=input("Enter choice for adding element : ")
while(choice):
    l1.add(random.randint(1,100))
    choice=input("Enter choice for adding element : ")
l1.display()
l1.reverse()
l1.display()
node=l1.check_for_delete()
l1.delete_without_head_pointer(node)
l1.display()