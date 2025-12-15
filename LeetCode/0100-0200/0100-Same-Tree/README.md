# [100. Same Tree](https://leetcode.com/problems/same-tree/)

---

### 🇷🇺 Русская версия

## Описание задачи

Даны корни двух бинарных деревьев, `p` и `q`. Напишите функцию, чтобы проверить, являются ли они одинаковыми.

Два бинарных дерева считаются одинаковыми, если они структурно идентичны, и узлы имеют одинаковые значения.

**Пример 1:**
**Input:** p = [1, 2, 3], q = [1, 2, 3]
**Output:** true

**Пример 2:**
**Input:** p = [1, 2], q = [1, null, 2]
**Output:** false

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Эта задача является классическим примером рекурсивного сравнения двух структур. Сама рекурсивная природа деревьев подсказывает нам решение.

Что значит "два дерева одинаковы"?
Это значит, что:

1.  Их корни имеют одинаковые значения.
2.  **И** их левые поддеревья одинаковы.
3.  **И** их правые поддеревья одинаковы.

Это определение само по себе является рекурсивным и напрямую переводится в код.

Ключевым моментом является правильная обработка **базовых случаев**, то есть условий, при которых рекурсия должна остановиться:

- Если мы сравниваем два узла, и оба они `None`, то на этом уровне они считаются одинаковыми. `-> True`
- Если один узел `None`, а другой нет — они очевидно разные. `-> False`
- Если оба узла существуют, но их значения не равны — они тоже разные. `-> False`

Если ни один из этих базовых случаев не сработал, значит, текущие узлы идентичны, и нам нужно продолжить проверку для их дочерних узлов.

### 2. Алгоритм

1.  **Базовый случай 1:** Если оба узла `p` и `q` равны `None`, вернуть `True`.
2.  **Базовый случай 2:** Если только один из узлов `p` или `q` равен `None`, или если `p.val != q.val`, вернуть `False`.
3.  **Рекурсивный шаг:** Вернуть результат логического "И" от двух рекурсивных вызовов: `isSameTree(p.left, q.left)` **AND** `isSameTree(p.right, q.right)`.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Если оба узла - None, они идентичны
        if not p and not q:
            return True

        # Если один из узлов None, или их значения не равны - они не идентичны
        if not p or not q or p.val != q.val:
            return False

        # Рекурсивно проверяем левые и правые поддеревья
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(N)**, где `N` — это количество узлов в меньшем из двух деревьев. В худшем случае нам придется посетить все узлы, чтобы подтвердить идентичность.
- **Сложность по памяти (Space Complexity):** **O(H)**, где `H` — это высота меньшего из деревьев. Это пространство, занимаемое стеком вызовов рекурсии. В худшем случае (вырожденное дерево) `H = N`.

---

## Ключевые выводы / Паттерн

- **Параллельный обход двух деревьев:** Этот паттерн заключается в одновременном рекурсивном спуске по двум деревьям. Функция принимает два узла (по одному из каждого дерева) и сравнивает их.
- **Важность порядка базовых случаев:** В решении критически важен порядок проверок. Сначала мы проверяем, не являются ли оба узла `None` (успешное завершение ветки), и только потом — не является ли один из них `None` или не равны ли их значения (неуспешное завершение).

---

<br>

### 🇬🇧 English Version

## Task Description

Given the roots of two binary trees, `p` and `q`, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

**Example 1:**
**Input:** p = [1, 2, 3], q = [1, 2, 3]
**Output:** true

**Example 2:**
**Input:** p = [1, 2], q = [1, null, 2]
**Output:** false

---

## My Approach to the Solution

### 1. Thought Process

This problem is a classic example of recursive comparison between two structures. The recursive nature of trees itself suggests the solution.

What does it mean for "two trees to be the same"?
It means that:

1.  Their roots have the same value.
2.  **AND** their left subtrees are the same.
3.  **AND** their right subtrees are the same.

This definition is inherently recursive and translates directly into code.

The key is to correctly handle the **base cases**, i.e., the conditions under which the recursion should stop:

- If we are comparing two nodes and both are `None`, they are considered identical at this level. `-> True`
- If one node is `None` and the other is not, they are obviously different. `-> False`
- If both nodes exist but their values are not equal, they are also different. `-> False`

If none of these base cases are met, it means the current nodes are identical, and we need to continue the check for their children.

### 2. Algorithm

1.  **Base Case 1:** If both nodes `p` and `q` are `None`, return `True`.
2.  **Base Case 2:** If only one of `p` or `q` is `None`, or if `p.val != q.val`, return `False`.
3.  **Recursive Step:** Return the result of a logical "AND" of two recursive calls: `isSameTree(p.left, q.left)` **AND** `isSameTree(p.right, q.right)`.

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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, they are identical
        if not p and not q:
            return True

        # If one of the nodes is None, or their values are not equal, they are not identical
        if not p or not q or p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## Complexity Analysis

- **Time Complexity:** **O(N)**, where `N` is the number of nodes in the smaller of the two trees. In the worst case, we have to visit all nodes to confirm their identity.
- **Space Complexity:** **O(H)**, where `H` is the height of the smaller of the two trees. This is the space occupied by the recursion call stack. In the worst case (a skewed tree), `H = N`.

---

## Key Takeaways / Pattern

- **Parallel Traversal of Two Trees:** This pattern involves a simultaneous recursive descent down two trees. The function takes two nodes (one from each tree) and compares them.
- **Importance of Base Case Order:** The order of checks in the solution is critical. We first check if both nodes are `None` (successful termination of a branch), and only then do we check if one of them is `None` or if their values are unequal (unsuccessful termination).
