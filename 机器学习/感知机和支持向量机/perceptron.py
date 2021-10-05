import numpy as np
class Perceptron(object):
    def perceptron(s,t):
        n=len(s)

        w=np.array([0,0])
        b=0
        k=0
        while(k<n):
            if (np.dot(w,s[k][0])+b)*s[k][1]<=0:
                w=w+s[k][0]*s[k][1]*t
                b=b+s[k][1]
                k=0
            else:
                k+=1
        return w,b,n
#感知机判断出错误点 直到错误点纠正过来才停止


