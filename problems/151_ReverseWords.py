#Given an input string s, reverse the order of the words.

# A two pass deque based solution:

from collections import deque
class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        
        while s[left] == ' ' and left <= right:
            left += 1
        while s[right] == ' ' and left <= right:
            right -= 1
            
        listOfWords = deque()
        curWord = []
        while left <= right:
            if (s[left] != ' '):
                curWord.append(s[left])
            elif (s[left] == ' ' and curWord):
                listOfWords.appendleft(''.join(curWord))
                curWord = []
            left += 1
        listOfWords.appendleft(''.join(curWord))

        return ' '.join(listOfWords)



# If you use built in functions, it's trivial

class SolutionAlt:
    def reverseWords(self, s: str) -> str:
        wordList = s.split()
        return ' '.join(reversed(wordList))