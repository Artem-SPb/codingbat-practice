from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Решает задачу "Trapping Rain Water" с использованием двух указателей.

        Сложность по времени: O(n)
        Сложность по памяти: O(1)
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0

        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]

        return water
