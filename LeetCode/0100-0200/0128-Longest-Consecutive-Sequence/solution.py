from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Находит самую длинную последовательность подряд идущих чисел за O(N).
        Использует множество (Hash Set) для мгновенного поиска соседей.
        """
        # Преобразуем массив в множество для поиска за O(1)
        # и удаления дубликатов
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Проверяем, является ли текущее число началом
            # новой последовательности
            # Если (num - 1) есть в множестве,
            # значит текущее число — где-то в середине цепочки,
            # и мы его игнорируем, чтобы не делать лишнюю работу.
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Идем по цепочке вперед,
                # пока находим следующие по порядку числа
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1

                # Обновляем глобальный рекорд
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Классический случай, числа разбросаны
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == (
        4, "Ошибка в тесте 1")

    # Тест 2: Длинная последовательность с дубликатами нулей и единиц
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == (
        9, "Ошибка в тесте 2")

    # Тест 3: Пустой массив
    assert solution.longestConsecutive([]) == 0, "Ошибка в тесте 3"

    # Тест 4: Массив с дубликатами, где ответ = 1
    assert solution.longestConsecutive([5, 5, 5, 5]) == 1, "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
