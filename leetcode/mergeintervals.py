class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return intervals
        if len(intervals) == 1:
            return intervals
        
        sorted_intervals = sorted(intervals, key=lambda x: (x.start, x.end))
        merged_intervals = [sorted_intervals[0]]
        
        for idx, interval in enumerate(sorted_intervals):
            if interval.start <= merged_intervals[-1].end:
                merged_intervals[-1].end = max(interval.end, merged_intervals[-1].end)
            else:
                merged_intervals.append(interval)
                
        return merged_intervals
