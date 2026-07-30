from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Находит пересечение двух массивов.
        Использует структуру данных Hash Set для обеспечения поиска за O(1).

        Сложность по времени: O(N + M)
        Сложность по памяти: O(N)
        """
        # Преобразуем первый массив во множество для мгновенного поиска
        set1 = set(nums1)

        # Результирующее множество для обеспечения
        # уникальности элементов ответа
        result_set = set()

        # Проходим по второму массиву и ищем совпадения
        for num in nums2:
            if num in set1:
                result_set.add(num)

        # По условию задачи нужно вернуть список (List)
        return list(result_set)

        # Однострочный Pythonic вариант
        # (часто используется на практике, но скрывает логику):
        # return list(set(nums1) & set(nums2))


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Вспомогательная функция для сортировки ответа перед проверкой,
    # так как порядок элементов в результате не имеет значения.
    def normalize(lst: List[int]) -> List[int]:
        return sorted(lst)

    # Тест 1: Классический случай с дубликатами
    assert normalize(solution.intersection([1, 2, 2, 1], [2, 2])) == (
        [2], "Ошибка в тесте 1")

    # Тест 2: Множественные пересечения
    assert normalize(solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])) == (
        [4, 9], "Ошибка в тесте 2")

    # Тест 3: Нет пересечений
    assert normalize(solution.intersection([1, 2, 3], [4, 5, 6])) == (
        [], "Ошибка в тесте 3")
    # Тест 4: Один из массивов пустой
    assert normalize(solution.intersection([], [1, 2])) == (
        [], "Ошибка в тесте 4")

    print("Все тесты пройдены успешно!")
