# [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан корневой узел `root` бинарного дерева. Инвертируйте дерево и верните его корень.

Инвертировать дерево означает, что для каждого узла его левый и правый потомки меняются местами.

**Пример:**
**Input:** root = [4, 2, 7, 1, 3, 6, 9]
**Output:** [4, 7, 2, 9, 6, 3, 1]

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Эта задача идеально подходит для рекурсивного решения. Идея очень проста: чтобы инвертировать все дерево, нам нужно для каждого узла поменять местами его левого и правого потомков.

Давайте применим рекурсивное мышление:

- **Задача для текущего узла:** Что нужно сделать с текущим узлом `root`? Просто поменять местами его `root.left` и `root.right`.
- **Делегирование:** После того как мы поменяли потомков у `root`, само левое поддерево (которое теперь находится справа) и правое поддерево (которое теперь слева) тоже должны быть инвертированы. Мы можем просто "попросить" их инвертировать самих себя, рекурсивно вызвав ту же самую функцию.
- **Базовый случай:** Когда рекурсия должна остановиться? Когда мы дойдем до пустого узла (`None`). Инвертировать `None` не нужно, мы просто возвращаем `None`.

Этот подход "сверху-вниз" (Top-Down) гарантирует, что мы посетим каждый узел и выполним операцию обмена для него.

### 2. Алгоритм

1.  Проверить базовый случай: если `root` равен `None`, вернуть `None`.
2.  Поменять местами левого и правого потомков текущего узла: `root.left, root.right = root.right, root.left`.
3.  Рекурсивно вызвать `invertTree` для левого поддерева: `self.invertTree(root.left)`.
4.  Рекурсивно вызвать `invertTree` для правого поддерева: `self.invertTree(root.right)`.
5.  Вернуть `root`.

---

## Код решения

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Меняем местами потомков
        root.left, root.right = root.right, root.left

        # Рекурсивно инвертируем поддеревья
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**, где `n` — количество узлов в дереве. Мы должны посетить каждый узел ровно один раз, чтобы поменять местами его потомков.
- **Сложность по памяти (Space Complexity):** **O(h)**, где `h` — высота дерева. Это пространство, занимаемое стеком вызовов рекурсии. В худшем случае (вырожденное дерево) `h = n`, в лучшем (сбалансированное дерево) `h = log(n)`.

---

## Ключевые выводы / Паттерн

- **Рекурсия "сверху-вниз" (Top-Down):** Этот паттерн заключается в выполнении операции на текущем узле, а затем рекурсивном вызове функции для дочерних узлов. Он очень эффективен для задач, где нужно модифицировать структуру дерева.
- **Простота рекурсии:** Для многих задач на деревьях рекурсивное решение оказывается значительно проще и короче итеративного. Главное — четко определить базовый случай и рекурсивный шаг.

---

<br>

### 🇬🇧 English Version

## Task Description

Given the `root` of a binary tree, invert the tree, and return its root.

Inverting a tree means that for every node, its left and right children are swapped.

**Example:**
**Input:** root = [4, 2, 7, 1, 3, 6, 9]
**Output:** [4, 7, 2, 9, 6, 3, 1]

---

## My Approach to the Solution

### 1. Thought Process

This problem is a perfect fit for a recursive solution. The idea is very simple: to invert the entire tree, we need to swap the left and right children of every node.

Let's apply recursive thinking:

- **Task for the current node:** What needs to be done at the current node `root`? Simply swap its `root.left` and `root.right` children.
- **Delegation:** After we've swapped the children of `root`, the left subtree itself (which is now on the right) and the right subtree (now on the left) also need to be inverted. We can just "ask" them to invert themselves by recursively calling the same function.
- **Base Case:** When should the recursion stop? When we reach an empty node (`None`). There's nothing to invert for a `None` node, so we just return `None`.

This "Top-Down" approach ensures that we visit every node and perform the swap operation on it.

### 2. Algorithm

1.  Check the base case: if `root` is `None`, return `None`.
2.  Swap the left and right children of the current node: `root.left, root.right = root.right, root.left`.
3.  Recursively call `invertTree` for the left subtree: `self.invertTree(root.left)`.
4.  Recursively call `invertTree` for the right subtree: `self.invertTree(root.right)`.
5.  Return `root`.

---

## Solution Code

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap the children
        root.left, root.right = root.right, root.left

        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**, where `n` is the number of nodes in the tree. We must visit each node exactly once to swap its children.
- **Space Complexity:** **O(h)**, where `h` is the height of the tree. This is the space occupied by the recursion call stack. In the worst case (a skewed tree), `h = n`; in the best case (a balanced tree), `h = log(n)`.

---

## Key Takeaways / Pattern

- **Top-Down Recursion:** This pattern involves performing an operation at the current node and then recursively calling the function for its children. It's very effective for problems that require modifying the tree's structure.
- **Simplicity of Recursion:** For many tree problems, the recursive solution is significantly simpler and shorter than an iterative one. The key is to clearly define the base case and the recursive step.
