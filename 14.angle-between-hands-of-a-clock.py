"""
July 14, 2020
Angle Between Hands of a Clock
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
            
        degreeM = minutes * 6
        degreeH = hour * 30 + minutes * 0.5
        option1 = abs(degreeM - degreeH)
        
        degreeM = 360 - minutes * 6
        degreeH = hour * 30 + minutes * 0.5
        option2 = degreeM + degreeH
        
        degreeM = minutes * 6
        degreeH = 360 - (hour * 30 + minutes * 0.5)
        option3 = degreeM + degreeH
        
        return min(option1, option2, option3)


