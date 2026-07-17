from typing import List


class Solution:
    def canFinish(
            self, numCourses: int, prerequisites: List[List[int]]
    ) -> bool:
        """
        Определяет, можно ли завершить все курсы
        (ищет циклы в ориентированном графе).
        Использует DFS с тремя состояниями вершин.

        Сложность по времени: O(V + E)
        Сложность по памяти: O(V + E)
        """
        # Шаг 1: Построение списка смежности
        # adj[i] хранит список курсов,
        # для которых курс i является пререквизитом
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[pre].append(course)

        # Массив состояний для DFS:
        # 0 = не посещена, 1 = в процессе обхода, 2 = полностью проверена
        states = [0] * numCourses

        def dfs(node: int) -> bool:
            # Если вершина "в процессе", мы обнаружили цикл
            if states[node] == 1:
                return False
            # Если вершина уже проверена ранее, всё ок
            if states[node] == 2:
                return True

            # Помечаем текущую вершину как "в процессе"
            states[node] = 1

            # Проверяем все зависящие курсы (соседей)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            # Помечаем вершину как полностью проверенную
            states[node] = 2
            return True

        # Шаг 2: Запуск DFS для каждой вершины (граф может быть несвязным)
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
