"""
Obvious brute force solution is to calculate all the possible containers and get the max pair. 

Better solution- a 2 poiter solution. 

sleft = 0, right = end.
start with first rectangle as max.
iterate with left and right going inwards and calculating. Use flag to check if left or right should move on this iteration.

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        waterHeight = min(height[left], height[right])
        width = right - left

        maxWaterArea = waterHeight * width

        leftMoves = True
        while right - left > 0:
            width -= 1

            leftMoves = height[left] < height[right]

            if leftMoves:
                left += 1
            else:
                right -= 1
            
            waterHeight = min(height[left], height[right])
            curWaterArea = waterHeight * width

            if curWaterArea > maxWaterArea:
                maxWaterArea = curWaterArea
        
        return maxWaterArea



