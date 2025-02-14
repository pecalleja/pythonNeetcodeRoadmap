from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                left = m + 1
            else:
                right = m - 1
        return -1
