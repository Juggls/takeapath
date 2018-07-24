from collections import defaultdict
def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    sums = defaultdict(list)
    
    quads = set()
    
    for i in xrange(len(nums)):
        for j in xrange(i + 1, len(nums)):
            curr_sum = nums[i] + nums[j]
            if (target - curr_sum) in sums:
                for pair in sums[target-curr_sum]:
                    quad = set([x for x in pair]) | set([i, j])
                    if len(quad) == 4:
                        quad = tuple(sorted([nums[x] for x in quad]))
                        quads.add(quad)
                                     
            sums[curr_sum].append((i, j))
            
    return list(quads)
        
def main(): 
    print(fourSum([1, 0, -1, 0, -2, 2], 0))
    
main()
                         
