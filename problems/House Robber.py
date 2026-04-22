#You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
#
# 
#
#Example 1:
#
#Input: nums = [1,2,3,1]
#Output: 4
#Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#Total amount you can rob = 1 + 3 = 4.
#Example 2:
#
#Input: nums = [2,7,9,3,1]
#Output: 12
#Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#Total amount you can rob = 2 + 9 + 1 = 12.
# 
#
#Constraints:
#
#1 <= nums.length <= 100
#0 <= nums[i] <= 400

"""

nums = [1,2,3,1]
n = 4


for n = 1, return 1
for n = 2, return max(nums[1], nums[2])
for n = 3, max()
"""

"""
Approach 1: Top Down recursion 
TC: O(2^n)
SC: O(n)
"""



def rob(nums: list[list[int]]) -> int:
	n = len(nums)
	
	def rob_rec(n: int) -> int:
		
		#base cases
		if n == 1: return nums[0]
		if n == 2: return max(nums[0], nums[1])
		
		#general case
		return max(rob_rec(n - 1) , rob_rec(n - 2) + nums(n))
		
		pass
		
	return rob_rec(n)



"""
nums= [1,2,3]

n = 3
rob_rec(2) -> 2
rob_rec(1) -> 1
rob_rec(3) -> max(2, 1 + 3) -> 4
"""

"""
Approach 2 Optimized: Top Down recursion with memoization
TC: O(n)
SC: O(n)
"""

def rob(nums: list[list[int]]) -> int:

	n = len(nums)
	memo = dict()
	
	def rob_rec(n: int) -> int:
		
		if n in memo: return memo[n]
		
		#base cases
		if n == 1: return nums[0]
		if n == 2: return max(nums[0], nums[1])
		
		#general case
		result = max(rob_rec(n - 1) , rob_rec(n - 2) + nums(n))
		memo[n] = result
		
		return result
		
	return rob_rec(n)


"""
Approach 3 Optimized: Bottom Up recursion with Tabulation
TC: O(n)
SC: O(n) only used for dp array
"""

def rob(nums: list[list[int]]) -> int:

	n = len(nums)
	dp = [0] * n
	
	#base cases
	if n == 1: return nums[0]
	if n == 2: return max(nums[0], nums[1])
	
	dp[0] = nums[0]
	dp[1] = max(nums[0], nums[1])
	
	for i in range(2, n):
		dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
	
	return dp[n - 1]
	
"""
Approach 3 Optimized: Bottom Up recursion with Tabulation
TC: O(n)
SC: O(1)
"""

def rob(nums: list[list[int]]) -> int:

	n = len(nums)
	
	#base cases
	if n == 1: return nums[0]
	if n == 2: return max(nums[0], nums[1])
	
	secondlast_rob = nums[0]
	last_rob = max(nums[0], nums[1])
	
	for i in range(2, n):
		curr_rob = max(last_rob, secondlast_rob + nums[i])
		secondlast_rob = last_rob
		last_rob = curr_rob
	
	
	return max(last_rob, secondlast_rob)
