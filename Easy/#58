class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0 
        keeper = 0
       
        if len(s) == 0:
            return 0 
        
        if s[-1] == ' ':
            for j in range(len(s)-1, 0, -1):
                if s[j] != ' ':
                    break
                else:
                    keeper += 1
    
        for i in range(len(s)-keeper-1, -1, -1):
            if s[i] != ' ':
                count += 1
            else:
                return count 
        return count 