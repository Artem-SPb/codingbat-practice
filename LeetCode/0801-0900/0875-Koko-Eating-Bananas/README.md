# [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

---

### 🇷🇺 Русская версия

## Описание задачи

Коко любит есть бананы. Есть `n` кучек бананов, `i`-я кучка содержит `piles[i]` бананов. Охранники ушли и вернутся через `h` часов.

Коко может выбрать свою скорость поедания бананов `k` (бананов в час). Каждый час она выбирает одну кучку и съедает из нее `k` бананов. Если в кучке меньше `k` бананов, она съедает их все и больше не ест в течение этого часа.

Коко хочет съесть все бананы, но как можно медленнее. Верните минимальную целочисленную скорость `k`, при которой она сможет съесть все бананы за `h` часов.

**Пример 1:**
**Input:** piles = [3, 6, 7, 11], h = 8
**Output:** 4

---

## Мой подход к решению

### 1. Размышления (Thought Process)

На первый взгляд, задача не похожа на бинарный поиск. Давайте проанализируем. Нам нужно найти _минимальное_ значение `k` (скорость), которое удовлетворяет условию (успеть за `h` часов).

- **Пространство поиска:** Каким может быть `k`? Минимальная скорость — `1`. Максимальная осмысленная скорость — `max(piles)` (есть быстрее самой большой кучи за час не имеет смысла). Итак, наш ответ лежит в диапазоне `[1, max(piles)]`.

- **Монотонность:** Заметим ключевое свойство. Если Коко может съесть все бананы со скоростью `k`, она точно сможет съесть их и с любой скоростью `k+1`, `k+2` и т.д. Это монотонная функция: чем выше скорость, тем меньше времени требуется. Эта монотонность — прямой сигнал к тому, что мы можем применить **бинарный поиск по пространству ответов**.

Идея в том, чтобы не искать значение в массиве `piles`, а искать его в диапазоне возможных скоростей `[1, max(piles)]`.

### 2. Алгоритм

1.  Определить границы для бинарного поиска: `left = 1`, `right = max(piles)`.
2.  Инициализировать переменную `res` для хранения минимальной подходящей скорости, например, `res = right`.
3.  Запустить стандартный цикл бинарного поиска `while left <= right`.
4.  Внутри цикла:
    a. Выбрать тестовую скорость `k = (left + right) // 2`.
    b. Написать вспомогательную логику: посчитать, сколько часов `hours_needed` потребуется, чтобы съесть все бананы со скоростью `k`. Для каждой кучи `p` время равно `ceil(p / k)`.
    c. Сравнить `hours_needed` с лимитом `h`:
    i. Если `hours_needed <= h`: Эта скорость `k` нам подходит! Но, возможно, есть скорость еще меньше. Поэтому мы сохраняем `k` как потенциальный лучший ответ (`res = k`) и сдвигаем правую границу (`right = k - 1`), чтобы поискать в левой (меньшей) половине.
    ii. Если `hours_needed > h`: Скорость `k` слишком мала, мы не успеваем. Нам нужно есть быстрее. Поэтому мы отбрасываем левую половину и сдвигаем левую границу (`left = k + 1`).
5.  После завершения цикла `res` будет содержать минимальную скорость, которая удовлетворяет условию.

---

## Код решения

```python
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p / k)

            if hours_needed <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1

        return res
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n \* log(m))**, где `n` — количество кучек (`len(piles)`), а `m` — максимальное значение в `piles`. Бинарный поиск выполняется за `log(m)` итераций, и на каждой итерации мы проходим по всему массиву `piles` за `O(n)`, чтобы вычислить `hours_needed`.
- **Сложность по памяти (Space Complexity):** **O(1)**.

---

## Ключевые выводы / Паттерн

- **Бинарный поиск по ответу:** Этот мощный паттерн применяется, когда нам нужно найти минимальное или максимальное значение, удовлетворяющее некоторому условию, и это условие обладает монотонностью.
- **Определение пространства поиска:** Первый шаг в таких задачах — правильно определить границы (минимально и максимально возможный ответ), в которых мы будем искать.
- **Функция проверки:** Внутри бинарного поиска всегда есть "проверочная" функция или логика, которая для тестового значения `mid` говорит, удовлетворяет ли оно условию задачи, и помогает решить, в какой половине продолжать поиск.

---

<br>

### 🇬🇧 English Version

## Task Description

Koko loves to eat bananas. There are `n` piles of bananas, the `i`-th pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko wants to finish all the bananas before the guards return. Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

**Example 1:**
**Input:** piles = [3, 6, 7, 11], h = 8
**Output:** 4

---

## My Approach to the Solution

### 1. Thought Process

At first glance, this problem doesn't look like a binary search problem. Let's analyze it. We need to find the _minimum_ value `k` (speed) that satisfies a condition (finishing within `h` hours).

- **Search Space:** What could `k` be? The minimum possible speed is `1`. The maximum meaningful speed is `max(piles)` (eating faster than the largest pile in an hour is pointless). So, our answer lies in the range `[1, max(piles)]`.

- **Monotonicity:** Let's notice a key property. If Koko can eat all the bananas at a speed of `k`, she can definitely also eat them at any speed `k+1`, `k+2`, etc. This is a monotonic function: the higher the speed, the less time it takes. This monotonicity is a direct signal that we can apply **Binary Search on the Answer Space**.

The idea is not to search for a value within the `piles` array, but to search for it within the range of possible speeds `[1, max(piles)]`.

### 2. Algorithm

1.  Define the boundaries for the binary search: `left = 1`, `right = max(piles)`.
2.  Initialize a variable `res` to store the minimum valid speed, for example, `res = right`.
3.  Start a standard binary search loop `while left <= right`.
4.  Inside the loop:
    a. Choose a test speed `k = (left + right) // 2`.
    b. Implement helper logic: calculate how many hours `hours_needed` it would take to eat all bananas at speed `k`. For each pile `p`, the time is `ceil(p / k)`.
    c. Compare `hours_needed` with the limit `h`:
    i. If `hours_needed <= h`: This speed `k` works! But maybe there's an even smaller speed. So, we save `k` as a potential best answer (`res = k`) and move the right boundary (`right = k - 1`) to search in the left (smaller) half.
    ii. If `hours_needed > h`: The speed `k` is too slow; we can't finish in time. We need to eat faster. So, we discard the left half and move the left boundary (`left = k + 1`).
5.  After the loop finishes, `res` will hold the minimum speed that satisfies the condition.

---

## Solution Code

```python
import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p / k)

            if hours_needed <= h:
                res = min(res, k)
                right = k - 1
            else:
                left = k + 1

        return res
```

---

## Complexity Analysis

- **Time Complexity:** **O(n \* log(m))**, where `n` is the number of piles (`len(piles)`), and `m` is the maximum value in `piles`. The binary search performs `log(m)` iterations, and in each iteration, we traverse the entire `piles` array in `O(n)` time to calculate `hours_needed`.
- **Space Complexity:** **O(1)**.

---

## Key Takeaways / Pattern

- **Binary Search on the Answer:** This powerful pattern is applied when we need to find the minimum or maximum value that satisfies a certain condition, and this condition exhibits monotonicity.
- **Defining the Search Space:** The first step in such problems is to correctly identify the boundaries (the minimum and maximum possible answer) within which we will search.
- **Check Function:** Inside the binary search, there is always a "check" function or logic that, for a test value `mid`, determines if it satisfies the problem's condition and helps decide in which half to continue the search.
