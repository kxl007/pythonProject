import pysnooper
class Solution(object):
    #@pysnooper.snoop()
    def lengthOfLongestSubstring(s):#"abccbcbb"
        if s=='':
            return 0
        i = 0
        ans = 0
        n=len(s)
        t1 = []
        while(i<n):
            x = s[i]
            flag = (x in t1)
            if x not in t1 :
                t1.append(x)
                i+=1
                flag=(i==n)
            y1=t1.index(x)
            if flag:
                ans=max(ans,len(t1))
                t1=t1[y1+1:]
        return ans
    x='abc'
    lengthOfLongestSubstring(x)

