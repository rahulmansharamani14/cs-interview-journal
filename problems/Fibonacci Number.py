# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

 

# Example 1:

# Input: n = 2
# Output: 1
# Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
# Example 2:

# Input: n = 3
# Output: 2
# Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
# Example 3:

# Input: n = 4
# Output: 3
# Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

# Constraints:

# 0 <= n <= 30

"""
Approach 1: Using Recursion

TC: O(n)
SC: O(n) for max recursion depth
"""

def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return self.fib(n - 1) + self.fib(n - 2)


"""
Approach 2: Dynamic Programming (Top Down Approach: Memoization)

TC: O(n)
SC: O(n) for memo/cache
"""

def fib(self, n: int) -> int:
    """
    Top Down Memoization Technique
    """

    memo = {0: 0, 1: 1} #base cases

    def f(x: int) -> int:
        if x in memo:
            return memo[x]
        else:
            memo[x] = f(x-1) + f(x-2)
            return memo[x]

    return f(n)

"""
Approach 3: Dynamic Programming (Bottom Up Approach: Tabulation)
TC: O(n)
SC: O(n) for dp array (tabulization)

"""

def fib(self, n: int) -> int:

    #base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1) #initializing dp array

    dp[0], dp[1] = 0, 1 #fill up base case values

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] #tabulation part
    
    return dp[n]

"""
Approach 4: Optimizing Space with Bottom Up Approach with Variables
TC: O(n)
SC: O(1)
"""

def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    second_last = 0
    last = 1
    curr = 0

    for i in range(2, n + 1):
        curr = last + second_last
        second_last = last
        last = curr

    return curr