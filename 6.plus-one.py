#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start


class Solution:
    # My 1st Solution: Naive Approach, but beats 99%
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        output = []
        for i in digits:
            string += str(i)
        print(int(string))
        result = int(string) + 1
        for i in str(result):
            output.append(i)
        return output


# @lc code=end
