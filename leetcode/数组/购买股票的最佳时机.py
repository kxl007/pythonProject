class Solution(object):
    def maxProfit(prices):
        i=0
        n=len(prices)
        flag=True
        profit=0
        while i<n-1:
              if prices[i]<prices[i+1]:
                 flag=False
                 buyin=prices[i]
                 j=i+1
                 while j<n-1&prices[j]<prices[j+1]:
                     j+=1
                 i=j
                 soldout=prices[j]
                 profit+=soldout-buyin
              else:
                  i+=1

        if flag:
            profit=0
        return profit
    price=[7,6,5]
    maxProfit(price)





