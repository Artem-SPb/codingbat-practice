from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Находит первую и последнюю позицию элемента в отсортированном массиве.
        Использует два прохода модифицированного бинарного поиска.

        Сложность по времени: O(log N)
        Сложность по памяти: O(1)
        """

        def binary_search(is_finding_first: bool) -> int:
            left, right = 0, len(nums) - 1
            bound_index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    # Мы нашли target! Запоминаем индекс.
                    bound_index = mid

                    # Решаем, куда сужать окно дальше
                    if is_finding_first:
                        # Если ищем первую позицию, отсекаем правую часть
                        right = mid - 1
                    else:
                        # Если ищем последнюю позицию, отсекаем левую часть
                        left = mid + 1

            return bound_index

        # Запускаем поиск для левой границы
        first_pos = binary_search(is_finding_first=True)

        # Если левая граница не найдена, значит элемента в массиве вообще нет.
        # Нет смысла искать правую границу, можно сразу вернуть [-1, -1].
        if first_pos == -1:
            return [-1, -1]

        # Запускаем поиск для правой границы
        last_pos = binary_search(is_finding_first=False)

        return [first_pos, last_pos]


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Классический случай, элемент встречается несколько раз
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 8) == (
        [3, 4], "Ошибка в тесте 1")

    # Тест 2: Элемента нет в массиве
    assert solution.searchRange([5, 7, 7, 8, 8, 10], 6) == (
        [-1, -1], "Ошибка в тесте 2")

    # Тест 3: Пустой массив
    assert solution.searchRange([], 0) == [-1, -1], "Ошибка в тесте 3"

    # Тест 4: Элемент встречается ровно один раз
    assert solution.searchRange([1, 2, 3, 4, 5], 3) == (
        [2, 2], "Ошибка в тесте 4")

    # Тест 5: Массив состоит только из искомых элементов
    assert solution.searchRange([8, 8, 8, 8], 8) == [0, 3], "Ошибка в тесте 5"

    print("Все тесты пройдены успешно!")
