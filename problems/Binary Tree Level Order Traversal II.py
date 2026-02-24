#Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).
#
# 
#
#Example 1:
#
#
#Input: root = [3,9,20,null,null,15,7]
#Output: [[15,7],[9,20],[3]]
#Example 2:
#
#Input: root = [1]
#Output: [[1]]
#Example 3:
#
#Input: root = []
#Output: []
# 
#
#Constraints:
#
#The number of nodes in the tree is in the range [0, 2000].
#-1000 <= Node.val <= 1000


"""
Approach 1: Do a normal BFS level order traversal then reverse the result list

TC: O(N) for processing every node + O(N) for reversing res list ~ O(N)
SC: O(N) for queue in worst case + O(N) for res list ~ O(N)


Approach 2: Add levels in the result queue instead of list


TC: O(N) for processing every node + O(N) for converting queue to list ~ O(N)
SC: O(N) for queue in worst case + O(N) for res list ~ O(N)
"""

from collections import deque

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def levelOrderBottom(root: TreeNode) -> list[list[int]]:

	if not root:
		return []
		
	res = deque()
	
	queue = deque([root])
	
	while queue:
		level_size = len(queue) #capture the level size
		level = []
		
		#visit every node from the same level
		for _ in range(level_size):
			node = queue.popleft()
			
			level.append(node.val)
			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)
		
		#append level to result queue from left side to maintain down to up order
		res.appendleft(level)
	
	return list(res)

	
