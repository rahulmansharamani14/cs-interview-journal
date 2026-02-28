#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
#
# 
#
#Example 1:
#
#
#Input: p = [1,2,3], q = [1,2,3]
#Output: true
#Example 2:
#
#
#Input: p = [1,2], q = [1,null,2]
#Output: false
#Example 3:
#
#
#Input: p = [1,2,1], q = [1,1,2]
#Output: false
# 
#
#Constraints:
#
#The number of nodes in both trees is in the range [0, 100].
#-104 <= Node.val <= 104


"""
Approach: Top Down Recursion

Traverse through the tree at the same time recrustively.

TC: O(n)
SC: O(n)
"""


class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
	
	# both root are None
	if not p and not q:
		return True
	
	# one root is None
	if not p or not q:
		return False
	
	if p.val != q.val:
		return False
	
	
	left_subtree  = isSameTree(p.left, q.left)
	right_subtree = isSameTree(p.right, q.right)
	
	return left_subtree and right_subtree

