class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        max_val = max(nums)

        
        size = 1
        while size <= max_val:
            size *= 2

        tree = [0] * (2 * size)

        def query(left, right):
            
            left += size
            right += size

            ans = 0

            while left <= right:
                if left % 2 == 1:
                    ans = max(ans, tree[left])
                    left += 1

                if right % 2 == 0:
                    ans = max(ans, tree[right])
                    right -= 1

                left //= 2
                right //= 2

            return ans

        def update(pos, value):
            pos += size
            tree[pos] = max(tree[pos], value)

            pos //= 2

            while pos:
                tree[pos] = max(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2

        answer = 0

        for num in nums:
        
            
            left = max(1, num - k)
            right = num - 1

            best = query(left, right)
            current = best + 1

            update(num, current)

            answer = max(answer, current)

        return answer