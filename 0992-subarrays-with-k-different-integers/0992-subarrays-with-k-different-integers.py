class Solution:
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            freq = {}
            left = 0
            ans = 0

            for right, num in enumerate(nums):
                freq[num] = freq.get(num, 0) + 1

                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)