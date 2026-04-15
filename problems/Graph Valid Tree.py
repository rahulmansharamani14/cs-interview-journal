"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

 

Example 1:


Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

{
	0 : [1,2,3],
	1 : [0, 4],
	2 : [0],
	3 : [0]
	4 : [1]
}



Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false



To verify a given a graph is tree/not, we can check for:
1. edge/node property: if a tree has n nodes, it should have n- 1 edges
2. it should be fully connected (meaning no cycles)


TC: O(V + E)
SC: O(V + E)

"""




from collections import defaultdict

def valid_tree(n : int, edges: list[list[tuple]]) -> bool:

	if n - 1 != len(edges):
		return False
	
	#build adjacency list
	graph = defaultdict(list)
	
	for u,v in edges:
		graph[u].append(v)
		graph[v].append(u)
	
	visited = set()
	
	def dfs_rec(node) -> None:
		visited.add(node)
		
		for neighbor in graph[node]:
			if neighbor not in visited:
				dfs_rec(neighbor)
		
	
	dfs_rec(0)
	return len(visited) == n
	


"""
visited = (0, 1, 4, 2, 3)

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

{
	0 : [1,2,3],
	1 : [0, 4],
	2 : [0],
	3 : [0]
	4 : [1]
}







Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false


{
	0 : [1]
	1 : [0, 2, 3, 4]
	2 : [1, 3]
	3 : [1, 2]
	4:  [1]

}


"""
