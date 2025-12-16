from typing import Optional


# Определение узла бинарного дерева (предоставлено LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(
            self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        """
        Основная функция. Проверяет, является ли subRoot поддеревом root.

        Сложность по времени: O(N * M),
        где N - число узлов в root, M - в subRoot.
        Сложность по памяти: O(H_root),
        высота основного дерева для стека рекурсии.
        """
        # Базовый случай: пустое дерево является поддеревом любого дерева.
        if not subRoot:
            return True
        # Базовый случай: если основное дерево пусто, а subRoot нет,
        # то ответа нет.
        if not root:
            return False

        # Если поддерево, начинающееся с текущего узла root, идентично subRoot,
        # то мы нашли ответ.
        if self.isSameTree(root, subRoot):
            return True

        # Если нет, то мы должны проверить, не является ли subRoot поддеревом
        # левого ИЛИ правого потомка root.
        return (
            self.isSubtree(root.left, subRoot) or self.isSubtree(
                root.right, subRoot)
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Вспомогательная функция из задачи LeetCode #100.
        Проверяет, являются ли два дерева p и q полностью идентичными.
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return (
            self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right)
        )
