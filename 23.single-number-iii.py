"""
July 23, 2020
Single Number III
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if nums == []:
            return []
        dic = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
        
        for i in dic:
            if dic[i] == 1:
                result.append(i)
                
        return result


