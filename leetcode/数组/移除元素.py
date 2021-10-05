import pysnooper
class Solution(object):
   # @pysnooper.snoop()
    def removeElement(nums, val):
        n=len(nums)
        i=0
        j=n-1
        k=0
        while(i<j):
            if nums[i]==val:
                nums[i]=-1
                k+=1
                n-=1
            if nums[j]==val:
                nums[j] = -1
                k+=1
                n-=1
            i+=1
            j-=1
        nums.sort()
        nums1=nums[k:]

        return n,nums1

    nums=[0,1,2,2,3,0,4,2]
    val=2
    removeElement(nums,val)
