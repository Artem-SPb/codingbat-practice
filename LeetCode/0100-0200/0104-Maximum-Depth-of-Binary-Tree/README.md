# [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дано корневой узел `root` бинарного дерева. Верните его максимальную глубину.

Максимальная глубина бинарного дерева — это количество узлов на самом длинном пути от корневого узла до самого дальнего листового узла.

**Пример:**
**Input:** root = [3, 9, 20, null, null, 15, 7]
**Output:** 3

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Эта задача — классический пример обхода дерева. Существует два основных подхода: рекурсивный и итеративный.

#### Подход 1: Рекурсия (DFS - Поиск в глубину)

Это самый интуитивный и элегантный способ. Идея строится на принципе "Разделяй и властвуй":

- **Базовый случай:** Если узел, в который мы пришли, пустой (`null`), то глубина этого "поддерева" равна 0.
- **Рекурсивный шаг:** Глубина любого непустого узла — это `1` (сам узел) плюс максимальная из глубин его левого и правого поддеревьев.

То есть, чтобы найти глубину всего дерева, мы просим левое поддерево посчитать свою глубину, правое поддерево — свою, а затем берем максимум из этих двух значений и прибавляем единицу.

#### Подход 2: Итеративный (BFS - Поиск в ширину)

Этот подход использует очередь (`queue`) для обхода дерева уровень за уровнем.

- Мы начинаем с того, что кладем в очередь корневой узел.
- Затем мы запускаем цикл, который работает, пока очередь не пуста.
- Внутри цикла мы обрабатываем все узлы **текущего уровня**: достаем их из очереди и кладем в нее всех их потомков.
- Каждый раз, когда мы полностью обработали один уровень, мы увеличиваем наш счетчик глубины (`level`) на 1.
- Когда очередь опустеет, счетчик `level` и будет содержать максимальную глубину дерева.

Оба подхода имеют одинаковую временную сложность, но рекурсивный код обычно получается короче и чище для таких задач.

### 2. Алгоритм (Рекурсивный)

1.  Если `root` равен `null`, вернуть `0`.
2.  Рекурсивно вызвать функцию для левого потомка: `left_depth = maxDepth(root.left)`.
3.  Рекурсивно вызвать функцию для правого потомка: `right_depth = maxDepth(root.right)`.
4.  Вернуть `1 + max(left_depth, right_depth)`.

---

## Код решения (Рекурсивный)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**, где `n` — количество узлов в дереве. Мы должны посетить каждый узел ровно один раз.
- **Сложность по памяти (Space Complexity):**
  - **Для рекурсивного решения (DFS):** **O(h)**, где `h` — высота дерева. Это связано с максимальной глубиной стека вызовов рекурсии. В худшем случае (полностью несбалансированное, "вырожденное" дерево) `h` может быть равно `n`, и сложность станет O(n). В лучшем случае (сбалансированное дерево) — O(log n).
  - **Для итеративного решения (BFS):** **O(w)**, где `w` — максимальная ширина дерева. В худшем случае (полное бинарное дерево) `w` может быть равно `n/2`, что дает сложность O(n).

---

## Ключевые выводы / Паттерн

- **Рекурсивный обход дерева (DFS):** Многие задачи на деревья элегантно решаются с помощью рекурсии. Ключ к успеху — правильно определить **базовый случай** (обычно это `if not root`) и **рекурсивный шаг** (что делать с результатами вызовов для левого и правого поддеревьев).
- **Итеративный обход по уровням (BFS):** Использование очереди для обхода дерева уровень за уровнем — это второй фундаментальный способ работы с деревьями. Он особенно полезен в задачах, где нужно найти кратчайший путь или что-то, связанное с уровнями дерева.

---

<br>

### 🇬🇧 English Version

## Task Description

Given the `root` of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example:**
**Input:** root = [3, 9, 20, null, null, 15, 7]
**Output:** 3

---

## My Approach to the Solution

### 1. Thought Process

This problem is a classic example of tree traversal. There are two main approaches: recursive and iterative.

#### Approach 1: Recursion (DFS - Depth-First Search)

This is the most intuitive and elegant way. The idea is based on the "Divide and Conquer" principle:

- **Base Case:** If the node we've reached is empty (`null`), the depth of this "subtree" is 0.
- **Recursive Step:** The depth of any non-empty node is `1` (for the node itself) plus the maximum of the depths of its left and right subtrees.

So, to find the depth of the entire tree, we ask the left subtree to calculate its depth, the right subtree to calculate its depth, then we take the maximum of these two values and add one.

#### Approach 2: Iterative (BFS - Breadth-First Search)

This approach uses a queue to traverse the tree level by level.

- We start by putting the root node into a queue.
- Then, we start a loop that runs as long as the queue is not empty.
- Inside the loop, we process all nodes of the **current level**: we dequeue them and enqueue all of their children.
- Each time we have completely processed one level, we increment our depth counter (`level`) by 1.
- When the queue becomes empty, the `level` counter will hold the maximum depth of the tree.

Both approaches have the same time complexity, but the recursive code is usually shorter and cleaner for such problems.

### 2. Algorithm (Recursive)

1.  If `root` is `null`, return `0`.
2.  Recursively call the function for the left child: `left_depth = maxDepth(root.left)`.
3.  Recursively call the function for the right child: `right_depth = maxDepth(root.right)`.
4.  Return `1 + max(left_depth, right_depth)`.

---

## Solution Code (Recursive)

```python
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**, where `n` is the number of nodes in the tree. We must visit each node exactly once.
- **Space Complexity:**
  - **For the recursive solution (DFS):** **O(h)**, where `h` is the height of the tree. This is due to the maximum depth of the recursion call stack. In the worst case (a completely unbalanced, "skewed" tree), `h` can be equal to `n`, making the complexity O(n). In the best case (a balanced tree), it's O(log n).
  - **For the iterative solution (BFS):** **O(w)**, where `w` is the maximum width of the tree. In the worst case (a complete binary tree), `w` can be `n/2`, which results in O(n) complexity.

---

## Key Takeaways / Pattern

- **Recursive Tree Traversal (DFS):** Many tree problems can be solved elegantly with recursion. The key to success is to correctly define the **base case** (usually `if not root`) and the **recursive step** (what to do with the results of the calls for the left and right subtrees).
- **Iterative Level-Order Traversal (BFS):** Using a queue to traverse a tree level by level is the second fundamental way to work with trees. It's particularly useful for problems where you need to find the shortest path or something related to the levels of the tree.
