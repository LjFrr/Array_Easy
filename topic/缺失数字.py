#
# 找缺失数字
# @param a int整型一维数组 给定的数字串
# @return int整型
#
class Solution:
    def solve(self , a ):
        # write code here
        preSum = (len(a) * (len(a) + 1)) / 2
        curSum = sum(a)
        return preSum - curSum
