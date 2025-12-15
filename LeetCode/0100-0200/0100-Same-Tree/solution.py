from typing import Optional


# Определение узла бинарного дерева (предоставлено LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Проверяет, являются ли два бинарных дерева структурно идентичными
        и имеют ли узлы одинаковые значения, используя рекурсию.

        Сложность по времени: O(N),
        где N - количество узлов в меньшем из деревьев.
        Сложность по памяти: O(H), где H - высота меньшего из деревьев.
        """

        # --- Базовые случаи ---

        # 1. Если оба узла None, они идентичны в этой ветке.
        if not p and not q:
            return True

        # 2. Если только один из узлов None, или их значения не равны,
        #    деревья точно не идентичны.
        if not p or not q or p.val != q.val:
            return False

        # --- Рекурсивный шаг ---

        # Если мы дошли сюда, то текущие узлы p и q равны.
        # Теперь нужно проверить, равны ли их поддеревья.
        # Деревья идентичны, только если И левые поддеревья идентичны,
        # И правые поддеревья идентичны.
        return (
            self.isSameTree(p.left, q.left) and self.isSameTree(
                p.right, q.right)
        )
