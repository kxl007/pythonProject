import numpy
import pysnooper
class Solution(object): #组合所有字母异位词
    @pysnooper.snoop()
    def groupAnagrams(strs): #字典键是唯一的，值不一定 strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        res=[]
        s=[x for x in range(len(strs))]
        for k in s:
            res1 = []
            i = 0
            j = len(s) - 1
            while(i<j):
                a=list(strs[s[i]])
                a.sort()
                b=list(strs[s[k]])
                b.sort()
                c=list(strs[s[j]])
                c.sort()
                if a==b :
                    res1.append(strs[s[i]])
                    s[i]=0
                if  c== b :
                    res1.append(strs[s[j]])
                    s[j]=0

                i+=1
                j-=1
            s=list(set(s))
            res.append(res1)
        print(res)
        return res

    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    groupAnagrams(strs)
















