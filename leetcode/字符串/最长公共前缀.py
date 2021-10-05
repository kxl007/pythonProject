class Solution(object):
    def longestCommonPrefix(strs):
        n=len(strs)
        n1=len(strs[0])
        x1=''
        for i in range(n1):
            x=strs[0][i]
            flag=True
            for j in range(1,n):
                if i<len(strs[j]):
                    if x == strs[j][i]:
                        pass
                    else:
                        flag = False
                        break
                else:
                    flag=False
                    break
            if flag:
               x1 =''.join([x1,x])
            else:
                break
        return x1

    strs=["flower","flow","flight"]
    longestCommonPrefix(strs)



