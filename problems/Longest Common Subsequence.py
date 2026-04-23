#Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
#
#A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
#
#For example, "ace" is a subsequence of "abcde".
#A common subsequence of two strings is a subsequence that is common to both strings.
#
# 
#
#Example 1:
#
#Input: text1 = "abcde", text2 = "ace" 
#Output: 3  
#Explanation: The longest common subsequence is "ace" and its length is 3.
#Example 2:
#
#Input: text1 = "abc", text2 = "abc"
#Output: 3
#Explanation: The longest common subsequence is "abc" and its length is 3.
#Example 3:
#
#Input: text1 = "abc", text2 = "def"
#Output: 0
#Explanation: There is no such common subsequence, so the result is 0.
# 
#
#Constraints:
#
#1 <= text1.length, text2.length <= 1000
#text1 and text2 consist of only lowercase English characters.


"""
Approach: Dynamic Programming

TC: O(m * n)
SC: O(m * n)

"""

def longestCommonSubsequence(text1: str, text2: str) -> int:
	
	ROWS, COLS = len(text1), len(text2)
	
	#initialize dp 2d array
	dp = [[0] * (COLS + 1) for _ in range (ROWS + 1)]
	
	dp[0][0] = 0
	
	for i in range(1, ROWS + 1):
		for j in range(1, COLS + 1):
			if text1[i - 1] == text2[j - 1]:
				#current char matches, found new longest commom subsequence
				dp[i][j] = dp[i - 1][j - 1] + 1
			else:
				#current char matches, track prev longest common subsequence
				dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
	
	return dp[ROWS][COLS]

