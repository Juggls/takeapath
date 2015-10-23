import sys
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxlist = []
        
        while True:
            max = -sys.maxint
            for num in nums:
                if num > max:
                    max = num
            
            maxlist.append(max)
            nums.remove(max)
            
            if(len(maxlist) == k):
                return maxlist[len(maxlist)-1]
        
            
           