import pysnooper
class Solution(object):
    #@pysnooper.snoop()
    def findMaxConsecutiveOnes(nums): #[0,0,1,1,0,1,1,1]
        n=len(nums)
        i=0
        j=0

        max1=0
        while(i<n):
            if nums[i]==0:
                flag=True
                j+=1
                i+=1
            else:
                flag = False
                i+=1
            if flag or i==n:
                max1=max(max1,i-j)
                j=i

        print(max1)
        return max1








    nums=[1,0,1,0,1,1,1,1]
    findMaxConsecutiveOnes(nums)




