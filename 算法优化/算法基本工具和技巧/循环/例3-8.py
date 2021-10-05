#从高位到地位输出十进制数字
class Solution(object):
    def highTolow(s):
        q=[]
        while(s>=1):
            x=s%10
            q.append(x)
            s=int(s/10)
        for i in range(len(q)-1,-1,-1):
            print(q[i])
    s=976
    highTolow(s)

