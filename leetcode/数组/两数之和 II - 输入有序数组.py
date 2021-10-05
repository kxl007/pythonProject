class Solution(object):
    def twoSum(numbers, target):#numbers = [2,7,11,15], target = 9
        i=0
        k=len(numbers)-1
        while(i<k):
            if numbers[i]+numbers[k]==target:
                print([i+1,k+1])
                return [i+1,k+1]
            if numbers[i]+numbers[k]<target:
                i+=1
            if numbers[i] + numbers[k] > target:
                k-=1

    numbers =[-2,-2,7,11,15]
    target =-4
    twoSum(numbers,target)