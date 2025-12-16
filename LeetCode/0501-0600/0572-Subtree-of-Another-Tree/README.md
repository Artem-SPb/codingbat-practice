# [572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/)

---

### 🇷🇺 Русская версия

## Описание задачи

Даны корни двух бинарных деревьев, `root` и `subRoot`. Верните `true`, если существует поддерево в `root` с такой же структурой и значениями узлов, как `subRoot`, и `false` в противном случае.

Поддерево дерева `tree` — это дерево, состоящее из узла в `tree` и всех его потомков.

**Пример:**
**Input:** root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
**Output:** true

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Задача распадается на две части:

1.  Нам нужно обойти основное дерево `root`, чтобы найти все возможные "стартовые" узлы, которые могут быть корнем искомого поддерева.
2.  Для каждого такого узла нам нужно проверить: "Является ли поддерево, начинающееся с этого узла, **полностью идентичным** `subRoot`?".

Вторую часть мы уже умеем решать! Это в точности задача **#100. Same Tree**. Таким образом, мы можем написать вспомогательную функцию `isSameTree` и использовать ее.

Основная логика будет рекурсивной. Для любой пары узлов (`root`, `subRoot`) есть три возможности, при которых `subRoot` является поддеревом `root`:

1.  Дерево `root` **само по себе** идентично дереву `subRoot`. (Мы проверяем это с помощью `isSameTree`).
2.  **ИЛИ** `subRoot` является поддеревом **левого** потомка `root`. (Мы проверяем это, рекурсивно вызывая `isSubtree(root.left, subRoot)`).
3.  **ИЛИ** `subRoot` является поддеревом **правого** потомка `root`. (Мы проверяем это, рекурсивно вызывая `isSubtree(root.right, subRoot)`).

Если хотя бы одно из этих условий истинно, значит, ответ `true`.

### 2. Алгоритм

1.  Создать вспомогательную функцию `isSameTree(p, q)`, которая решает задачу #100.
2.  В основной функции `isSubtree(root, subRoot)`:
    a. Обработать базовые случаи: если `subRoot` пуст, вернуть `true`. Если `root` пуст (а `subRoot` нет), вернуть `false`.
    b. Вызвать `isSameTree(root, subRoot)`. Если она возвращает `true`, то мы нашли совпадение, и можно сразу вернуть `true`.
    c. Если совпадения нет, рекурсивно проверить левое и правое поддеревья: вернуть `self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`.

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(N \* M)**, где `N` — количество узлов в `root`, а `M` — количество узлов в `subRoot`. В худшем случае мы для каждого из `N` узлов основного дерева будем запускать проверку `isSameTree`, которая работает за `O(M)`.
- **Сложность по памяти (Space Complexity):** **O(H_root)**, где `H_root` — высота основного дерева `root`. Это глубина стека вызовов для основной рекурсии `isSubtree`.

---

## Ключевые выводы / Паттерн

- **Декомпозиция и вспомогательные функции:** Это ключевой паттерн в программировании. Сложная задача разбивается на более простые подзадачи. Умение распознать, что часть текущей проблемы уже решена ранее (`isSameTree`), и переиспользовать это решение — признак опытного разработчика.
- **Композиция рекурсий:** Одна рекурсивная функция (`isSubtree`) обходит структуру, а другая (`isSameTree`) выполняет проверку для каждого элемента этой структуры.

---

<br>

### 🇬🇧 English Version

## Task Description

Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a subtree of `root` with the same structure and node values of `subRoot` and `false` otherwise.

A subtree of a tree `tree` is a tree that consists of a node in `tree` and all of this node's descendants.

**Example:**
**Input:** root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
**Output:** true

---

## My Approach to the Solution

### 1. Thought Process

This problem can be broken down into two parts:

1.  We need to traverse the main tree `root` to find all possible "starting" nodes that could be the root of the desired subtree.
2.  For each such node, we need to check: "Is the subtree starting from this node **exactly identical** to `subRoot`?".

We already know how to solve the second part! This is precisely the **#100. Same Tree** problem. Therefore, we can write a helper function `isSameTree` and use it.

The main logic will be recursive. For any pair of nodes (`root`, `subRoot`), there are three possibilities for `subRoot` to be a subtree of `root`:

1.  The tree `root` **itself** is identical to the tree `subRoot`. (We check this using `isSameTree`).
2.  **OR** `subRoot` is a subtree of the **left** child of `root`. (We check this by recursively calling `isSubtree(root.left, subRoot)`).
3.  **OR** `subRoot` is a subtree of the **right** child of `root`. (We check this by recursively calling `isSubtree(root.right, subRoot)`).

If at least one of these conditions is true, then the answer is `true`.

### 2. Algorithm

1.  Create a helper function `isSameTree(p, q)` that solves problem #100.
2.  In the main function `isSubtree(root, subRoot)`:
    a. Handle base cases: if `subRoot` is empty, return `true`. If `root` is empty (but `subRoot` is not), return `false`.
    b. Call `isSameTree(root, subRoot)`. If it returns `true`, we've found a match and can immediately return `true`.
    c. If there's no match, recursively check the left and right subtrees: return `self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)`.

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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

---

## Complexity Analysis

- **Time Complexity:** **O(N \* M)**, where `N` is the number of nodes in `root` and `M` is the number of nodes in `subRoot`. In the worst case, for each of the `N` nodes in the main tree, we might run an `isSameTree` check, which takes `O(M)` time.
- **Space Complexity:** **O(H_root)**, where `H_root` is the height of the main tree `root`. This is for the recursion stack depth of the main `isSubtree` function.

---

## Key Takeaways / Pattern

- **Decomposition and Helper Functions:** This is a key pattern in programming. A complex problem is broken down into simpler subproblems. The ability to recognize that a part of the current problem has been solved before (`isSameTree`) and to reuse that solution is a sign of an experienced developer.
- **Composition of Recursions:** One recursive function (`isSubtree`) traverses a structure, while another (`isSameTree`) performs a check for each element of that structure.
