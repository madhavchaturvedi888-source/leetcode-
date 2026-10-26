class Solution:
    def maxSumBST(self, root):
        self.ans = 0

        def dfs(node):
            if node is None:
             
                return True, float('inf'), float('-inf'), 0

            left_bst, left_min, left_max, left_sum = dfs(node.left)
            right_bst, right_min, right_max, right_sum = dfs(node.right)

            if left_bst and right_bst and left_max < node.val < right_min:
                total = left_sum + right_sum + node.val

                self.ans = max(self.ans, total)

                return (
                    True,
                    min(left_min, node.val),
                    max(right_max, node.val),
                    total
                )

        
            return False, 0, 0, 0

        dfs(root)
        return self.ans