class Solution(object):
    def removeDuolicates(nums):
        n=len(nums)
        for i in range(0,n-1):
            x = nums[i]
            j=i+1
            while j<n:
                if x==nums[j]:
                   del nums[j]
                   n-=1
                else:
                    break
            if j>=n:
                break
        return nums

    num=[0,0,0,1,1,1,1,2,5,5,5,7,7,7]
    removeDuolicates(num)