"""
July 17, 2020
Top K Frequent Elements
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if nums == []:
            return []
        if len(nums) == k:
            return nums
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
                
        sortedDic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        result = []
        for i in range(0, k):
            result.append(sortedDic[i][0])
        
        return result


