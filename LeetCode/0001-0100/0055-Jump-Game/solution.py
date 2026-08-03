from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Определяет, можно ли достичь последнего индекса массива.
        Использует Жадный алгоритм (Greedy)
        для отслеживания максимально достижимой точки.
        """
        max_reach = 0
        target = len(nums) - 1

        for i, jump in enumerate(nums):
            # Если текущий индекс недостижим (мы застряли где-то раньше)
            if i > max_reach:
                return False

            # Обновляем максимально дальний прыжок
            max_reach = max(max_reach, i + jump)

            # Оптимизация: если уже можем допрыгнуть до конца, прерываем цикл
            if max_reach >= target:
                return True

        return True


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Успешный случай из примера
    assert solution.canJump([2, 3, 1, 1, 4]) is True, "Ошибка в тесте 1"

    # Тест 2: Застревание на нуле
    assert solution.canJump([3, 2, 1, 0, 4]) is False, "Ошибка в тесте 2"

    # Тест 3: Массив из одного элемента (мы уже в конце)
    assert solution.canJump([0]) is True, "Ошибка в тесте 3"

    # Тест 4: Длинные прыжки
    assert solution.canJump([2, 0, 0]) is True, "Ошибка в тесте 4"

    # Тест 5: Большой ноль, который нельзя перепрыгнуть
    assert solution.canJump([1, 0, 1, 0]) is False, "Ошибка в тесте 5"

    print("Все тесты пройдены успешно!")
