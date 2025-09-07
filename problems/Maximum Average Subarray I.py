# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000


# Constraints:

# n == nums.length
# 1 <= k <= n <= 105
# -104 <= nums[i] <= 104



# Clarifying Questions:
#
# Can there be a case where k > len(nums)? What would be appropriate return value?
#
# Approach:
# maintain a window of size k, maintianing the sum of k elements
# Drop the left value from the window by subtrcting it from the sum and add the right value to the window by adding to the sum
# Also maintain a max avg value (float), updating it for each window by comparing it to the current window avg
# Return the max avg value at the end
#
# TC: O(n) where n is len(nums)
# SC: O(1)
#


def findMaxAverage(nums: list[int], k: int) -> float:
    max_window_avg = float("-inf")

    l, r = 0, 0
    window_sum = 0

    while r < k:
        window_sum += nums[r]
        r += 1

    max_window_avg = window_sum/k

    while r < len(nums):
        window_sum -= nums[l]
        l += 1

        window_sum += nums[r]
        r += 1

        window_avg = window_sum/k
        max_window_avg = max(max_window_avg, window_avg)

    return max_window_avg
