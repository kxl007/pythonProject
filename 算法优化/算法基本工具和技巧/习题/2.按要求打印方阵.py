import pysnooper
class Solution(object):
    @pysnooper.snoop()
    def printM(nums):
        n=len(nums)
        s=[]
        s.append(nums)

        for i in range(1,n):
            nums1=s[i-1][:] #数组赋值 注意不能全部跟动
            x = nums1[n - 1]
            for j in range(n-1,0,-1):
                nums1[j]=nums1[j-1]
            nums1[0]=x
            s.append(nums1)
        print(s)
        return s



    nums=[5,7,4,8,9,1]
    printM(nums)




