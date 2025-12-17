# [98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан корневой узел `root` бинарного дерева. Определите, является ли оно валидным **Бинарным Деревом Поиска (BST)**.

Валидное BST определяется следующим образом:

- Левое поддерево узла содержит только узлы со значениями **меньше**, чем значение узла.
- Правое поддерево узла содержит только узлы со значениями **больше**, чем значение узла.
- Оба, левое и правое, поддеревья также должны быть бинарными деревьями поиска.

**Пример 1:**
**Input:** root = [2, 1, 3]
**Output:** true

**Пример 2:**
**Input:** root = [5, 1, 4, null, null, 3, 6]
**Output:** false
**Пояснение:** Значение корневого узла — 5, но в его правом поддереве есть узел со значением 4.

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Свойство BST должно выполняться для **всего** поддерева, а не только для непосредственных потомков. Это ключевой момент и частая ловушка.

**Неправильный подход:** Проверить для каждого узла, что `node.left.val < node.val < node.right.val`. Этот подход не работает. Например, в дереве `[5, 1, 7, null, null, 6, 8]` узел `6` находится в правом поддереве узла `5`, но `6 > 5`, что кажется правильным. Однако `6` также является потомком корня `5` и находится в его правом поддереве, но `6` не больше, чем родительский узел `7`. Ошибка в другом: в дереве `[5, 4, 6, null, null, 3, 7]` узел `3` находится в правом поддереве корня `5`, но `3 < 5`, что нарушает главное свойство BST. Локальная проверка этого не выявит.

**Правильный подход:** Для каждого узла нужно проверять не только его непосредственных родителей, а то, что его значение находится в **допустимом диапазоне**, который определяется всеми его предками.

Этот подход элегантно реализуется рекурсией с передачей границ:

- Мы пишем вспомогательную функцию `validate(node, lower_bound, upper_bound)`.
- Для корневого узла мы вызываем ее с границами от минус до плюс бесконечности.
- Когда мы рекурсивно спускаемся **влево** от узла `node`, мы знаем, что все узлы в этом поддереве должны быть не только больше `lower_bound`, но и **меньше `node.val`**. Таким образом, `node.val` становится новой **верхней границей** (`upper_bound`).
- Аналогично, при спуске **вправо**, `node.val` становится новой **нижней границей** (`lower_bound`).

### 2. Алгоритм

1.  Создать вспомогательную рекурсивную функцию `validate(node, lower_bound, upper_bound)`.
2.  Внутри `validate`:
    a. **Базовый случай:** Если `node` пуст, вернуть `True` (пустое дерево — валидное BST).
    b. Проверить, находится ли `node.val` в диапазоне `(lower_bound, upper_bound)`. Если нет, вернуть `False`.
    c. Рекурсивно вызвать `validate` для левого потомка с обновленными границами: `validate(node.left, lower_bound, node.val)`.
    d. Рекурсивно вызвать `validate` для правого потомка с обновленными границами: `validate(node.right, node.val, upper_bound)`.
    e. Вернуть `True`, только если оба рекурсивных вызова вернули `True`.
3.  В основной функции `isValidBST` запустить этот процесс с начальными границами `(-inf, +inf)`.

---

## Код решения

```python
import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)

    def validate(self, node: Optional[TreeNode], lower_bound: float, upper_bound: float) -> bool:
        if not node:
            return True

        if not (lower_bound < node.val < upper_bound):
            return False

        return (self.validate(node.left, lower_bound, node.val) and
                self.validate(node.right, node.val, upper_bound))
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**, так как мы должны посетить каждый узел дерева ровно один раз.
- **Сложность по памяти (Space Complexity):** **O(h)**, где `h` — высота дерева. Это пространство, занимаемое стеком вызовов рекурсии.

---

## Ключевые выводы / Паттерн

- **Рекурсия с передачей ограничений (Bounds):** Это мощный паттерн для валидации структур, обладающих глобальными свойствами, таких как BST. Вместо того чтобы принимать решения только на основе локальной информации (родитель-потомок), мы проносим через рекурсию "контекст" (в данном случае, допустимый диапазон значений).
- **Понимание определения BST:** Ключ к решению — глубокое понимание того, что свойство BST (все слева меньше, все справа больше) относится не только к прямым потомкам, а ко **всем** узлам в поддеревьях.

---

<br>

### 🇬🇧 English Version

## Task Description

Given the `root` of a binary tree, determine if it is a valid **Binary Search Tree (BST)**.

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

**Example 1:**
**Input:** root = [2, 1, 3]
**Output:** true

**Example 2:**
**Input:** root = [5, 1, 4, null, null, 3, 6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

---

## My Approach to the Solution

### 1. Thought Process

The BST property must hold for the **entire** subtree, not just the immediate children. This is a key point and a common pitfall.

**Incorrect Approach:** Checking for each node that `node.left.val < node.val < node.right.val`. This approach fails. For example, in the tree `[5, 4, 6, null, null, 3, 7]`, the node `3` is in the right subtree of the root `5`, but `3 < 5`, which violates the main BST property. A local check would not detect this.

**Correct Approach:** For each node, we need to check not only against its immediate parent but that its value falls within a **valid range** determined by all its ancestors.

This approach is elegantly implemented with recursion by passing down boundaries:

- We write a helper function `validate(node, lower_bound, upper_bound)`.
- For the root node, we call it with boundaries from negative to positive infinity.
- When we recursively go **left** from a `node`, we know that all nodes in that subtree must be greater than `lower_bound` but also **less than `node.val`**. Thus, `node.val` becomes the new **upper bound**.
- Similarly, when going **right**, `node.val` becomes the new **lower bound**.

### 2. Algorithm

1.  Create a recursive helper function `validate(node, lower_bound, upper_bound)`.
2.  Inside `validate`:
    a. **Base Case:** If `node` is null, return `True` (an empty tree is a valid BST).
    b. Check if `node.val` is within the range `(lower_bound, upper_bound)`. If not, return `False`.
    c. Recursively call `validate` for the left child with updated bounds: `validate(node.left, lower_bound, node.val)`.
    d. Recursively call `validate` for the right child with updated bounds: `validate(node.right, node.val, upper_bound)`.
    e. Return `True` only if both recursive calls return `True`.
3.  In the main `isValidBST` function, start the process with initial bounds `(-inf, +inf)`.

---

## Solution Code

```python
import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)

    def validate(self, node: Optional[TreeNode], lower_bound: float, upper_bound: float) -> bool:
        if not node:
            return True

        if not (lower_bound < node.val < upper_bound):
            return False

        return (self.validate(node.left, lower_bound, node.val) and
                self.validate(node.right, node.val, upper_bound))
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**, as we must visit each node of the tree exactly once.
- **Space Complexity:** **O(h)**, where `h` is the height of the tree, for the recursion call stack.

---

## Key Takeaways / Pattern

- **Recursion with Passing Bounds:** This is a powerful pattern for validating structures with global properties like BSTs. Instead of making decisions based only on local information (parent-child), we pass down "context" (in this case, the valid range of values) through the recursion.
- **Understanding the BST Definition:** The key to the solution is a deep understanding that the BST property (all left are smaller, all right are larger) applies not just to direct children but to **all** nodes in the subtrees.
