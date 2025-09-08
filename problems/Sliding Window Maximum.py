# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.



# Example 1:

# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length
#
# Approach:
#
# We would use a doubly ended queue to maintain the window and push only the current max element in the window so that we don't have to scan the window once again to compute max
#
# TC: O(n)
# SC: O(k)

from collections import deque

def maxSlidingWindow(nums: list[int], k : int) -> list[int]:
    res = []

    window = deque()


    for i in range(k):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    res.append(nums[window[0]])

    for i in range(k, len(nums)):
        if window and window[0] == i - k:
            window.popleft()

        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)
        res.append(nums[window[0]])


    return res
