"""
July 3, 2020
Prison Cells After N Days 
"""


class Solution:
    def nextday(self, cells):
        next_day_cells = [0] * 8
        for i in range(1, 7):
            if cells[i-1] == cells[i+1]:
                next_day_cells[i] = 1
            else:
                next_day_cells[i] = 0
        return next_day_cells

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = {}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = self.nextday(cells)

        return cells


# @lc code=end
