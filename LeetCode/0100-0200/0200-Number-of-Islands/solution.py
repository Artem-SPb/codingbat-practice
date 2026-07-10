from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Находит количество островов в матрице с
        использованием Поиска в глубину (DFS).

        Сложность по времени: O(M * N)
        Сложность по памяти: O(M * N) в худшем случае для стека рекурсии
        """
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r: int, c: int) -> None:
            # Базовый случай: выход за границы или попали на воду ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            # "Топим" сушу, чтобы не посетить её дважды
            grid[r][c] = "0"

            # Рекурсивно обходим всех соседей
            dfs(r - 1, c)  # вверх
            dfs(r + 1, c)  # вниз
            dfs(r, c - 1)  # влево
            dfs(r, c + 1)  # вправо

        # Главный цикл обхода матрицы
        for r in range(rows):
            for c in range(cols):
                # Если нашли кусок суши — это новый остров
                if grid[r][c] == "1":
                    island_count += 1
                    # Запускаем DFS, чтобы стереть весь этот остров с карты
                    dfs(r, c)

        return island_count
