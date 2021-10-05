import pysnooper
class Solution(object):    #给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
   # @pysnooper.snoop()
    def reverseWords(s):   #"Let's take LeetCode contest"    "s'teL ekat edoCteeL tsetnoc"
        i=0                #：在python中，字符串是不可变对象，不能通过下标的方式直接赋值修改
        j=0
        k=0
        s=list(str(s))
        while(k<len(s)):
            if s[k]!=' ':
                j=k
            if s[k]==' ' or k==len(s)-1:
                i1=i
                j1=j
                while(i1<j1):
                    x=s[j1]
                    s[j1]=s[i1]
                    s[i1]=x
                    i1+=1
                    j1-=1
                i=k+1
            k+=1
        s=''.join(s)
        return s
    s="Let's take LeetCode contest"
    reverseWords(s)





