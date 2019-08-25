class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # approach from the front and back, then compare
        Front = 0 
        Back = len(str(x))-1
       
        for i in range(len(str(x))//2):
            if str(x)[Front] == str(x)[Back]:
                Front += 1
                Back -= 1
                continue
            else:
                return False 
        return True 