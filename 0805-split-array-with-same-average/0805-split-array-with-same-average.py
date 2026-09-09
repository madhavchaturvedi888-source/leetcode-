class Solution:
    def splitArraySameAverage(self, nums: list[int]) -> bool:
        n = len(nums)
        total = sum(nums)


        dp = [set() for _ in range(n // 2 + 1)]
        dp[0].add(0)

        for num in nums:
            for k in range(n // 2, 0, -1):
                for s in dp[k - 1]:
                    dp[k].add(s + num)

        
        for k in range(1, n // 2 + 1):
            if (total * k) % n == 0:
                target_sum = (total * k) // n

                if target_sum in dp[k]:
                    return True

        return False