import string
class Solution(object):
    def myAtoi(s):
        n=len(s)
        s1=''
        flag=True
        k1=1
        for i in range(n):
            if str(s)[i].isalpha() and flag:
                return 0
            if str(s)[i].isspace() and flag:
                pass
            if str(s)[i].isspace() and flag==False:
                break
            if s[i] in string.punctuation and flag and s[i]!='-' and s[i]!='+':
                return 0
            if s[i] in string.punctuation and flag==False :
                break
            if str(s)[i].isalpha() and flag==False:
                break
            if s[i]=='-' or s[i]=='+':
                if k1==1:
                    s1=''.join([s1,s[i]])
                    flag=False
                    k1+=1
                else:
                    return 0
            if str(s)[i].isalnum():
                s1 = ''.join([s1, s[i]])
                flag = False
        if flag or s1=='-' or s1=='+':
            return 0
        k=int(s1)
        if k<-2**31:
            return -2**31
        if k>2**31-1:
            return 2**31-1
        if -2**31<=k<=2**31-1:
           print(k)
    s='+ 12'
    myAtoi(s)












