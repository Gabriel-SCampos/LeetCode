from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique_nums = set(nums)

        min_operations = 0
        for num in unique_nums:
            if num < k:
                return -1
            if num == k:
                continue
            min_operations += 1

        return min_operations