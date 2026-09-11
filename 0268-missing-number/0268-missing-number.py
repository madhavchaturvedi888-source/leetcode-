class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        ans = n

        for i, num in enumerate(nums):
            ans ^= i ^ num

        return ans