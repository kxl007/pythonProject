import string
class Solution(object):
    def isPalindrome(s):
        #回文串 正着读反着读都一样
        s=str(s).lower()
        list=[]
        flag=True
        n=len(s)
        for i in range(n):
            x=s[i]
            if x not in string.punctuation and x not in string.whitespace:
                list.append(x)
        k=len(list)
        for j in range(int(k/2)):
            if list[j]==list[k-1-j]:
                pass
            else:
                flag=False
                return False
        if flag:
            return True
        #return语句退出一个函数，而不执行函数之后的代码  如果在一个函数中有一个循环，那么在循环中使用return就相当于在循环中使用了break(当然，循环外的函数剩余的的代码也都没有执行)


s='abbbA'
Solution.isPalindrome(s)




