# [704. Binary Search](https://leetcode.com/problems/binary-search/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан отсортированный по возрастанию массив целых чисел `nums` и целое число `target`. Напишите функцию для поиска `target` в `nums`. Если `target` существует, верните его индекс. В противном случае верните `-1`.

Вы должны написать алгоритм с временной сложностью **O(log n)**.

**Пример 1:**
**Input:** nums = [-1, 0, 3, 5, 9, 12], target = 9
**Output:** 4
**Пояснение:** 9 существует в nums и его индекс равен 4.

**Пример 2:**
**Input:** nums = [-1, 0, 3, 5, 9, 12], target = 2
**Output:** -1
**Пояснение:** 2 не существует в nums, поэтому мы возвращаем -1.

---

## Мой подход к решению

### 1. Размышления (Thought Process)

- **Линейный поиск:** Самый простой способ — пройти по всему массиву и сравнить каждый элемент с `target`. Это работает, но имеет временную сложность **O(n)**, что не соответствует требованию задачи.

- **Бинарный поиск:** Ключевое условие — массив **отсортирован**. Это прямой сигнал к использованию бинарного поиска. Идея алгоритма "Разделяй и властвуй":
  1.  Берем весь массив как наше "пространство для поиска".
  2.  Смотрим на элемент точно посередине.
  3.  Если этот элемент — тот, что мы ищем, — ура, задача решена.
  4.  Если наш искомый элемент **больше** серединного, то мы можем с уверенностью отбросить всю левую половину массива. Наше новое пространство для поиска — это правая половина.
  5.  Если искомый элемент **меньше** серединного, мы отбрасываем правую половину и продолжаем искать в левой.
  6.  Мы повторяем этот процесс (деление пополам и отбрасывание) до тех пор, пока не найдем элемент или пока пространство для поиска не иссякнет.

Этот подход на каждом шаге сокращает область поиска вдвое, что и дает логарифмическую сложность.

### 2. Алгоритм

1.  Инициализировать два указателя: `left = 0` (начало массива) и `right = len(nums) - 1` (конец массива).
2.  Запустить цикл `while left <= right`. Этот цикл будет работать, пока наше пространство поиска не станет пустым.
3.  Внутри цикла вычислить средний индекс: `mid = (left + right) // 2`.
4.  Сравнить `nums[mid]` с `target`:
    a. Если `nums[mid] == target`, вернуть `mid`.
    b. Если `nums[mid] < target`, значит, `target` может быть только справа. Обновляем левую границу: `left = mid + 1`.
    c. Если `nums[mid] > target`, значит, `target` может быть только слева. Обновляем правую границу: `right = mid - 1`.
5.  Если цикл завершился (т.е. `left > right`), это означает, что элемент не найден. Вернуть `-1`.

---

## Код решения

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(log n)**. На каждой итерации мы уменьшаем пространство поиска примерно вдвое. Количество таких делений, необходимое для того, чтобы свести массив из `n` элементов к одному, равно `log₂(n)`.
- **Сложность по памяти (Space Complexity):** **O(1)**. Мы используем только несколько переменных для указателей, память не зависит от размера входного массива.

---

## Ключевые выводы / Паттерн

- **Бинарный поиск (Binary Search):** Это фундаментальный алгоритм для поиска в **отсортированных** структурах данных. Его главная сила — чрезвычайно высокая скорость (O(log n)).
- **Обязательное условие:** Данные **должны быть отсортированы**. Если они не отсортированы, бинарный поиск применять нельзя.
- **Обработка границ:** Ключевые моменты в реализации — правильная инициализация указателей (`len(nums) - 1`), условие цикла (`<=`) и обновление границ (`mid + 1` и `mid - 1`). Небольшая ошибка здесь может привести к бесконечному циклу или неверному результату.

---

<br>

### 🇬🇧 English Version

## Task Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search for `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with **O(log n)** runtime complexity.

**Example 1:**
**Input:** nums = [-1, 0, 3, 5, 9, 12], target = 9
**Output:** 4
**Explanation:** 9 exists in nums and its index is 4.

**Example 2:**
**Input:** nums = [-1, 0, 3, 5, 9, 12], target = 2
**Output:** -1
**Explanation:** 2 does not exist in nums so we return -1.

---

## My Approach to the Solution

### 1. Thought Process

- **Linear Search:** The simplest approach is to iterate through the entire array and compare each element with the `target`. This works but has a time complexity of **O(n)**, which does not meet the problem's requirement.

- **Binary Search:** The key condition is that the array is **sorted**. This is a direct signal to use binary search. The algorithm follows a "Divide and Conquer" strategy:
  1.  Take the entire array as our "search space."
  2.  Look at the element exactly in the middle.
  3.  If this element is what we're looking for, we're done.
  4.  If our target element is **greater than** the middle element, we can confidently discard the entire left half of the array. Our new search space is the right half.
  5.  If our target element is **less than** the middle element, we discard the right half and continue searching in the left half.
  6.  We repeat this process (halving and discarding) until we either find the element or the search space becomes empty.

This approach reduces the search space by half at each step, which gives it logarithmic complexity.

### 2. Algorithm

1.  Initialize two pointers: `left = 0` (start of the array) and `right = len(nums) - 1` (end of the array).
2.  Start a `while left <= right` loop. This loop will run as long as our search space is not empty.
3.  Inside the loop, calculate the middle index: `mid = (left + right) // 2`.
4.  Compare `nums[mid]` with `target`:
    a. If `nums[mid] == target`, return `mid`.
    b. If `nums[mid] < target`, the `target` can only be on the right side. Update the left boundary: `left = mid + 1`.
    c. If `nums[mid] > target`, the `target` can only be on the left side. Update the right boundary: `right = mid - 1`.
5.  If the loop finishes (i.e., `left > right`), it means the element was not found. Return `-1`.

---

## Solution Code

```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
```

---

## Complexity Analysis

- **Time Complexity:** **O(log n)**. At each iteration, we reduce the search space by approximately half. The number of such divisions required to reduce an array of `n` elements to one is `log₂(n)`.
- **Space Complexity:** **O(1)**. We only use a few variables for pointers; the memory usage is independent of the input array's size.

---

## Key Takeaways / Pattern

- **Binary Search:** This is a fundamental algorithm for searching in **sorted** data structures. Its main strength is its extremely high speed (O(log n)).
- **Prerequisite:** The data **must be sorted**. Binary search cannot be applied to unsorted data.
- **Boundary Handling:** The key implementation details are the correct initialization of pointers (`len(nums) - 1`), the loop condition (`<=`), and the boundary updates (`mid + 1` and `mid - 1`). A small mistake here can lead to an infinite loop or an incorrect result.
