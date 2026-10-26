class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root):
            result = []

            def dfs(node):
                if node is None:
                    return

                dfs(node.left)
                result.append(node.val)
                dfs(node.right)

            dfs(root)
            return result

        a = inorder(root1)
        b = inorder(root2)

        
        i = 0
        j = 0
        ans = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                ans.append(a[i])
                i += 1
            else:
                ans.append(b[j])
                j += 1

        while i < len(a):
            ans.append(a[i])
            i += 1

        while j < len(b):
            ans.append(b[j])
            j += 1

        return ans