# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.


# Approach: 
# - Construct an adjacency list out of the given edge list. 
# - Do a DFS (recursive/iterative) traversal from each unvisted node, while maintaining a visited node.
# - Each DFS would count as single connected component
# - Return the toal count of single connected component

# TC: O(n + edges) i.e. total no of nodes
# SC: O(n + edges) for adjacency list + O(n) for visited set + O(n) for max recursion depth ~ O(n + edges) 

# from collections import defaultdict

# def countComponents(self, n: int, edges: list[list[int]]) -> int:

#     graph = defaultdict(list)

#     for u , v in edges:
#         graph[u].append(v)
#         graph[v].append(u)

#     connected_component_count = 0

#     visited = set()

#     def dfs_recursive(node):

#         visited.add(node)

#         for neighbor_node in graph[node]:
#             if neighbor_node not in visited:
#                 dfs_recursive(neighbor_node)


#     for node in range(n):
#         if node not in visited:
#             dfs_recursive(node)
#             connected_component_count += 1

#     return connected_component_count

from collections import defaultdict

def countComponents(self, n: int, edges: list[list[int]]) -> int:

    graph = defaultdict(list)

    for u , v in edges:
        graph[u].append(v)
        graph[v].append(u)

    connected_component_count = 0

    visited = set()

    def dfs_iterative(node):
        stack = [node]
        visited.add(node)

        while stack:
            neighbor_node = stack.pop()

            for neighbor_node in graph[node]:
                if neighbor_node not in visited:
                    dfs_iterative(neighbor_node)


    for node in range(n):
        if node not in visited:
            dfs_iterative(node)
            connected_component_count += 1

    return connected_component_count