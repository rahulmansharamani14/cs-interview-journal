#Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
#
#A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#
# 
#
#Example 1:
#
#
#Input: root = [3,4,5,1,2], subRoot = [4,1,2]
#Output: true
#Example 2:
#
#
#Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#Output: false
# 
#
#Constraints:
#
#The number of nodes in the root tree is in the range [1, 2000].
#The number of nodes in the subRoot tree is in the range [1, 1000].
#-104 <= root.val <= 104
#-104 <= subRoot.val <= 104

"""
Approach: Recursive DFS 

if main tree has S nodes and another subtree has T nodes
TC: O(S*T)
SC: O(S+T)

"""

class TreeNode:
	def __init__(self, val = 0, left = None, right= None):
		self.val = val
		self.left = left
		self.right = right

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
	
	#helper method
	def _isSametree(root1: TreeNode, root2: TreeNode) -> bool:
		"""Return True if both trees are same, otherwise False"""
		if not root1 and not root2:
			return True
		
		if not root1 or not root2:
			return False
		
		if root1.val != root2.val:
			return False
		
		return (_isSametree(root1.left, root2.left) and 
			_isSametree(root1.right, root2.right))
		
	#base cases
	if not subRoot:
		return True
	
	if not root:
		return False
	
	if _isSametree(root, subRoot):
		return True
	
	return (isSubtree(root.left, subRoot) or
	isSubtree(root.right, subRoot))
		
		

