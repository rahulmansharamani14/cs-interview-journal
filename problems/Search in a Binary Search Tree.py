# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
 
 

# Example 1:


# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
# Example 2:


# Input: root = [4,2,7,1,3], val = 5
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107


class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

def searchBST(root: TreeNode, val: int) -> TreeNode:
    """
        return: root of the subtree where the root node is equal to the give value


        - if the root node of tree is the target, we return the root
        - if the val of root node is greater than target, we search in left subtree recrusively
        - else we search in right subtree recrusively
        - if we don't find the target, we should return None

        TC: O(logn) and SC: O(logn)
    """

    if not root:
        return None
    if root.val == val:
        return root
    
    if root.val > val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)