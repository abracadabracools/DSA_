# Problem: Subarray Sum Equals K
# Given an integer array nums and an integer k, find the total number of continuous subarrays whose sum equals to k.

# Great question!
#
# Let’s explore the **mathematical logic** behind the **efficient O(n)** approach to the **"Subarray Sum Equals K"** problem.
#
# ---
#
# ## ✅ The Core Idea: Prefix Sum
#
# Let’s define:
#
# * `prefix_sum[i]` = sum of the first `i` elements: `nums[0] + nums[1] + ... + nums[i]`
#
# Now, for a subarray `nums[i...j]`, its sum can be computed as:
#
# $$
# \text{sum(nums[i...j])} = \text{prefix\_sum}[j] - \text{prefix\_sum}[i - 1]
# $$
#
# This leads to the key observation:
#
# ---
#
# ### 🎯 Key Condition:
#
# To find if any subarray `nums[x...i]` sums to `k`:
#
# $$
# \text{current\_sum} - \text{previous\_prefix\_sum} = k
# \Rightarrow \text{previous\_prefix\_sum} = \text{current\_sum} - k
# $$
#
# So, as we iterate and build the **running sum**, we can just check:
#
# > Have we seen a prefix sum equal to `current_sum - k`?
#
# If **yes**, it means that there's a subarray ending at current index whose sum is `k`.
#
# ---
#
# ## 🧠 Prefix Sum Hash Map
#
# We use a hash map (dictionary) to store how many times each prefix sum has appeared so far.
#
# ```python
# prefix_sum_count = {0: 1}
# ```
#
# * We start with `0 → 1` because if the current sum itself is exactly `k`, it should count as a valid subarray.
#
# As we iterate:
#
# 1. Compute `current_sum += num`
# 2. Check if `current_sum - k` exists in the map
# 3. If it does, **add its count** to the result
# 4. Add/update `current_sum` in the map
#
# ---
#
# ## 🔁 Example Walkthrough
#
# ```python
# nums = [1, 2, 3], k = 3
# prefix_sum_count = {0: 1}
# ```
#
# ### Step-by-step:
#
# | Index | Num | Current Sum | Current Sum - K | Count Found | Map After Step       |
# | ----- | --- | ----------- | --------------- | ----------- | -------------------- |
# | 0     | 1   | 1           | -2              | 0           | {0:1, 1:1}           |
# | 1     | 2   | 3           | 0               | 1 ✅         | {0:1, 1:1, 3:1}      |
# | 2     | 3   | 6           | 3               | 1 ✅         | {0:1, 1:1, 3:1, 6:1} |
#
# **Result:** `2 subarrays` sum to `k = 3`
#
# ---
#
# ## 📌 Summary of Mathematical Logic
#
# * Every subarray sum can be written as the **difference of two prefix sums**.
# * By keeping track of previous prefix sums in a hash map, we can instantly know if such a subarray exists.
# * This avoids checking every pair (i, j), leading to an **O(n)** solution.
#
# ---
# Great question!
#
# Let’s explore the **mathematical logic** behind the **efficient O(n)** approach to the **"Subarray Sum Equals K"** problem.
#
# ---
#
# ## ✅ The Core Idea: Prefix Sum
#
# Let’s define:
#
# * `prefix_sum[i]` = sum of the first `i` elements: `nums[0] + nums[1] + ... + nums[i]`
#
# Now, for a subarray `nums[i...j]`, its sum can be computed as:
#
# $$
# \text{sum(nums[i...j])} = \text{prefix\_sum}[j] - \text{prefix\_sum}[i - 1]
# $$
#
# This leads to the key observation:
#
# ---
#
# ### 🎯 Key Condition:
#
# To find if any subarray `nums[x...i]` sums to `k`:
#
# $$
# \text{current\_sum} - \text{previous\_prefix\_sum} = k
# \Rightarrow \text{previous\_prefix\_sum} = \text{current\_sum} - k
# $$
#
# So, as we iterate and build the **running sum**, we can just check:
#
# > Have we seen a prefix sum equal to `current_sum - k`?
#
# If **yes**, it means that there's a subarray ending at current index whose sum is `k`.
#
# ---

## 🧠 Prefix Sum Hash Map
#
# We use a hash map (dictionary) to store how many times each prefix sum has appeared so far.
#
# ```python
# prefix_sum_count = {0: 1}
# ```
#
# * We start with `0 → 1` because if the current sum itself is exactly `k`, it should count as a valid subarray.
#
# As we iterate:
#
# 1. Compute `current_sum += num`
# 2. Check if `current_sum - k` exists in the map
# 3. If it does, **add its count** to the result
# 4. Add/update `current_sum` in the map
#
# ---
#
# ## 🔁 Example Walkthrough
#
# ```python
# nums = [1, 2, 3], k = 3
# prefix_sum_count = {0: 1}
# ```
#
# ### Step-by-step:
#
# | Index | Num | Current Sum | Current Sum - K | Count Found | Map After Step       |
# | ----- | --- | ----------- | --------------- | ----------- | -------------------- |
# | 0     | 1   | 1           | -2              | 0           | {0:1, 1:1}           |
# | 1     | 2   | 3           | 0               | 1 ✅         | {0:1, 1:1, 3:1}      |
# | 2     | 3   | 6           | 3               | 1 ✅         | {0:1, 1:1, 3:1, 6:1} |
#
# **Result:** `2 subarrays` sum to `k = 3`
#
# ---
#
# ## 📌 Summary of Mathematical Logic
#
# * Every subarray sum can be written as the **difference of two prefix sums**.
# * By keeping track of previous prefix sums in a hash map, we can instantly know if such a subarray exists.
# * This avoids checking every pair (i, j), leading to an **O(n)** solution.
#
# ---



def subarray_sum(nums, k):
    prefix_sum_count = {0: 1}  # prefix sum map: sum -> count
    count = 0
    current_sum = 0

    for num in nums:
        current_sum += num

        # Check if there is a prefix sum that when subtracted gives k
        if current_sum - k in prefix_sum_count:
            count += prefix_sum_count[current_sum - k]

        # Update prefix sum count
        prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

    return count
nums = [1, 2,2,1,1,1,3]
k = 3
print(subarray_sum(nums, k))  # Output: 2
