class Solution(object):
    def generate(numRows):
        s=[x for x in range(numRows)]
        for i in range(numRows):
            s1=[x for x in range(i+1)]
            if i==0:
                s[i]=[1]
                continue
            if i==1:
                s[i]=[1,1]
                continue
            if i>1:
                for j in range(1, i):
                    s1[0] = 1
                    s1[i] = 1
                    s1[j] = s[i - 1][j - 1] + s[i - 1][j]
                s[i]=s1
        return s
    n=1
    generate(n)


