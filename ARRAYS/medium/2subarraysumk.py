# Let’s define:
#     prefix_sum[i] = sum of the first i elements: nums[0] + nums[1] + ... + nums[i]
# Now, for a subarray nums[i...j], its sum can be computed as:
#     sum(nums[i...j])=prefix_sum[j]−prefix_sum[i−1]
# To find if any subarray nums[x...i] sums to k:
#     current_sum  = previous_prefix_sum + k
#     ⇒ previous_prefix_sum = current_sum − k


nums = [1, 2,2,1,3]
k = 3
total_sum = 0

index_sum = {0:1}
count = 0
for i in nums:
    total_sum += i


    if total_sum - k in index_sum:
        count+=1

    index_sum[total_sum] = index_sum.get(total_sum, 0) + 1

print(f'The number of sub arrays = {count}')