#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#
#An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# 
#
#Example 1:
#
#Input: grid = [
#  ["1","1","1","1","0"],
#  ["1","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]
#]
#Output: 1
#Example 2:
#
#Input: grid = [
#  ["1","1","0","0","0"],
#  ["1","1","0","0","0"],
#  ["0","0","1","0","0"],
#  ["0","0","0","1","1"]
#]
#Output: 3
# 
#
#Constraints:
#
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 300
#grid[i][j] is '0' or '1'.

"""
Approach: Using Standard DFS in four directions

TC: O(m * n)
SC: O(m * n)
"""

def numIslands(grid: list[list[int]]) -> int:
	
	m, n = len(grid), len(grid[0])
	
	visited = set()
	island_count = 0
	
	
	def dfs_rec(r: int, c: int) -> None:
		visited.add((r,c))
		
		for dr, dc in [(-1,0), (0,-1), (0,1), (1,0)]:
			new_r = r + dr
			new_c = c + dc
			
			#check for out of bounce
			if new_r >= 0 and new_r < m and new_c >= 0 and new_c < n and (new_r, new_c) not in visited and grid[new_r][new_c] == "1":
				dfs_rec(new_r, new_c)
		
		pass 
	
	for i in range(m):
		for j in range(n):
			if (i, j) not in visited and grid[i][j] == "1":
				dfs_rec(i,j)
				island_count += 1
				
	return island_count
	

