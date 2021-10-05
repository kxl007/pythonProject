class Solution(object):
    def countAndSay(n):
        s=['1']
        for i in range(10):
            x = s[len(s) - 1]
            x1 = ''
            i = 0

            while (i < len(x)):
                y = x[i]
                k = 0
                for j in range(i, len(x)):
                    if y == x[j]:
                        i += 1
                        k += 1
                    else:
                        break
                x1 = ''.join([x1,str(k) + str(y)])
            s.append(x1)
        print(s)
        print(s[n-1])

    n=4
    countAndSay(n)




