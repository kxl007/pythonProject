import pysnooper
class Solution(object):               #双指针记录长度
    #@pysnooper.snoop()
    def minSubArrayLen(target, nums): #target = 7, nums = [2,3,1,2,4,3]
        n=len(nums)
        i=0
        j=0
        min1=n
        flag=1
        while(j<n):
            if i>j:
                j=i
            a=sum(nums[i:j + 1])
            if a <target:
                j+=1
            else:
                flag=0
                min1 = min(j - i+1, min1)
                i += 1
                if min1==1:
                    break

        if flag:
            return 0

        return min1

    target = 11
    nums = [1,2,3,4,5]
    minSubArrayLen(target,nums)


