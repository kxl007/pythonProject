class Solution(object):  #注意循环算法的效率 累加 /累乘
    def sumL(n):
        sum1=0
        x = 0
        for i in range(n):
            x=x+2*10**i
            sum1=sum1+x
        print(sum1)
        return sum1
    sumL(3)
