#
# 
# @param numbers int整型一维数组 
# @param target int整型 
# @return int整型一维数组
#
class Solution:
    def twoSum(self , numbers , target ):
        # write code here
        res = [0,0]#保存结果
        mp = {}#定义一个哈希表存储numbers[i]和对应的下标
        for i in range(len(numbers)):#进行标记
            mp[numbers[i]] = i
        for i in range(len(numbers)):
             #每遍历一个numbers[i]就去对应的mp里找有没有target - numbers[i]
             #如果有就返回结果
             #如果没有就找下一个
            if target - numbers[i] in mp:
                if mp[target - numbers[i]] != i:
                    res[0] = i + 1
                    res[1] = mp[target - numbers[i]] + 1
                    return res
        return res
