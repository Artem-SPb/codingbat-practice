import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Находит минимальное время доставки сигнала до всех узлов.
        Использует Алгоритм Дейкстры с приоритетной очередью (Min-Heap).
        """
        # 1. Строим список смежности графа
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        # 2. Инициализируем Min-Heap и множество посещенных узлов
        # В куче храним кортежи (текущее_время_пути, текущий_узел)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        # 3. Запускаем обход Дейкстры
        while min_heap:
            # Извлекаем узел, до которого путь в данный момент самый короткий
            time, node = heapq.heappop(min_heap)

            # Если мы тут уже были по более короткому маршруту — пропускаем
            if node in visited:
                continue

            # Помечаем узел как обработанный
            visited.add(node)
            # Обновляем максимальное время (время доставки до последнего узла)
            max_time = max(max_time, time)

            # Проходим по всем соседям
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    # Добавляем в кучу новый маршрут:
                    # накопившееся время + вес пути к соседу
                    heapq.heappush(min_heap, (time + weight, neighbor))

        # 4. Если мы смогли посетить все N узлов, возвращаем время, иначе -1
        return max_time if len(visited) == n else -1


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Классический случай
    assert solution.networkDelayTime(
        [[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == (
        2, "Ошибка в тесте 1")

    # Тест 2: Граф из двух узлов
    assert solution.networkDelayTime([[1, 2, 1]], 2, 1) == (
        1, "Ошибка в тесте 2")

    # Тест 3: Несвязный граф (сигнал из узла 2 не может попасть в узел 1)
    assert solution.networkDelayTime([[1, 2, 1]], 2, 2) == (
        -1, "Ошибка в тесте 3")

    print("Все тесты пройдены успешно!")
