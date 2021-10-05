class Solution(object):
    def intersect(num1,num2):
        n1 = len(num1)
        n2 = len(num2)
        n = min(n1,n2)
        num3 = []
        i = 0
        while i < n:
            m1=0
            m=0
            for l in range(0,n1):
                if num1[i]==num1[l]:
                    m1 += 1
            for j in range(0,n2):
                if num1[i] == num2[j]:
                    m += 1
            if m != 0:
                if num1[i] not in num3:
                    for i1 in range(0,min(m,m1)):
                        num3.append(num1[i])
            i += 1
        return num3
    num2=[4,4,9,5]
    num1=[9,4,9,8,4,4]
    intersect(num1,num2)


