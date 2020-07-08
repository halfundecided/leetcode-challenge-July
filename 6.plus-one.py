"""
July 6, 2020
Plus One
"""


class Solution:
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
