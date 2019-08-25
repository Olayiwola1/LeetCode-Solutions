class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tempDict = {}
        for i in nums: 
            if i in tempDict: 
                tempDict[i] = tempDict[i] + 1
            else:
                tempDict[i] = 1
        
        for j in tempDict:
            if(tempDict[j] > len(nums)/2):
                return j