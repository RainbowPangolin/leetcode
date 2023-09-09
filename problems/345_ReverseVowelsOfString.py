# Given a string s, reverse only all the vowels in the string and return it.

# Naive solution- iterate through each letter. have 2 arrays- appended by end. One for each vowel, one for each vowel's position. Traverse the position in reverse order and p9ut the vowels in in-order from th eother array.

# Two pointer solution is better, but not asymptotically better. But I'll go with the two pointer solution anyway since it's still better by a constant factor > 2. 

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowelSet = set("aeiouAEIOU")
        
        startIndex = 0
        endIndex = len(s) - 1

        s = list(s)  # Convert the string to a list for in-place modification


        while startIndex < endIndex:
            while (startIndex < endIndex) and (s[startIndex] not in vowelSet):
                startIndex += 1

            while (startIndex < endIndex) and (s[endIndex] not in vowelSet):
                endIndex -= 1

            s[startIndex], s[endIndex] = s[endIndex], s[startIndex]

            startIndex += 1
            endIndex -= 1

        return ''.join(s)