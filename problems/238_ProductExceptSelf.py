"""
Naive solution:

answer = []
for i in range nums:
    for j in range nums:
        if j == i: 
            skip
        else:
            curProduct = nums[j] * curProduct
    answer[i] = curProduct 

return answer

But an O(n) solution exists. The division operation solution would go as follows:

Get product of entire array, excluding any 0's. If i is 0, mark that spot for later.
For each index, do totalproduct/element, and that is the value of that element in the array.
If 1 0 was marked, only that spot is not 0. If more, then entire array is 0. If no zeroes marked, follow above algorithm.


In the naive solution, we were repeating a lot of operations. Instead of doubly looping through the array which gets us a polynomial time solution, we can iterate through it simply twice, bearing a linear time solution. The first time, you have an array such that each index is the product up to that point from the left. Then another one for the right. Then you just multiply L and R. 
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L = [0] * len(nums)
        L[0] = 1
        R = [0] * len(nums)
        R[len(nums) - 1] = 1

        # cumulativeLeftProduct = 1 
        for i in range(1, len(nums)):
            # cumulativeLeftProduct = nums[i-1] * cumulativeLeftProduct
            # L[i] = cumulativeLeftProduct
            L[i] = nums[i-1] * L[i-1]

        for i in reversed(range(0, len(nums)-1)):
            R[i] = nums[i + 1] * R[i + 1]

        product = [0] * len(nums)
        for i in range(0, len(nums)):
            product[i] = L[i] * R[i]

        return product