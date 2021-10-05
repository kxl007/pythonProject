#编写算法 打印图形
import pysnooper
class Solution(object):
    #@pysnooper.snoop()
    def printPic(n):
        for i in range(n):
            s = str(i + 1)
            j=i
            j-=1
            x=0
            k=0
            while(j+1>0):
                x=x+n-k
                x1=x+j+1
                s=' '.join([str(x1),s])
                j-=1
                k+=1
            print(s)
    n=5
    printPic(n)







