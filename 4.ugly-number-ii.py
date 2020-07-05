"""
July 4, 2020
Ugly Number II 
"""t


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        l1, l2, l3 = 0, 0, 0
        while n > 1:
            temp1 = ugly_numbers[l1] * 2
            temp2 = ugly_numbers[l2] * 3
            temp3 = ugly_numbers[l3] * 5

            minNum = min((temp1, temp2, temp3))

            if minNum == temp1:
                l1 += 1
            if minNum == temp2:
                l2 += 1
            if minNum == temp3:
                l3 += 1
            ugly_numbers.append(minNum)
            n -= 1

        return ugly_numbers[-1]
