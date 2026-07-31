from typing import List
from collections import deque


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Находит минимальное количество поворотов дисков для открытия замка.
        Использует BFS (Поиск в ширину) для нахождения кратчайшего пути.
        """
        # Преобразуем список тупиков в множество для O(1) поиска.
        # Это множество также будет играть роль visited (посещенных узлов).
        visited = set(deadends)

        # Базовая проверка: если стартовая точка уже тупик
        if "0000" in visited:
            return -1

        # Очередь хранит кортежи: (текущая_комбинация, количество_шагов)
        queue = deque([("0000", 0)])
        visited.add("0000")

        while queue:
            current_lock, turns = queue.popleft()

            # Если нашли целевую комбинацию, возвращаем количество шагов
            if current_lock == target:
                return turns

            # Генерируем все 8 возможных следующих состояний замка
            for i in range(4):
                digit = int(current_lock[i])

                # Крутим диск вверх (+1) и вниз (-1)
                for move in (1, -1):
                    # Используем остаток от деления
                    # для зацикливания: 9+1=0, 0-1=9
                    new_digit = (digit + move) % 10

                    # Собираем новую строку-комбинацию
                    new_lock = (
                        current_lock[:i] + str(new_digit) + current_lock[i+1:])

                    # Если такой комбинации еще не было и она не в тупиках
                    if new_lock not in visited:
                        visited.add(new_lock)
                        queue.append((new_lock, turns + 1))

        # Если перебрали все доступные комбинации и не нашли цель
        return -1


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Классический обход тупиков
    assert solution.openLock(
        ["0201", "0101", "0102", "1212", "2002"], "0202"
    ) == 6, "Ошибка в тесте 1"

    # Тест 2: Крутим назад (через 0 к 9)
    assert solution.openLock(["8888"], "0009") == 1, "Ошибка в тесте 2"

    # Тест 3: Невозможно решить (стартуем в тупике)
    assert solution.openLock(["0000"], "8888") == -1, "Ошибка в тесте 3"

    # Тест 4: Цель окружена тупиками
    assert solution.openLock(
        ["0001", "0009", "0010", "0090",
         "0100", "0900", "1000", "9000"], "1111"
    ) == -1, "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
