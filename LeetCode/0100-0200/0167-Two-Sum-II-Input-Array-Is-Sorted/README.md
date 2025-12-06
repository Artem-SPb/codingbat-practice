# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан **отсортированный** по возрастанию массив целых чисел `numbers` и число `target`. Необходимо найти два числа в этом массиве, которые в сумме дают `target`, и вернуть их индексы.

**Важное примечание:** Индексы в ответе должны быть **1-based** (т.е. начинаться с 1, а не с 0).

**Пример:**
**Input:** numbers = [2, 7, 11, 15], target = 9
**Output:** [1, 2]

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Ключевое слово в условии — **отсортированный**. Это прямой сигнал к использованию паттерна "Два указателя", который будет эффективнее по памяти, чем хэш-таблица.

Идея заключается в том, чтобы поставить один указатель (`l`) в начало массива (на самый маленький элемент), а другой (`r`) — в конец (на самый большой). Затем мы анализируем их сумму:

- Если сумма **больше** `target`, нам нужно ее уменьшить. Для этого мы сдвигаем правый указатель `r` влево.
- Если сумма **меньше** `target`, нам нужно ее увеличить. Для этого мы сдвигаем левый указатель `l` вправо.
- Если сумма **равна** `target`, мы нашли решение.

Этот метод гарантированно найдет ответ за один проход, так как на каждом шаге мы логически сужаем пространство поиска.

### 2. Алгоритм

1.  Инициализировать два указателя: `l = 0` и `r = len(numbers) - 1`.
2.  Запустить цикл `while l < r`.
3.  Внутри цикла вычислить `current_sum = numbers[l] + numbers[r]`.
4.  Сравнить `current_sum` с `target`:
    - Если они равны, вернуть `[l + 1, r + 1]`.
    - Если `current_sum` меньше `target`, инкрементировать `l`.
    - Если `current_sum` больше `target`, декрементировать `r`.

---

## Код решения

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**. Каждый элемент посещается не более одного раза.
- **Сложность по памяти (Space Complexity):** **O(1)**. Мы используем константное количество дополнительной памяти.

---

## Ключевые выводы / Паттерн

- **Два указателя для отсортированных массивов:** Если массив отсортирован и задача связана с поиском пары элементов, удовлетворяющих условию, паттерн "Два указателя" (один с начала, другой с конца) является самым оптимальным подходом, особенно по использованию памяти.

---

<br>

### 🇬🇧 English Version

## Task Description

Given a **sorted** (in non-decreasing order) array of integers `numbers` and an integer `target`, find two numbers such that they add up to `target` and return their indices.

**Important Note:** The indices in the answer must be **1-based** (i.e., starting from 1, not 0).

**Example:**
**Input:** numbers = [2, 7, 11, 15], target = 9
**Output:** [1, 2]

---

## My Approach to the Solution

### 1. Thought Process

The keyword in the problem description is **sorted**. This is a strong signal to use the "Two Pointers" pattern, which will be more memory-efficient than a hash map.

The idea is to place one pointer (`l`) at the beginning of the array (at the smallest element) and another pointer (`r`) at the end (at the largest element). Then, we analyze their sum:

- If the sum is **greater than** `target`, we need to decrease it. To do this, we move the right pointer `r` to the left.
- If the sum is **less than** `target`, we need to increase it. To do this, we move the left pointer `l` to the right.
- If the sum is **equal to** `target`, we have found the solution.

This method is guaranteed to find the solution in a single pass, as we logically narrow down the search space with each step.

### 2. Algorithm

1.  Initialize two pointers: `l = 0` and `r = len(numbers) - 1`.
2.  Start a `while l < r` loop.
3.  Inside the loop, calculate `current_sum = numbers[l] + numbers[r]`.
4.  Compare `current_sum` with `target`:
    - If they are equal, return `[l + 1, r + 1]`.
    - If `current_sum` is less than `target`, increment `l`.
    - If `current_sum` is greater than `target`, decrement `r`.

---

## Solution Code

```python
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**. Each element is visited at most once.
- **Space Complexity:** **O(1)**. We use a constant amount of extra space.

---

## Key Takeaways / Pattern

- **Two Pointers for Sorted Arrays:** If an array is sorted and the task involves finding a pair of elements that satisfy a certain condition, the "Two Pointers" pattern (one from the start, one from the end) is the most optimal approach, especially in terms of memory usage.
