# 📘 Topic 1: Traverse an Array

# General Pattern
traverse_array(arr):
    for i in range(0, len(arr)):        # loop through array by index
        element = arr[i]                # access current element
        print(element)                  # operation on element (example: print)


------------------------------------------------
🔗 LeetCode Problems + Hints
------------------------------------------------

EASY
-----

1) 1480. Running Sum of 1d Array
Question: Given an array nums, return the running sum of nums where running_sum[i] = sum(nums[0]…nums[i]).

running_sum(arr):
    result = []                          # store prefix sums
    current = 0                          # running total
    for num in arr:                      # loop through array
        current += num                   # accumulate
        result.append(current)           # add to result
    return result


2) 1920. Build Array from Permutation
Question: Given a permutation array nums, build an array ans where ans[i] = nums[nums[i]].

build_array(nums):
    n = len(nums)
    result = [0]*n                       # placeholder array    !! can we use append ? 
    for i in range(n):                   # traverse indices
        result[i] = nums[nums[i]]        # map index → value → new index
    return result


3) 1929. Concatenation of Array
Question: Given an integer array nums, return the array ans of length 2n where ans[i] = nums[i] and ans[i+n] = nums[i].

get_concatenation(nums):
    return nums + nums                   # simply append same list twice  !! adding and concatenation of list ?


MEDIUM
------

1) 238. Product of Array Except Self
Question: Return array where result[i] = product of all elements except nums[i].

product_except_self(nums):
    n = len(nums)
    left = [1]*n                         # prefix product !! append ?
    right = [1]*n                        # suffix product
    
    for i in range(1, n):                # fill prefix
        left[i] = left[i-1] * nums[i-1]
    
    for i in range(n-2, -1, -1):         # fill suffix
        right[i] = right[i+1] * nums[i+1]
    
    result = [left[i]*right[i] for i in range(n)]
    return result


2) 442. Find All Duplicates in an Array
Question: Given an array, return all elements that appear twice.

find_duplicates(nums):
    result = []
    for num in nums:
        idx = abs(num) - 1               # map num → index
        if nums[idx] < 0:                # if already marked negative
            result.append(abs(num))      # duplicate found
        else:
            nums[idx] = -nums[idx]       # mark visited
    return result


3) 560. Subarray Sum Equals K
Question: Count the number of subarrays with sum equal to k.

subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    hashmap = {0:1}                      # prefix sum frequency
    
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in hashmap:    # check if valid subarray exists
            count += hashmap[prefix_sum - k]
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1
    return count
