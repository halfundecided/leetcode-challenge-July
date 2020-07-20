"""
July 19, 2020
Add Binary
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        binSum = bin(int(a, 2) + int(b, 2))
        binSum = binSum.replace('0b', '')
        
        return str(binSum)
