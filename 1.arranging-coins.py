"""
July 1, 2020
Arranging Coins 
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        i = 1
        nums = -1
        while n >= 0:
            nums += 1
            n -= i
            i += 1
        return nums
