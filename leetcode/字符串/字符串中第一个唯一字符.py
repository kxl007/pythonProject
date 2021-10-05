

class Solution(object):
    def firstUniq(s):
        n=len(s)
        m=''
        flag=False
        for i in range(n):
            k=0
            x=s[i]
            if x not in m :
                m=''.join([m,x])
                for j in range(n):
                    if x == s[j]:
                        k += 1
                    if k > 1:
                        break
                if k == 1:
                    flag=True
                    print(i)
                    break
            if x in m and len(m)==26:
                print(-1)
                break
        if not flag:
            print(444)

    s='loveleetcode'
    firstUniq(s)










