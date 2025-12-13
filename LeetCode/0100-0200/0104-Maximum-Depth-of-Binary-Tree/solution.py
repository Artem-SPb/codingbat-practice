from typing import Optional
from collections import deque


# Определение узла бинарного дерева (предоставлено LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth_recursive(self, root: Optional[TreeNode]) -> int:
        """
        Находит максимальную глубину бинарного дерева с помощью рекурсии (DFS).

        Сложность по времени: O(n), где n - количество узлов.
        Сложность по памяти: O(h),
        где h - высота дерева (из-за стека рекурсии).
                             В худшем случае (вырожденное дерево) O(n).
        """
        # Базовый случай рекурсии: если узел пустой, его глубина 0.
        if not root:
            return 0

        # Рекурсивно находим глубину левого и правого поддеревьев.
        left_depth = self.maxDepth_recursive(root.left)
        right_depth = self.maxDepth_recursive(root.right)

        # Глубина текущего дерева =
        # 1 (за сам узел) + максимум из глубин поддеревьев.
        return 1 + max(left_depth, right_depth)

    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        """
        Находит максимальную глубину бинарного дерева итеративно с помощью BFS.

        Сложность по времени: O(n)
        Сложность по памяти: O(w), где w - максимальная ширина дерева.
                             В худшем случае (полное дерево) O(n).
        """
        if not root:
            return 0

        level = 0
        q = deque([root])  # Очередь для BFS, начинаем с корневого узла

        while q:
            # Проходим по всем узлам текущего уровня
            for i in range(len(q)):
                node = q.popleft()
                # Добавляем дочерние узлы в очередь для следующего уровня
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Увеличиваем счетчик уровней после обработки каждого уровня
            level += 1

        return level

    # Основной метод, который будет вызываться LeetCode
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepth_recursive(root)
        # или return self.maxDepth_iterative(root)
