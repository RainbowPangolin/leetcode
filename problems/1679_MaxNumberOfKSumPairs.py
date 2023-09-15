"""
Hash table solution might work- put k - element into hash set, and if it appears later, then remove from set and increment number of ops. 

"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        num_counts = {}  # Dictionary to store counts of each number in nums
        # A plain set() will not do, since it would fail the case such as [1,1,2,2] k = 3 
        ops = 0

        for num in nums:
            # Check if the complementary number (k - num) exists in the dictionary
            if k - num in num_counts and num_counts[k - num] > 0:
                ops += 1
                num_counts[k - num] -= 1
            else:
                # Increment the count of the current number in the dictionary
                if num in num_counts:
                    num_counts[num] += 1
                else:
                    num_counts[num] = 1

        return ops