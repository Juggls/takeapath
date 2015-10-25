class Solution(object):
    
    #terribly sloppy O(n) solution
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0 or sum(nums) < s:
            return 0
        
        
        minlength = 1
        start = 0
        end = 0
        summy = 0

        #get the first subarray which exceeds s
        for i in range(len(nums)):
            summy += nums[i]
            if summy >= s:
                end = i
                minlength = i + 1
                break
            
        #after first subarray, iterate through rest, noting if you can ever get a subarray below minlength
        currlength = minlength
        currstart = end - minlength + 1
        

        while end < len(nums):
            summy -= nums[currstart]
            while(summy < s):
                end += 1
                if(end >= len(nums)):
                    currlength+=1
                    break
                
                summy += nums[end]
                currlength += 1
                print currlength
                
            currstart +=1
            currlength -= 1 
            
            if currlength < minlength:
                minlength = currlength
        
        return minlength
            