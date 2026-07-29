from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Находит непрерывный подмассив с наибольшей суммой.
        Использует Алгоритм Кадане (Kadane's Algorithm) за O(N).
        """
        max_sum = nums[0]
        current_sum = 0

        for num in nums:
            # Если накопленная сумма стала отрицательной,
            # она нам больше не поможет. Сбрасываем её.
            if current_sum < 0:
                current_sum = 0

            current_sum += num

            # Обновляем глобальный максимум на каждом шаге
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Массив со смешанными числами (отрицательными и положительными)
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == (
        6, "Ошибка в тесте 1")

    # Тест 2: Массив из одного элемента
    assert solution.maxSubArray([1]) == 1, "Ошибка в тесте 2"

    # Тест 3: Все числа положительные (должен взять весь массив)
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23, "Ошибка в тесте 3"

    # Тест 4: Все числа отрицательные
    # (должен взять одно наименьшее по модулю число)
    assert solution.maxSubArray([-5, -2, -9]) == -2, "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
