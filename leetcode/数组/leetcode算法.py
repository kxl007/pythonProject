class Solution(object):
    def twosum(nums,target):
        n=len(nums)
        for i in range (0,n) :
            a=target-nums[i]
            for j in range(i+1,n):
                if nums[j]==a:
                   print(i,j)
    x=[3,7,11,15]
    y=18
    twosum(x,y)
