class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = 0
        
        for num in nums:
            if num != 0:
                nums[x] = nums[y]
                x = x + 1
            y = y + 1
            
        for i in range(x, len(nums)):
            nums[i] = 0 
        
