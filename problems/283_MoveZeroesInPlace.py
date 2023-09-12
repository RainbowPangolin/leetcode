# A sub optimal solution, since nums.pop is an O(n) operation when used the way I used it.

class SubOptimalSolution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        endOfArr = len(nums)
        i = 0
        while True: # probably better to do while true and do a spearate check inside using endOfArr
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                endOfArr -= 1
            else:
                i += 1

            if i >= endOfArr:
                break
                

# Better runtime than the above since it uses constant time operations.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroAt = 0

        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[lastNonZeroAt] = nums[i]
                lastNonZeroAt += 1
        
        for i in range(lastNonZeroAt, len(nums)):
            nums[i] = 0
                

    