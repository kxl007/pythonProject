import pysnooper
class Solution:
    @pysnooper.snoop()
    def lengthOfLongestSubstring( s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            print(ans)
            st[s[j]] = j + 1
            print(st)
        print(ans)
    s='abcab'
    lengthOfLongestSubstring(s)