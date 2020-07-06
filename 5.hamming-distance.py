"""
July 5, 2020
Hamming Distance
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        result = 0
        while x > 0 or y > 0:
            # Gives last digit of binary number
            result += (x % 2) ^ (y % 2)
            # Shift
            x >>= 1
            y >>= 1

        return result
