#Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
#
# 
#
#Example 1:
#
#
#Input: root = [3,1,4,null,2], k = 1
#Output: 1
#Example 2:
#
#
#Input: root = [5,3,6,2,4,null,null,1], k = 3
#Output: 3
# 
#
#Constraints:
#
#The number of nodes in the tree is n.
#1 <= k <= n <= 104
#0 <= Node.val <= 104
# 
#
#Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?



"""
Approach: Traverse the BST in-order and create an array out of it

TC: O(n)
SC: O(n)
"""

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
	
	
	array = []
	
	def inorder(root: TreeNode):
		if not root:
			return
		
		inorder(root.left)
		array.append(root.val)
		inorder(root.right)
	
	inorder(root)
	return array[k-1]
	


