class Solution:
    def nextLargerNodes(self, head):
        values = []

        
        while head:
            values.append(head.val)
            head = head.next

        ans = [0] * len(values)
        stack = []

        
        for i, val in enumerate(values):
            while stack and values[stack[-1]] < val:
                idx = stack.pop()
                ans[idx] = val

            stack.append(i)

        return ans