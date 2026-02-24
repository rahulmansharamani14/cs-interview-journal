#Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
# 
#
#Example 1:
#
#
#Input: root = [3,9,20,null,null,15,7]
#Output: [3.00000,14.50000,11.00000]
#Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
#Hence return [3, 14.5, 11].
#Example 2:
#
#
#Input: root = [3,9,20,15,7]
#Output: [3.00000,14.50000,11.00000]


"""
Approach : BFS level order traversal

TC: O(N)
SC: O(N)

"""

from collections import deque

class TreeNode:
	def __init__(self, val = 0, left = None, right = None):
		self.val = val
		self.left = left
		self.right = right

def averageOfLevels(root: TreeNode) -> List[float]:
	
	if not root:
		return []
		
	res = []
	
	queue = deque([root])
	
	while queue:
		level_size = len(queue)
		level_sum = 0 
		
		for _ in range(level_size):
			node = queue.popleft()
			
			level_sum += node.val
			if node.left: queue.append(node.left)
			if node.right: queue.append(node.right)
		
		#compute level averge
		level_avg = level_sum / level_size
		res.append(level_avg)
		
	return res
	