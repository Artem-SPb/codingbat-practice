class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        """
        Создает глубокую копию связного неориентированного графа.
        Использует DFS и Hash Map для отслеживания уже скопированных узлов.

        Сложность по времени: O(V + E)
        Сложность по памяти: O(V)
        """
        old_to_new = {}

        def dfs(node):
            if not node:
                return None

            # Если узел уже скопирован, просто возвращаем его копию
            if node in old_to_new:
                return old_to_new[node]

            # Создаем новый узел (клон)
            copy = Node(node.val)

            # ВАЖНО: сохраняем в словарь ДО обхода соседей,
            # чтобы избежать бесконечного цикла
            old_to_new[node] = copy

            # Рекурсивно клонируем всех соседей и
            # добавляем их в список связей клона
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)


# --- Вспомогательные функции для самопроверки ---
def build_graph(adjList: list) -> 'Node':
    """Строит граф из списка смежности и возвращает ссылку на первый узел."""
    if not adjList:
        return None

    nodes = {i + 1: Node(i + 1) for i in range(len(adjList))}

    for i, neighbors in enumerate(adjList):
        nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

    return nodes[1]


def graph_to_adjList(node: 'Node') -> list:
    """Преобразует граф обратно в список смежности для удобного сравнения."""
    if not node:
        return []

    result = []
    visited = set()
    queue = [node]

    # BFS для обхода всех узлов и сортировки их по значению
    nodes_dict = {}
    while queue:
        curr = queue.pop(0)
        if curr.val not in visited:
            visited.add(curr.val)
            nodes_dict[curr.val] = curr
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)

    # Формируем итоговый список
    for i in range(1, len(nodes_dict) + 1):
        result.append([n.val for n in nodes_dict[i].neighbors])

    return result


if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Квадратный граф из 4 узлов
    adj1 = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original_node1 = build_graph(adj1)
    cloned_node1 = solution.cloneGraph(original_node1)

    assert graph_to_adjList(cloned_node1) == (
        adj1, "Ошибка в тесте 1: структура графа не совпадает")
    assert original_node1 is not (
        cloned_node1,
        "Ошибка в тесте 1: возвращен старый объект, а не глубокая копия"
    )
    assert original_node1.neighbors[0] is not (
        cloned_node1.neighbors[0],
        "Ошибка в тесте 1: соседи не были глубоко скопированы"
    )

    # Тест 2: Граф из одного узла без соседей
    adj2 = [[]]
    original_node2 = build_graph(adj2)
    cloned_node2 = solution.cloneGraph(original_node2)
    assert graph_to_adjList(cloned_node2) == adj2, "Ошибка в тесте 2"

    # Тест 3: Пустой граф
    assert solution.cloneGraph(None) is None, "Ошибка в тесте 3"

    print("Все тесты пройдены успешно!")
