#求矩阵的鞍点  行上最下 列上最大
class Solution(object):
    def findAndian(matrix):
        n=len(matrix)
        m=len(matrix[0])
        for i in range(n):
            ans=min(matrix[i])
            ind=matrix[i].index(ans)
            max=max(matrix[:ind])
            if ans==max:
                print(ans)
                break

