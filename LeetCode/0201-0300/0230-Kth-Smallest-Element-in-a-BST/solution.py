from typing import Optional


# Определение узла бинарного дерева (предоставлено LeetCode)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Находит k-й наименьший элемент в BST с помощью
        итеративного in-order обхода.

        Сложность по времени: O(H + k), где H - высота дерева.
                             В худшем случае O(n).
        Сложность по памяти: O(H) для стека. В худшем случае O(n).
        """
        # Стек для итеративного обхода
        stack = []
        # Текущий узел, начинаем с корня
        current = root

        # Цикл продолжается, пока есть узлы для обработки или что-то в стеке
        while current or stack:
            # 1. Спускаемся влево до конца, добавляя все узлы в стек.
            #    Это нужно, чтобы добраться до самого маленького элемента.
            while current:
                stack.append(current)
                current = current.left

            # 2. Достаем узел из стека. Это будет следующий наименьший элемент.
            current = stack.pop()

            # 3. Уменьшаем k. Если k стало равно 0, мы нашли наш элемент.
            k -= 1
            if k == 0:
                return current.val

            # 4. Переходим к правому поддереву,
            # чтобы найти следующие по величине элементы.
            current = current.right
