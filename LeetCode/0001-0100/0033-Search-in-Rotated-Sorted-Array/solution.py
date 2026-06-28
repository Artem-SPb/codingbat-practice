from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """
        Ищет целевое значение в повернутом отсортированном массиве за O(log n).
        Модифицированный бинарный поиск.
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Определяем, какая из половин массива строго отсортирована
            if nums[left] <= nums[mid]:
                # Левая половина отсортирована без разрывов
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Правая половина отсортирована без разрывов
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
