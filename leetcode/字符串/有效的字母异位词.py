import sys
class Solution1(object):
    def isAnagram(s,t):
        #每个字符出现的次数都相同 s='llove' t='ovlle'
        m=len(s)
        n=len(t)
        if m!=n:
            print('false')
        else:
            l = ''
            flag = True
            for i in range(n):
                x = s[i]
                if x not in l:
                    l = ''.join([l, x])
                    k = str(s).count(x)
                    k1 = str(t).count(x)
                    if k1 == k:
                        pass
                    else:
                        flag = False
                        print('false')
                        break  # 终止循环,不可用于终止程序
            if flag:
                print('true')
        # sys.exit(0) #终止程序


    s='lolve'
    t='olvel'
    isAnagram(s,t)















