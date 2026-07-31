from typing import List
from collections import deque


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        Проверяет, является ли граф двудольным.
        Использует BFS (Поиск в ширину) для раскраски графа в 2 цвета.

        Сложность по времени: O(V + E)
        Сложность по памяти: O(V)
        """
        n = len(graph)
        # 0 - не посещен, 1 - цвет А, -1 - цвет В
        colors = [0] * n

        # Граф может быть несвязным (состоять из нескольких отдельных частей),
        # поэтому проходим по всем узлам.
        for i in range(n):
            # Если узел уже раскрашен, пропускаем его
            if colors[i] != 0:
                continue

            # Иначе начинаем BFS для нового компонента связности
            queue = deque([i])
            colors[i] = 1  # Красим стартовый узел в цвет 1

            while queue:
                node = queue.popleft()

                # Проверяем всех соседей текущего узла
                for neighbor in graph[node]:
                    # Если сосед еще не раскрашен
                    if colors[neighbor] == 0:
                        # Красим в противоположный цвет и добавляем в очередь
                        colors[neighbor] = -colors[node]
                        queue.append(neighbor)
                    # Если сосед уже раскрашен в ТОТ ЖЕ цвет,
                    # что и текущий узел — конфликт!
                    elif colors[neighbor] == colors[node]:
                        return False

        # Если обошли весь граф и не нашли конфликтов
        return True


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Граф с циклом нечетной длины (треугольник 0-1-2)
    # — не может быть двудольным
    assert solution.isBipartite(
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False, "Ошибка в тесте 1")

    # Тест 2: Граф без циклов нечетной длины (квадрат 0-1-2-3)
    # — является двудольным
    assert solution.isBipartite(
        ([[1, 3], [0, 2], [1, 3], [0, 2]]) is True, "Ошибка в тесте 2")

    # Тест 3: Несвязный граф, обе части двудольные
    assert solution.isBipartite(
        ([[1], [0], [3], [2]]) is True, "Ошибка в тесте 3")

    # Тест 4: Несвязный граф, одна часть с конфликтом
    assert solution.isBipartite(
        ([[1], [0], [3, 4], [2, 4], [2, 3]]) is False, "Ошибка в тесте 4")

    print("Все тесты пройдены успешно!")
