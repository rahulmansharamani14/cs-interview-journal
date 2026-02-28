#Given a binary tree, determine if it is height-balanced.
#
# 
#
#Example 1:
#
#
#Input: root = [3,9,20,null,null,15,7]
#Output: true
#Example 2:
#
#
#Input: root = [1,2,2,3,3,null,null,4,4]
#Output: false
#Example 3:
#
#Input: root = []
#Output: true
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [0, 5000].
#-104 <= Node.val <= 104


"""
Approach 1: Top Down Recursion

TC: O(n^2) in the worst case (skew tree)
SC: O(n) for recursive call stack


Approach 2: Bottom Up Recursion

TC: O(n)
SC: O(n) for recursive call stack
"""

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def isBalanced(root: TreeNode) -> bool:

	# dfs recursion
	def dfs(root) -> tuple(bool, int):
		
		# base case
		if not root:
			return (True, 0)
		
		left_subtree_balanced, left_subtree_height = dfs(root.left)
		right_subtree_balanced, right_subtree_height = dfs(root.right)
		
		#compute height from bottom
		height = 1 + max(left_subtree_height, right_subtree_height)
		
		# check if any subtree is not balanced
		if not left_subtree_balanced or not right_subtree_balanced:
			return [False, height]
		
		is_subtree_balanced = abs(left_subtree_height - right_subtree_height) <= 1
		
		return (is_subtree_balanced, height)
		

	return dfs(root)[0]



