def binary_search(elements, target):
    low = 0
    high = len(elements)

    while low <= high:
            mid = (high + low)//2
            if elements[mid] == target:
                return mid
            elif elements[mid] < target:
                low = mid + 1
            else:
                high = mid
    return -1

nums = [1,2,5,6,7,10,14,19,20]
print(binary_search(nums, 7))
