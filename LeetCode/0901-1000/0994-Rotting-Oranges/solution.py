from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Находит минимальное время заражения всех апельсинов.
        Использует Multi-source BFS (Поиск в ширину из нескольких источников).

        Сложность по времени: O(M * N)
        Сложность по памяти: O(M * N)
        """
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh_count = 0

        # Шаг 1: Инициализация. Ищем все гнилые и считаем свежие.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1

        # Если свежих апельсинов изначально нет, время = 0
        if fresh_count == 0:
            return 0

        minutes = 0
        # Вверх, Вниз, Влево, Вправо
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Шаг 2: BFS распространение по уровням (минутам)
        while queue and fresh_count > 0:
            # Обрабатываем ровно один "уровень" (одну минуту)
            level_size = len(queue)

            for _ in range(level_size):
                r, c = queue.popleft()

                # Проверяем всех соседей
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    # Если сосед в пределах сетки и это свежий апельсин
                    if (
                        0 <= row < rows
                        and 0 <= col < cols
                        and grid[row][col] == 1
                    ):
                        # Заражаем его
                        grid[row][col] = 2
                        fresh_count -= 1
                        queue.append((row, col))

            minutes += 1

        # Шаг 3: Проверка результата
        return minutes if fresh_count == 0 else -1
