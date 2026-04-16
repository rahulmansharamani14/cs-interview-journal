"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.


Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Input: numCourses = 3, prerequisites = [[1,0],[2,1],[1,2]]
Output: false

"""

"""
Approach 1: Using DFS (to detect cycles)

TC: O(numCourses + len(prerequisites))
SC: O(numCourses + len(prerequisites))
"""


from collections import defaultdict

def canFinish(numCourses: int, prerequisites: list[list[int]]):
	
	if not len(prerequisites):
		return True
	
	#build adjancey list
	graph = defaultdict(list)
	
	for u,v in prerequisites:
		graph[u].append(v)
	
	visited = set()
	
	def dfs_rec(node) -> bool:
		if node in visited:
			return False
		
		if not graph[node]:
			return True
		
		visited.add(node)
		
		for nei in graph[node]:
			if not dfs_rec(nei):
				return False

		visited.remove(node)
		graph[node] = []
		
		return True
	
	for i in range(numCourses):
		if not dfs_rec(i):
			return False
	
	return True
	
	

