from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Находит количество непрерывных подмассивов с суммой k.
        Использует паттерн Prefix Sum (префиксные суммы)
        в комбинации с Hash Map.

        Сложность по времени: O(N)
        Сложность по памяти: O(N)
        """
        count = 0
        current_sum = 0

        # Словарь для хранения частоты префиксных сумм.
        # Базовый случай: сумма 0 встретилась 1 раз (до начала массива).
        prefix_sums = {0: 1}

        for num in nums:
            current_sum += num

            # Если (текущая_сумма - k) уже встречалась ранее,
            # значит подмассив между той старой суммой и текущей дает ровно k.
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]

            # Записываем текущую префиксную сумму в словарь
            # для использования на следующих шагах цикла.
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Классический случай из примера
    assert solution.subarraySum([1, 1, 1], 2) == 2, "Ошибка в тесте 1"

    # Тест 2: Элементы могут образовывать подмассив разными способами
    assert solution.subarraySum([1, 2, 3], 3) == 2, "Ошибка в тесте 2"

    # Тест 3: Массив с отрицательными числами
    assert solution.subarraySum([1, -1, 1, 1, 1, -1], 2) == (
        4, "Ошибка в тесте 3")

    # Тест 4: Искомая сумма k совпадает с одним элементом в массиве
    assert solution.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7) == (
        4, "Ошибка в тесте 4")

    # Тест 5: Целевая сумма 0
    assert solution.subarraySum([0, 0, 0], 0) == 6, "Ошибка в тесте 5"

    print("Все тесты пройдены успешно!")
