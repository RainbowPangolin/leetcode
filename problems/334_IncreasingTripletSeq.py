"""
Naive solution:
For i in range len_nums
    for j in range i -> len_nums
        for k in range k -> len_nums
            if nums[i] < nums[j] < nums[k]
                return true



Optimal solution- two pointers. Med and Small. In order iteration of the list:

set element 0 to small. On each iteration, check if curElement is bigger than Small. If it is, set it to Med. If Med is set, check current element is bigger than med. If at any point, there exists something bigger than Med, then return true. 

"""

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = float('inf')
        medium = float('inf')
        small = nums[0]
        for num in nums:
            if num > medium:
                return True
            if num > small:
                medium = num
            elif num < small:
                small = num
        return False

