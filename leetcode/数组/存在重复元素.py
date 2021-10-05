class Solution(object):
    def containDuplicate(nums):
        n=len(nums)
        for i in range(0,n):
            m=0
            x=nums[i]
            for j in range(0,n):
                if x==nums[j]:
                    m+=1
                else:
                    continue
        if m==1:
            print('false')
        else:
            print('true')
    nums=[1,2,3,4,1]
    containDuplicate(nums)