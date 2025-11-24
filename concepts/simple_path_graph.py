
# # Graph Path

# Given the adjacency list of an undirected graph, `graph`, and two distinct nodes, `node1` and `node2`, return a simple path from `node1` to `node2`.

# A _simple path_ does not repeat any nodes. Return an empty array if there is no path from `node1` to `node2`.

# Example 1:
# graph = [
#   [1],
#   [0, 2, 5, 4],
#   [1, 4, 5],
#   [],
#   [5, 2, 1],
#   [1, 2, 4]
# ]
# node1 = 0
# node2 = 4

# Output: [0, 1, 4]
# There are other valid answers, like [0, 1, 2, 5, 4].

# Example 2:
# graph = [
#   [1],
#   [0, 2, 5, 4],
#   [1, 4, 5],
#   [],
#   [5, 2, 1],
#   [1, 2, 4]
# ]
# node1 = 0
# node2 = 3

# Output: []
# There is no path to node 3.

# Example 3:
# graph = [
#   [1],
#   [0, 2],
#   [1]
# ]
# node1 = 0
# node2 = 2

# Output: [0, 1, 2]
# A simple path through all nodes.

# Here is a drawing of the graph from Example 1:

# https://iio-beyond-ctci-images.s3.us-east-1.amazonaws.com/graph-path-1.png

# Constraints:

# - `graph.length ≤ 1000`
# - `graph[i].length < 1000`
# - `0 ≤ graph[i][j] < graph.length`
# - `0 ≤ node1, node2 < graph.length`
# - `node1 != node2`
# - The adjacency list is properly formatted, with no parallel edges or self-loops


def simplePath(graph: list[list], node1: int, node2: int):
    result = []
    visited = set()


    def dfs(node):


        visited.add(node)
        result.append(node)

        if node == node2:
            return True

        for neighbor_node in graph[node]:
            if neighbor_node not in visited:
                if dfs(neighbor_node):
                    return True

        # update result array and visited set
        result.pop()
        visited.remove(node)
        return False


    if dfs(node1):
        return result
    else:
        return []
    