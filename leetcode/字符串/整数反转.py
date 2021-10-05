class Solution(object):
    def reverse(x):
        #数字转化为字符串 str(x) 字符串数字化
        z=''
        k=0
        if x==0 :
            print(k)
        if 0<x<=2**31-1:
            y=str(x)
            n=len(y)
            for i in range(n-1,-1,-1):
                z=''.join([z,y[i]])
            if int(z)>2**31-1 or int(z)<-2**31:
                print(k)
            else:
                print(int(z))

        if -2**31<=x<0:
            y=str(x)
            y=y.lstrip('-')
            n=len(y)
            for i in range(n-1,-1,-1):
                z = ''.join([z, y[i]])
            print(z)
            z1=''.join(['-',str(int(z))])
            if int(z1)>2**31-1 or int(z1)<-2**31:
                print(k)
            else:
                return int(z1)

    x=1563847412
    reverse(x)














