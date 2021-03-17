#
# 最大乘积
# @param A int整型一维数组 
# @return long长整型
#
class Solution:
    def solve(self , A ):
        # write code here
        A.sort()
        return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])
