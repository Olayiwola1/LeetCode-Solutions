class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tempDict = {}
        
        for i in nums:
            if i in tempDict:
                tempDict[i] = i+1
            else:
                tempDict[i] = i
               
        for j in tempDict:
            if(tempDict[j] - j) == 0:
                return tempDict[j]