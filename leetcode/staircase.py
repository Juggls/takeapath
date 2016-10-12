class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways = {}
        return self.climb_helper(n, ways)
    
    def climb_helper(self, n, ways):
        if n <= 0:
            return 0 
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n-1 in ways:
                prev_1 = ways[n-2]
            else:
                prev_1 = self.climb_helper(n-1, ways)
            
            if n-2 in ways:
                prev_2 = ways[n-2]
            else:
                prev_2 = self.climb_helper(n-2, ways)
                
            num_ways = prev_1 + prev_2
            ways[n] = num_ways
            return num_ways
    
