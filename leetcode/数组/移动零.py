class Solution(object):
    def moveZero(nums):
        #[0,1,0,3,12] [1,3,12,0,0] 不能拷贝额外数组
        n=len(nums)
        j=0
        for i in range(0,n):
            if nums[i]==0:
                j+=1
        for item in nums[:]:
            if item==0:
                nums.remove(item)
        print(nums)
        for i in range(0,j):
            nums.append(0)
        print(nums)

    num=[0,0]
    moveZero(num)




