class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        newArray = []
        newArray.append(0) 
        for i in digits:
            newArray.append(i)
        index = len(newArray) - 1
        
        if newArray[-1] == 9: 
            while(newArray[index] == 9):
                newArray[index] = 0 
                index -= 1
        newArray[index] += 1
        
        if newArray[0] == 0:
            del newArray[0]
            
        return newArray 
        