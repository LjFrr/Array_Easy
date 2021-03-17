# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if (length == 0):
            return 0
        elif(length == 1):
            return numbers[0]
        else:
            # 初始化
            num = numbers[0]
            count = 1
            for i in range(1,length):
                if numbers[i] == num:
                    count += 1
                else:
                    count -= 1
                if count == 0:
                    num = numbers[i]
                    count = 1
            if(numbers.count(num) > len(numbers)/2):
                return num
            return 0
