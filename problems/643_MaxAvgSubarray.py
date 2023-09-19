# A dynamic programming problem. A rolling sum  where we do sum = curSum + next - first would allow us to have an O(n) solution rather than an O(n * k) solution. The nk solution isn't that bad but I'll shoot for the optimization first here. 

# It looks like you don't need to calculate the average for each, iteration, just the summation. 
"""
start with [0:k - 1], get cursum. Say i = 0. Until the end pointer reaches the end, then we do:

sum[i:i + k - 1] <- this is the nk solution.

We can instead say i is the start pointer and i + k  is the end pointer. We subtract list[i] and add list[i + k] to get the new sum on each iteration. 

"""

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSum = sum(nums[0:k])
        maxSum = curSum
        startIndexOfMaxArray = 0
        i = 0
        while ((i + k - 1) < len(nums) - 1):
            i += 1
            curSum = curSum - nums[i - 1] + nums[i + k - 1]
            if curSum > maxSum:
                maxSum = curSum
                startIndexOfMaxArray = i
        
        return sum(nums[startIndexOfMaxArray: startIndexOfMaxArray + k])/k

