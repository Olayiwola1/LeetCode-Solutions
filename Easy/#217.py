class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tempDict = {}
        
        for i in nums:
            if i in tempDict:
                tempDict[i] += 1
            else:
                tempDict[i] = i
        
        for j in tempDict:
            if (tempDict[j] - j) > 0:
                return True 
        return False 