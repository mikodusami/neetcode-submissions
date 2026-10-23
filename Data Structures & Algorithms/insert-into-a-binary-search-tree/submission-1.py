# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        # input: root node, value to insert into a BST
        # output: the new value to be inserted into a BST (BST property is every node is the left tree follows a less than nature, the right tree follows a greater than,=)
        # inspect: every node: follow valid condition until you find the right location, you know you have found the right location when there is no node greater than ListNode(val) and less than ListNode(val)
        # remember: how to insert a node: create the LIstNode(val), point the parent node to the new node and the ListNode(val) to the current, so we have to remember the parent node?

        if not root:
            return TreeNode(val)

        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root