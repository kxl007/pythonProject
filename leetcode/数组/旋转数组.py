class Solution(object):
    def rotate(nums,k):
        #[1,2,3,4,5,6,7]
        i=0
        n=len(nums)
        while i<k:
            x=nums[n-1]
            for j in range(n-2,-1,-1):
                nums[j+1]=nums[j]
            nums[0]=x
            i+=1
        print(nums)

    nums=[1,2,3,4,5,6,7]
    rotate(nums,6)





