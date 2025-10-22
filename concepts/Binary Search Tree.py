

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node: TreeNode):
        if not self.root:
            self.root = node
            return

        def recursiveInsert(root: TreeNode):
            if not root:
                return node
            if node.val < root.val:
                root.left = recursiveInsert(root.left)
            else:
                root.right = recursiveInsert(root.right)
            return root
            
        recursiveInsert(self.root)

    def printTree(self, root:TreeNode):

        if not root:
            return
        self.printTree(root.left)
        print(root.val)
        self.printTree(root.right)

    def delete(self, val: int):
        pass

    def search(self, val: int) -> bool:
        pass

if __name__ == "__main__":
    bst = BST()
    bst.insert(TreeNode(5))
    bst.insert(TreeNode(3))
    bst.insert(TreeNode(7))
    bst.insert(TreeNode(8))
    bst.printTree(bst.root)