# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
 

# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100


"""
Initial Thoughts: 
- For each valid index in our answer list, we can iterate the temperatures list until we get a warmer temperature

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]


temperatures = [73,74,75,71,69,72,76,73]
index i      = [0, 1, 2, 3, 4, 5, 6, 7]
ans          = [1, 1, 4, 2, 1, 1, 0, 0]


TC: O(n^2)
SC: O(n)
"""

# def dailyTemperatures(temperatures: list[int]) -> list[int]:
#     ans = [0] * len(temperatures)

#     for i in range(len(temperatures)):
#         for j in range(i + 1, len(temperatures)):
#             if temperatures[i] < temperatures[j]:
#                 ans[i] = j - i
#                 break

#     return ans

"""
Optimization: Use Monotonic Stack

TC: O(n)
SC: O(n) in the worst case
"""

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    ans = [0] * len(temperatures)

    stack = []

    for curr_index in range(len(temperatures)):
        curr_temp = temperatures[curr_index]

        while stack and curr_temp > stack[-1][0]:
            old_temp , prev_index = stack.pop()
            ans[prev_index] = curr_index - prev_index

        stack.append((curr_temp, curr_index))
    return ans