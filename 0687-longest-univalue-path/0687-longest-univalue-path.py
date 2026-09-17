class Solution:
    def longestUnivaluePath(self, root):
        self.ans = 0

        def dfs(node):
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            left_path = 0
            right_path = 0

            if node.left and node.left.val == node.val:
                left_path = left + 1

            if node.right and node.right.val == node.val:
                right_path = right + 1

            self.ans = max(self.ans, left_path + right_path)

            return max(left_path, right_path)

        dfs(root)
        return self.ans