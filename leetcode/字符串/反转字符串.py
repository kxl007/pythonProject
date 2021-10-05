class Solution(object):
    def reverseString(s):
           #[h ,e ,l , l, o]--[o
        n=len(s)
        for i in range(int(n/2)):
            templt=s[i]
            s[i]=s[n-1-i]
            s[n-1-i]=templt
        return s
    s=['c','o','o','l']
    reverseString(s)

