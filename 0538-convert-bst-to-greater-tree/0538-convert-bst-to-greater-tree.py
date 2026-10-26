class Solution:
    def convertBST(self, root):
        self.sum = 0

        def reverse_inorder(node):
            if node is None:
                return

            
            reverse_inorder(node.right)

            self.sum += node.val
            node.val = self.sum

            reverse_inorder(node.left)

        reverse_inorder(root)
        return root