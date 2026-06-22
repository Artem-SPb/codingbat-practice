from collections import deque
from typing import List, Optional


# Определение узла бинарного дерева (предоставляется LeetCode)
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Выполняет обход бинарного дерева по уровням (BFS) с помощью очереди.

        Сложность по времени: O(N)
        Сложность по памяти: O(N)
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            # Количество узлов на текущем уровне
            level_size = len(queue)
            current_level = []

            # Обрабатываем строго узлы текущего уровня
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                # Добавляем потомков в очередь для следующего уровня
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Дерево из Примера 1: [3, 9, 20, null, null, 15, 7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))

    expected1 = [[3], [9, 20], [15, 7]]
    assert solution.levelOrder(root1) == (
        expected1, f"Ошибка: получено {solution.levelOrder(root1)}")

    # Пример 2: Дерево из одного узла [1]
    root2 = TreeNode(1)
    assert solution.levelOrder(root2) == [[1]]

    # Пример 3: Пустое дерево []
    assert solution.levelOrder(None) == []

    print("Все тесты пройдены успешно!")
