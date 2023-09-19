# easy brute force solution- calculate all the altitudes, then look for max altitude.

# Checking for the highest altitude as the altitudes are being calculated is probably the same number of calculations so it might not be any more efficient. But it would probably look nicer.

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for i in range(1, len(gain) + 1):
            altitudes.append(gain[i - 1] + altitudes[i - 1])
            
        return max(altitudes)