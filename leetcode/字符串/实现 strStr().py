import time

def kmp(needle):
    n=len(needle)
    needle1=needle
    s=[0]
    i=1
    i1=0
    while(i<n): #ABCDABD
        if needle[i]!=needle1[i1] and i1==0:
            s.append(0)
            i=i+1
           # continue #不在执行后续语句
        elif  needle[i]==needle1[i1]:
            s.append(s[len(s)-1]+1)
            i+=1
            i1+=1
        elif needle[i]!=needle1[i1] and i1!=0:
            i1=i1-(i1-s[i1-1])
    return s

class Solution(object):
    def strStr(haystack,needle):
        n=len(haystack)
        m=len(needle)
        if m==0:
            return 0
        s=kmp(needle)
        i=0
        j=0
        if m==n:
            if haystack==needle:
                return 0
            else:
                return -1
        if n<m:
            return -1
        if n>m:
            while(i<n and j <m):
                if haystack[i]==needle[j]:
                    i+=1
                    j+=1
                else:
                    if j==0:
                        i+=1
                    else:
                       i = i-s[j-1]
                       j=0
                print(i)
            if j==m:
               return i-j
            else:
               return -1

    h="mississippi"
    k="issip"
    start=time.perf_counter()
    strStr(h,k)
    end=time.perf_counter()
    #print(end-start)


