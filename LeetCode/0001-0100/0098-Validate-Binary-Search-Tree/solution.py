from typing import Optional
import math


# Определение узла бинарного дерева (предоставлено LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Основная функция, которая запускает рекурсивную проверку.

        Сложность по времени: O(n), где n - количество узлов.
        Сложность по памяти: O(h), где h - высота дерева.
        """
        # Начальные границы: от минус бесконечности до плюс бесконечности.
        return self.validate(root, -math.inf, math.inf)

    def validate(
            self,
            node: Optional[TreeNode],
            lower_bound: float,
            upper_bound: float
    ) -> bool:
        """
        Вспомогательная рекурсивная функция, которая проверяет, что узел
        и все его поддеревья находятся
        в заданных границах (lower_bound, upper_bound).
        """
        # Базовый случай: пустое дерево является валидным BST.
        if not node:
            return True

        # Проверяем, находится ли значение текущего узла в допустимых границах.
        # Обратите внимание: строгое неравенство,
        # т.к. дубликаты в BST не допускаются.
        if not (lower_bound < node.val < upper_bound):
            return False

        # Рекурсивно проверяем поддеревья, сужая границы:
        # - Для левого поддерева новой ВЕРХНЕЙ границей
        # становится значение текущего узла.
        # - Для правого поддерева новой НИЖНЕЙ границей
        # становится значение текущего узла.
        return (self.validate(node.left, lower_bound, node.val) and
                self.validate(node.right, node.val, upper_bound))
