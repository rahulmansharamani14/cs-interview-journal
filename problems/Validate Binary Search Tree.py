#Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
#A valid BST is defined as follows:
#
#The left subtree of a node contains only nodes with keys strictly less than the node's key.
#The right subtree of a node contains only nodes with keys strictly greater than the node's key.
#Both the left and right subtrees must also be binary search trees.
# 
#
#Example 1:
#
#
#Input: root = [2,1,3]
#Output: true
#Example 2:
#
#
#Input: root = [5,1,4,null,null,3,6]
#Output: false
#Explanation: The root node's value is 5 but its right child's value is 4.
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [1, 104].
#-231 <= Node.val <= 231 - 1


"""
Approach: Recursive DFS

TC: O(n)
SC: O(n)
"""

 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isValidBST(root: TreeNode) -> bool:
	
	def dfs(node: TreeNode, left_boundary, right_boundary):
		if not node:
			return True
			
		if not (node.val > left_boundary and node.val < right_boundary):
			return False
		
		# recursively traverse through left subtree and right subtree
		return (dfs(node.left, left_boundary, node.val) and
		dfs(node.right, node.val, right_boundary))
		
	left_boundary = float("-inf")
	right_boundary = float("inf")
	
	return dfs(root, left_boundary, right_boundary)
		
