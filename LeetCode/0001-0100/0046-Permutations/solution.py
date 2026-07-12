from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Генерирует все возможные перестановки уникальных чисел.
        Использует классический шаблон Бэктрекинга (Backtracking).

        Сложность по времени: O(N * N!)
        Сложность по памяти: O(N)
        """
        result = []

        def backtrack(path: List[int]) -> None:
            # Базовый случай: путь достиг нужной длины
            if len(path) == len(nums):
                # Обязательно добавляем КОПИЮ списка (path[:]),
                # иначе дальнейшие изменения path испортят результат
                result.append(path[:])
                return

            for num in nums:
                # Пропускаем числа, которые уже использованы
                # в текущей перестановке
                if num in path:
                    continue

                # 1. Делаем выбор (Choose)
                path.append(num)

                # 2. Исследуем ветку (Explore)
                backtrack(path)

                # 3. Отменяем выбор (Unchoose / Backtrack)
                path.pop()

        backtrack([])
        return result
