# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def isValidBST(self, root):
    # recursive helper fn to check left and right
    def dfs(node, min_node, max_node):
        if not node:
            return True

        if min_node and min_node.val >= node.val:
            return False

        if max_node and max_node.val <= node.val:
            return False

        return dfs(node.right, node, max_node) and dfs(node.left, min_node, node)

    return dfs(root, None, None)
