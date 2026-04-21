#You are given an m x n grid where each cell can have one of three values:
#
#0 representing an empty cell,
#1 representing a fresh orange, or
#2 representing a rotten orange.
#Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
#
#Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
#
# 
#
#Example 1:
#
#
#Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
#Output: 4

#Example 2:
#
#Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
#Output: -1
#Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

#Example 3:
#
#Input: grid = [[0,2]]
#Output: 0
#Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
# 
#
#Constraints:
#
#m == grid.length
#n == grid[i].length
#1 <= m, n <= 10
#grid[i][j] is 0, 1, or 2.



"""

Key Idea: Multi Source BFS

TC: O(m * n)
SC: O(m * n)

Example 1:
grid = [
[2, 1, 1]
[1, 1, 0]
[0, 1, 2]
]



Example 2:

grid = [
[2, 1, 1]
[0, 1, 1]
[1, 0, 1]
]
"""

from collections import deque

def orangesRotting(grid: list[list[int]]) -> int:
	
	ROWS, COLS = len(grid), len(grid[0])
	EMPTY, FRESH, ROTTEN = 0, 1, 2
	
	queue = deque()
	
	minute_count = 0
	fresh_count = 0
	
	#initialize the queue with rotten oranges
	for r in range(ROWS):
		for c in range(COLS):
			if grid[r][c] == ROTTEN:
				queue.append((r,c))
			if grid[r][c] == FRESH:
				fresh_count += 1
	
	if fresh_count == 0:
		return 0
	
	# Do Multi Source BFS per level
	while queue:
		for _ in range(len(queue)):
			curr_r, curr_c = queue.popleft()
		
			for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
				new_r = curr_r + dr
				new_c = curr_c + dc
			
				# check for out of bounce
				if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and grid[new_r][new_c] == FRESH:
					grid[new_r][new_c] = ROTTEN
					queue.append((new_r,new_c))
				
		minute_count += 1
		
	for r in range(ROWS):
		for c in range(COLS):
			if grid[r][c] == FRESH:
				return -1
		
	return minute_count -1

