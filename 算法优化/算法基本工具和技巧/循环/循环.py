#循环体是不变式
#自顶向下
#判断一个数是否为‘完数’
import pysnooper

class Solution(object):
    #@pysnooper.snoop()
    def findFullnum(s):
        for i in range(2,s+1):
            key=1
            strs='1'
            for j in range(2,int(i/2)+1):
                if i%j==0:
                    key=key+j
                    strs=','.join([strs,str(j)])
            if key==i:
                print('%d'%i+' its factors are '+strs)
    s=1000
    findFullnum(s)


