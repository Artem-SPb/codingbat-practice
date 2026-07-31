from typing import List
from collections import deque, defaultdict


class Solution:
    def findOrder(
            self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        """
        Находит правильный порядок прохождения курсов.
        Использует Алгоритм Кана (Топологическая сортировка через BFS).

        Сложность по времени: O(V + E)
        Сложность по памяти: O(V + E)
        """
        # 1. Подготовка структур данных
        # adj хранит связи в формате {курс: [курсы, которые зависят от него]}
        adj = defaultdict(list)
        # in_degree хранит количество невыполненных требований
        # для каждого курса
        in_degree = [0] * numCourses

        # 2. Построение графа
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1

        # 3. Инициализация очереди стартовыми курсами
        # (у которых нет требований)
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        order = []

        # 4. Обход графа (BFS)
        while queue:
            current = queue.popleft()
            order.append(current)

            # Мы "прошли" current курс, теперь уведомляем зависимые курсы
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1

                # Если все требования для соседа выполнены, он готов к изучению
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # 5. Проверка на наличие циклов
        # Если мы смогли добавить в расписание все курсы, возвращаем его.
        # Иначе (была циклическая зависимость) возвращаем пустой массив.
        if len(order) == numCourses:
            return order
        else:
            return []


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Линейная зависимость
    assert solution.findOrder(2, [[1, 0]]) == [0, 1], "Ошибка в тесте 1"

    # Тест 2: Множественные зависимости
    # В этом тесте ответ может быть [0, 1, 2, 3] или [0, 2, 1, 3].
    # Алгоритм Кана выдаст [0, 1, 2, 3] или [0, 2, 1, 3] в зависимости
    # от порядка обхода.
    result2 = solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert result2 in ([0, 1, 2, 3], [0, 2, 1, 3]), "Ошибка в тесте 2"

    # Тест 3: Нет зависимостей
    assert solution.findOrder(1, []) == [0], "Ошибка в тесте 3"

    # Тест 4: Неразрешимый цикл (0 зависит от 1, а 1 зависит от 0)
    assert solution.findOrder(2, [[1, 0], [0, 1]]) == [], "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
