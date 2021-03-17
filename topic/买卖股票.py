#
# 
# @param prices int整型一维数组 
# @return int整型
#
class Solution:
    def maxProfit(self , prices ):
        # write code here
        if len(prices) == 0:
            return 0
        minPrice = prices[0]
        profit = 0
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = max(profit, prices[i]-minPrice)
        return profit
