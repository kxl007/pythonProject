class Solution(object):
    def rotate(matrix):
        realmatrix = []
        n=len(matrix)  #行
        m=len(matrix[0])  #列
        for i in range(n):
            for j in range(m):
                realmatrix.append(matrix[i][j])
        for j in range(m*n):
            k=int(j/m)
            k1=j%m
            matrix[k1][n-1-k]=realmatrix[j]
        return matrix






    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)
