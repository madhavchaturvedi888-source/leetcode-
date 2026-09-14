class Solution:
    def subarraysDivByK(self, nums, k):
        freq = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num
            rem = prefix % k

            if rem in freq:
                ans += freq[rem]

            freq[rem] = freq.get(rem, 0) + 1

        return ans