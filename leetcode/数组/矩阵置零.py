import pysnooper
class Solution(object):
   # @pysnooper.snoop()
    def setZeroes(matrix): #矩阵置零
        m=len(matrix)
        n=len(matrix[0])
        s=[]
        t=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i not in s:
                        s.append(i)
                    if j not in t:
                        t.append(j)
        for i in range(len(s)):
            for j in range(n):
                matrix[s[i]][j]=0
        for i in range(len(t)):
            for j in range(m):
                matrix[j][t[i]]=0

        return matrix

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    setZeroes(matrix)




