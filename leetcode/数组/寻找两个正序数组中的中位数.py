from decimal import *
class Solution(object):
    def findMedianSortedArrays(nums1, nums2):
        m=len(nums1)
        n=len(nums2)
        nums3=[]
        if m==0 :
            nums3=nums2
        if n==0 :
            nums3=nums1
        i=0
        j=0
        while(i<m and j <n):
            if nums1[i]<=nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
            if j==n:
                for k in range(i,m):
                    nums3.append(nums1[k])
            if i==m:
                for k in range(j, n):
                    nums3.append(nums2[k])
        if (m+n)%2==0:
            mid=(nums3[int((n+m)/2)]+nums3[int((n+m)/2)-1])/2
        else:
            mid=nums3[int((n+m-1)/2)]
        mid=("{:.5f}".format(mid))
        mid=Decimal(mid)
        print(mid)

        return  mid  #返回小数点后几位




    nums1 = [1,2]
    nums2 = [3,4]
    findMedianSortedArrays(nums1,nums2)



