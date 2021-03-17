#
# 
# @param A int整型一维数组 
# @param B int整型一维数组 
# @return void
#
class Solution:
    def merge(self , A, m, B, n):
        # write code here
        A[:] = A[:m] + B[:n]
        A.sort()
        return A
