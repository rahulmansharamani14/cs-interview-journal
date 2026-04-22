#You are climbing a staircase. It takes n steps to reach the top.
#
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# 
#
#Example 1:
#
#Input: n = 2
#Output: 2
#Explanation: There are two ways to climb to the top.
#1. 1 step + 1 step
#2. 2 steps
#Example 2:
#
#Input: n = 3
#Output: 3
#Explanation: There are three ways to climb to the top.
#1. 1 step + 1 step + 1 step
#2. 1 step + 2 steps
#3. 2 steps + 1 step
# 
#
#Constraints:
#
#1 <= n <= 45

"""
Approach 1: Dynamic Programming (Top Down)

Key idea: To reach any n stair, we need to look at no of ways we can reach it's last two steps

TC: O(2^n)
SC: O(n)
"""


def climbStairs(n: int) -> int:

	#base case
	if n == 1: return 1
	if n == 2: return 2
	
	#general case
	return climbStairs(n - 1) + climbStairs(n - 2)
	

"""
Approach 2: Dynamic Programmin (Top Down) - Recursion with Memoization

Key optimization idea: Store repeated computation in some kind of data structure

TC: O(n)
SC: O(n)
"""

def climbStairs(n : int) -> int:
	
	#define hashmap
	memo = dict()
	
	def climbStairs_rec(n: int) -> int:
		if n in memo: return memo[n]
		
		#base case
		if n == 1: return 1
		if n == 2: return 2
		
		#general case
		res = climbStairs_rec(n - 1) + climbStairs_rec(n - 2)
		
		memo[n] = res
		return res
		
	return climbStairs_rec(n)
	


