class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        tempArray = s.split()
        if len(tempArray) == 0: 
            return 0
        else: 
            return len(tempArray[-1])