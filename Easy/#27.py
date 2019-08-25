class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = len(nums)
        index = 0
        for i in range(len(nums)):
            if nums[index] == val:
                del nums[index]
                counter -= 1
            else: 
                index += 1
        return counter 
        