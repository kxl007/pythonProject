#三元组下标 (i, j, k) 且满足 i < j < k ，使得 nums[i] < nums[j] < nums[k]
#判断是否局部有序 2,1,5,0,4,6
import pysnooper
class Solution(object):
    def increasingTripl(nums):
        if len(list(set(nums)))<3:
            return False
        n=len(nums)
        nums1=nums[:]    #互不影响的拷贝
        flag2=True
        s=[1]
        for i in range(1,n):
            sa=[]
            t=0
            j=i-1
            x=nums[i]
            while(x<=nums[j] and j>-1):
                nums[j+1]=nums[j]
                t+=1
                j-=1
            nums[j + 1] = x
            if t != i:
                for k1 in range(j,-1,-1):
                    y2 = [x for (x, m) in enumerate(nums1[:i]) if m == nums[k1]]
                    y3=max(y2)
                    if s[y3] not in sa:
                        sa.append(s[y3])
                y = max(sa) + 1
            else:
                y = 1
            s.append(y)
            if y>=3:
                flag2= False
                print('t')
                return True
        if flag2:
            print('f')
            return False
    a=[1,2,3,4,5]
    increasingTripl(a)







