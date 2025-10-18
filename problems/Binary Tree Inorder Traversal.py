# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:

# Input: root = [1,null,2,3]

# Output: [1,3,2]

# Explanation:



# Example 2:

# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,2,6,5,7,1,3,9,8]

# Explanation:



# Example 3:

# Input: root = []

# Output: []

# Example 4:

# Input: root = [1]

# Output: [1]

 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Inorder: left, Node, right


class TreeNode:
    def __init__(self, left=None, right=None, val):
        self.left = left
        self.right = right
        self.val = val
    
# def inorderTraversal(root: TreeNode) -> list[int]:

#     res = []

#     def dfs(root):
#         if not root:
#             return
#         dfs(root.left)
#         res.append(root.val)
#         dfs(root.right)
    
#     dfs(root)
#     return res
        
# Follow up: Recursive solution is trivial, could you do it iteratively?

def inorderTraversal(root: TreeNode) -> list[int]:
    if not root:
        return []
    
    stack = []
    curr = root
    res = []

    while stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr)
        curr = curr.right
        
    return res
    
