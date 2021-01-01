# -*- coding: utf-8 -*-
"""
Created on Tue May  5 06:13:49 2020

@author: ITACHI
"""
import random
import sys
class BinaryTree:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data    
    def preOrder(self):
        print(self.data,end=" ")
        if(self.left):
            self.left.preOrder()
        if(self.right):
            self.right.preOrder()    
    def inOrder(self):
        if(self.left):
            self.left.inOrder()
        print(self.data,end=" ")
        if(self.right):
            self.right.inOrder()
    def postOrder(self):
        if(self.left):
            self.left.postOrder()
        if(self.right):
            self.right.postOrder()
        print(self.data,end=" ")
    def printGivenLevel(self,level):
        if(self is None):
            return;
        if(level==1):
            print(self.data,end=" ")
        if(level>1):
            if(self.left is not None):
                self.left.printGivenLevel(level-1)
            if(self.right is not None):
                self.right.printGivenLevel(level-1)
    def levelOrder(self):
        h=self.height()
        for i in range(1,h+1):
            self.printGivenLevel(i)
            print()
    def levelOrderAgain(self):
        if(self is None):
            return
        q=[]
        q.append(self)
        n=len(q)
        while(n>0):
            size=len(q)
            for i in range(size):
                if(q[0] is not None):
                    print(q[0].data,end=" ")
                    if(q[0].left is not None):
                        n+=1
                        q.append(q[0].left)
                    if(q[0].right is not None):
                        n+=1
                        q.append(q[0].right)
                del q[0]
                n-=1
            print()
    def height(self):
        if(self is None):
            return 0
        ldepth,rdepth=0,0
        if(self.left is not None):
            ldepth=self.left.height()
        if(self.right is not None):
            rdepth=self.right.height()
        return max(ldepth,rdepth)+1
    # count leaf node
    def countLeafNode(self):
        if(self.left is None and self.right is None):
            return 1
        if(self.left is None):
            return self.right.countLeafNode()
        if(self.right is None):
            return self.left.countLeafNode()
        return self.left.countLeafNode()+self.right.countLeafNode()
    def topView(self):
        if(self is None):
            return
        q=[]
        q.append(self)
        n=len(q)
        ms=-sys.maxsize-1
        while(n>0):
            size=len(q)
            if(size>ms):
                if(q[0] is not None):
                    print(q[0].data,end=" ")
                if(q[-1] is not None and size!=1):
                    print(q[-1].data,end=" ")
                print()
            for i in range(size):
                if(q[0] is not None):
                    if(q[0].left is not None):
                        q.append(q[0].left)
                        n+=1
                    else:
                        q.append(None)
                    if(q[0].right is not None):
                        q.append(q[0].right)
                        n+=1
                    else:
                        q.append(None)
                del q[0]
                n-=1
            ms=max(ms,size)
    def leftView(self):
        if(self is None):
            return
        q=[]
        q.append(self)
        n=len(q)
        while(n>0):
            size=len(q)
            for i in range(size):
                if(i==0):
                    print(q[0].data,end=" ")
                if(q[0].left is not None):
                    n+=1
                    q.append(q[0].left)
                if(q[0].right is not None):
                    n+=1
                    q.append(q[0].right)
                del q[0]
                n-=1
            print()
    def rightView(self):
        if(self is None):
            return
        q=[]
        q.append(self)
        n=len(q)
        while(n>0):
            size=len(q)
            for i in range(size):
                if(i==size-1):
                    print(q[0].data,end=" ")
                if(q[0].left is not None):
                    n+=1
                    q.append(q[0].left)
                if(q[0].right is not None):
                    n+=1
                    q.append(q[0].right)
                del q[0]
                n-=1
            print()
    def isPerfect(self):
        if self is None :
            return True
        q=[]
        q.append(self)
        n=len(q)
        level=0
        while(n>0):
            size=len(q)
            if(size !=2**level):
                return False
            level+=1
            for i in range(size):
                if(q[0].left is not None):
                    q.append(q[0].left)
                    n+=1
                if(q[0].right is not None):
                    q.append(q[0].right)
                    n+=1
                n-=1
                del q[0]
        return True
    def isBST(self):
        v=[]
        def func(root):
            if(root is None):
                return
            func(root.left)
            v.append(root.data)
            func(root.right)
        func(self)
        for i in range(1,len(v)):
            if(v[i]<v[i-1]):
                return False
        return True
data=random.randint(1,100)
root=BinaryTree(data)
print("If you don't want to enter any data then leave choice blank and press enter.")
print("Root is already added :)")
choice=input("Want to enter more data in tree : ")
while(choice):
    root.insert(random.randint(1,100))
    choice=input("Want to enter more data in tree : ") 
root.preOrder()
print()
root.inOrder()
print()
root.postOrder()
print()
print("level order : ")
root.levelOrder()
print()
print("level order again : ")
root.levelOrderAgain()
print()
h=root.height()
print(f"Height : {h}")
leafnodes=root.countLeafNode()
print(f"Leaf Nodes : {leafnodes}")
print("right view : ")
root.rightView()
print()
print("left view : ")
root.leftView()
print()
print("top view : ")
root.topView()
print()
print(root.isPerfect())
print(root.isBST())
x=input("Press enter key to exit .....!")
