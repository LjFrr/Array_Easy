# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0
        for i in data:
            if k == i:
                count += 1
        return count
