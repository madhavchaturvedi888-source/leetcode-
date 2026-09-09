import heapq

class Solution:
    def smallestRange(self, nums):
        k = len(nums)

        heap = []
        current_max = float('-inf')

        
        for i in range(k):
            heapq.heappush(heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        best_left = heap[0][0]
        best_right = current_max

        while True:
            current_min, list_idx, element_idx = heapq.heappop(heap)

            
            if current_max - current_min < best_right - best_left:
                best_left = current_min
                best_right = current_max

            if element_idx + 1 == len(nums[list_idx]):
                break

          
            next_value = nums[list_idx][element_idx + 1]

            heapq.heappush(
                heap,
                (next_value, list_idx, element_idx + 1)
            )

            current_max = max(current_max, next_value)

        return [best_left, best_right]