class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binsearch(0, len(nums) - 1, target, nums)
        
        
        
    def binsearch(self, low, high, target, nums):
        if high < low:
            return low
            
        mid = (high + low)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binsearch(mid+1, high, target, nums)
            
        else:
            return self.binsearch(low, mid-1, target,nums)