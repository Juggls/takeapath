
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dups = {}
        
        for idx,num in enumerate(nums):
            if num not in dups:
                dups[num] = [idx]
            else:
                dups[num].append(idx)
        
        for num in nums:
            dupls = dups[num]
            for i in range(0,len(dupls) -1):
                if dupls[i + 1] - dupls[i] <= k:
                    return True
                    
        
        return False
                
    
