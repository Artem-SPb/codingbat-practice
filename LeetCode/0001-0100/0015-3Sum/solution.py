from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Находит все уникальные триплеты, сумма которых равна 0.
        Использует сортировку и паттерн двух указателей.

        Сложность по времени: O(N^2)
        Сложность по памяти: O(N) для сортировки
        """
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Если минимальное из оставшихся чисел больше нуля,
            # сумма трех чисел никогда не будет равна 0
            if a > 0:
                break

            # Пропускаем одинаковые фиксированные числа,
            # чтобы избежать дубликатов в ответе
            if i > 0 and a == nums[i - 1]:
                continue

            # Запускаем поиск двух указателей для оставшейся части массива
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = a + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    # Нашли подходящий триплет
                    res.append([a, nums[left], nums[right]])

                    # Сдвигаем левый указатель для поиска других комбинаций
                    left += 1

                    # Пропускаем одинаковые элементы для левого указателя
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res
