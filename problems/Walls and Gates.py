#You are given an m x n grid rooms initialized with these three possible values.
#
#-1 A wall or an obstacle.
#0 A gate.
#INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
#Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
#
# 
#
#Example 1:
#
#
#Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
#Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
#Example 2:
#
#Input: rooms = [[-1]]
#Output: [[-1]]
# 
#
#Constraints:
#
#m == rooms.length
#n == rooms[i].length
#1 <= m, n <= 250
#rooms[i][j] is -1, 0, or 231 - 1.


"""
Approach: Using Multi-source BFS on 2d Grid/Matrix

Key Idea: Doing BFS from all the gates all at once. Only adding coordinates to the queue if the room is empty (otherwise we already visited that room)

TC: O(m * n)
SC: O(m * n)
"""

from collections import deque

def wallsAndGates(rooms: list[list[int]]) -> None:

	ROWS, COLS = len(rooms), len(rooms[0])
	WALL, GATE, EMPTY = -1, 0, 2**31 - 1
	
	queue = deque()
	
	starting_dist = 0
	
	#intitalize queue with the gates coordinate
	for r in range(ROWS):
		for c in range(COLS):
			if rooms[r][c] == GATE:
				queue.append((r, c, starting_dist))
				
	#BFS using queue
	while queue:
		curr_r, curr_c, curr_dist = queue.popleft()
		
		for r , c in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
			new_r = r + curr_r
			new_c = c + curr_c
			
			#check out of bounce
			if (new_r >= 0 and new_r < ROWS) and new_c >= 0 and new_c < COLS and rooms[new_r][new_c] == EMPTY:
				rooms[new_r][new_c] = curr_dist + 1
				queue.append((new_r,new_c, curr_dist + 1))
				
			
