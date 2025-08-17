# Given an array of integers where 1 ≤ nums[i] ≤ n (with n = len(nums)), some elements appear twice and others appear once.
# Return all elements that appear twice.

# Input:  [4, 3, 2, 7, 8, 2, 3, 1]

arr = [4, 3, 2, 7, 8, 2, 3, 1,1,4]
trace=[]
duplicates = set()
for ele in arr:
    if ele in trace:
        duplicates.add(ele)
    trace.append(ele)

print(f'duplicates = {duplicates}')