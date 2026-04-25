#You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
#
#The area of an island is the number of cells with a value 1 in the island.
#
#Return the maximum area of an island in grid. If there is no island, return 0.
#
# 
#
#Example 1:
#
#
#Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#Output: 6
#Explanation: The answer is not 11, because the island must be connected 4-directionally.
#Example 2:
#
#Input: grid = [[0,0,0,0,0,0,0,0]]
#Output: 0
# 
#
#Constraints:
#
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 50
#grid[i][j] is either 0 or 1.

"""
Approach: Using Standard DFS in four directions

TC: O(m * n)
SC: O(m * n)
"""

def maxAreaOfIsland(grid: list[list[int]]) -> int:
	
	m, n = len(grid), len(grid[0])
	
	visited = set()
	island_count = 0
	max_island_area = 0
	
	
	def dfs_rec(r: int, c: int) -> int:
		island_area = 1
		visited.add((r,c))
		
		for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
			new_r = r + dr
			new_c = c + dc
			
			#check for out of bounce
			if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and (new_r, new_c) not in visited and grid[new_r][new_c] == 1:
				island_area += dfs_rec(new_r, new_c)
		
		return island_area

	
	for i in range(m):
		for j in range(n):
			if (i, j) not in visited and grid[i][j] == 1:
				max_island_area = max(max_island_area, dfs_rec(i,j))
				island_count += 1
				
	return max_island_area
	

