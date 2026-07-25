from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Сортировка слиянием (Merge Sort).
        Оптимальное решение для LeetCode, работающее за O(N log N) времени.
        """
        # Базовый случай рекурсии: массив из 1 (или 0)
        # элементов уже отсортирован
        if len(nums) <= 1:
            return nums

        # Шаг 1: Разделение (Divide)
        mid = len(nums) // 2
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])

        # Шаг 2: Слияние (Conquer)
        return self._merge(left_half, right_half)

    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Вспомогательная функция для слияния
        двух отсортированных массивов."""
        merged = []
        i, j = 0, 0

        # Используем два указателя, чтобы выбирать наименьший элемент
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # Если в одном из массивов остались элементы,
        # просто дописываем их в конец
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    assert solution.sortArray([5, 2, 3, 1]) == [1, 2, 3, 5], "Ошибка в тесте 1"
    assert solution.sortArray([5, 1, 1, 2, 0, 0]) == (
        [0, 0, 1, 1, 2, 5], "Ошибка в тесте 2")
    assert solution.sortArray([1, 2, 3, 4]) == [1, 2, 3, 4], "Ошибка в тесте 3"
    assert solution.sortArray([9, 8, 7, 6, 5]) == (
        [5, 6, 7, 8, 9], "Ошибка в тесте 4")
    assert solution.sortArray([42]) == [42], "Ошибка в тесте 5"

    print("Все тесты Merge Sort пройдены успешно!")
