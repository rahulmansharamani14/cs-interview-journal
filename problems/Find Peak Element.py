# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

# You must write an algorithm that runs in O(log n) time.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 5
# Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

# Constraints:

# 1 <= nums.length <= 1000
# -231 <= nums[i] <= 231 - 1
# nums[i] != nums[i + 1] for all valid i.



# """
# Appraoch 1: Linear Scan (checking left and right neighbors). Edge cases with 1st and last element.
# TC: O(n)

# nums = [1] -> 1 (index 0)
# nums = [1,2] -> 2 (index 1)
# nums = [2,1] -> 2 (index 0)
# nums = [3,2,1] -> 3 (index 0)
# """

# def findPeakElement(nums: list[int]) -> int:
    
#     if len(nums) == 1:
#         return 0

#     if nums[0] > nums[1]:
#         return 0
#     if nums[-1] > nums[-2]:
#         return len(nums) - 1

#     for i in range(1, len(nums) - 1):
#         if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
#             return i

"""
Appraoch 2: Binary Search: Go to that half where the neigbor element is grater than middle
TC: O(logn)
"""

def findPeakElement(nums: list[int]) -> int:
    
    l , r = 0 , len(nums) - 1

    while l <= r:
        mid = l  + ((r - l) // 2)

        # check left side
        if mid > 0 and nums[mid] < nums[mid - 1]:
            r = mid - 1
        # check right side
        elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
            l = mid + 1
        # we found the peak element
        else:
            return mid
    
    