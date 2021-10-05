import numpy as np
class Solution(object):
    def addTwoNum(l1,l2):
        n1=len(l1)
        n2=len(l2)
        x=0
        y=0
        for i in range(0,n1):
            x=x+10**i*l1[i]
        for j in range(0,n2):
            y=y+10**j*l2[j]
        a=x+y
        l3=[]
        while(a>=1):
            l3.append(a%10)
            a=int(a/10)
        return l3

    l1=[2,4,3]
    l2=[7,6,5]
    addTwoNum(l1,l2)
