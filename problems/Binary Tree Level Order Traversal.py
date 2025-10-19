# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# Example 2:

# Input: root = [1]
# Output: [[1]]
# Example 3:

# Input: root = []
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000

# TC: O(n)
# SC: O(n/2) ~ O(n)

from collections import deque

class TreeNode:
    def __inti__(self, left=None, right=None, val):
        self.left = left
        self.right = right
        self.val = val

def levelOrder(root: TreeNode) -> list[int]:
    if not root:
        return []
    res = []
    queue = deque([root])

    while queue:
        level = []
        n = len(queue)

        for i in range(n):
            root = queue.popleft()
            level.append(root.val)
            if root.left:
                queue.append(root.left)
            if root.right:
                queue.append(root.right)
        if level:
            res.append(level)
    return res