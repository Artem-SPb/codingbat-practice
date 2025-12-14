from typing import Optional


# Определение узла бинарного дерева (предоставлено LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Инвертирует бинарное дерево с помощью рекурсии (DFS).

        Сложность по времени: O(n), где n - количество узлов.
        Сложность по памяти: O(h),
        где h - высота дерева (из-за стека рекурсии).
        """
        # Базовый случай:
        # если узел пустой, инвертировать нечего, возвращаем его.
        if not root:
            return None

        # Шаг 1: Меняем местами левого и правого потомков текущего узла.
        # Мы можем использовать временную переменную
        # или кортежное присваивание в Python.
        root.left, root.right = root.right, root.left

        # Шаг 2: Рекурсивно вызываем инверсию
        # для (уже новых) левого и правого поддеревьев.
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Возвращаем измененный узел.
        return root
