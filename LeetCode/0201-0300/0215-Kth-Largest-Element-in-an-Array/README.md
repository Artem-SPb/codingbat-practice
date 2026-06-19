# [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан целочисленный массив `nums` и целое число `k`. Верните `k`-й по величине элемент в массиве.

Обратите внимание, что вам нужно найти k-й по величине элемент в отсортированном порядке, а не k-й уникальный элемент.

**Пример 1:**
**Input:** nums = [3, 2, 1, 5, 6, 4], k = 2
**Output:** 5

**Пример 2:**
**Input:** nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
**Output:** 4

---

## Мой подход к решению

### 1. Размышления (Thought Process)

- **Подход 1: Сортировка.**
  Самое очевидное решение — отсортировать массив по убыванию и взять элемент с индексом `k-1`.
  - **Сложность:** O(N log N) по времени из-за сортировки. Это работает, но можно ли быстрее?

- **Подход 2: Куча (Heap).**
  Задача просит найти "k-й самый большой" элемент. Это классический признак задач из категории "Top K Elements", которые эффективно решаются с помощью кучи.

  Идея в том, чтобы поддерживать структуру, которая хранит `k` самых больших элементов, встреченных на данный момент. Для этой цели идеально подходит **min-heap** (куча с минимумом на вершине) размером `k`.

  Почему именно **min-heap** для поиска **наибольшего**?
  1.  Мы итерируем по всем числам массива.
  2.  Каждое число мы добавляем в нашу min-heap.
  3.  Если размер кучи становится `k+1`, мы удаляем из нее самый маленький элемент (`heappop`).
  4.  Таким образом, куча всегда "избавляется" от маленьких элементов и оставляет внутри себя только `k` самых больших.
  5.  После того как мы пройдем по всему массиву, на вершине кучи (`min_heap[0]`) будет находиться самый маленький из `k` самых больших элементов. Это и есть `k`-й наибольший элемент.

  Этот подход имеет временную сложность **O(N log k)**, что лучше, чем O(N log N), особенно если `k` значительно меньше `N`.

### 2. Алгоритм

1.  Инициализировать пустую min-heap `min_heap`.
2.  Пройтись по каждому `num` в массиве `nums`.
3.  Добавить `num` в `min_heap`.
4.  Если размер `min_heap` стал больше `k`, удалить из нее минимальный элемент (`heappop`).
5.  После завершения цикла вернуть вершину кучи (`min_heap[0]`).

---

## Код решения

```python
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(N log k)**. Мы итерируем `N` раз по массиву. Каждая операция `heappush` и `heappop` для кучи размером `k` занимает `O(log k)` времени.
- **Сложность по памяти (Space Complexity):** **O(k)**. Нам нужно хранить в куче не более `k` элементов.

---

## Ключевые выводы / Паттерн

- **Паттерн "Top K Elements":** Для задач, где нужно найти `k` самых больших/маленьких/частых элементов, куча (heap) является одной из самых подходящих структур данных.
- **Использование Min-Heap для Max-элементов:** Чтобы найти `k` **наибольших** элементов, эффективно использовать **min-heap** размером `k`. Она действует как "вышибала" для маленьких элементов, всегда сохраняя внутри только "топ-k". Аналогично, для поиска `k` **наименьших** элементов используется **max-heap**.

---

<br>

### 🇬🇧 English Version

## Task Description

Given an integer array `nums` and an integer `k`, return the `k`-th largest element in the array.

Note that it is the k-th largest element in the sorted order, not the k-th distinct element.

**Example 1:**
**Input:** nums = [3, 2, 1, 5, 6, 4], k = 2
**Output:** 5

**Example 2:**
**Input:** nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
**Output:** 4

---

## My Approach to the Solution

### 1. Thought Process

- **Approach 1: Sorting.**
  The most obvious solution is to sort the array in descending order and take the element at index `k-1`.
  - **Complexity:** O(N log N) time due to sorting. This works, but can we do better?

- **Approach 2: Heap.**
  The problem asks for the "k-th largest" element. This is a classic sign of "Top K Elements" problems, which are efficiently solved using a heap.

  The idea is to maintain a data structure that stores the `k` largest elements seen so far. A **min-heap** of size `k` is perfect for this purpose.

  Why a **min-heap** to find the **largest** element?
  1.  We iterate through all numbers in the array.
  2.  We add each number to our min-heap.
  3.  If the heap size becomes `k+1`, we remove the smallest element from it (`heappop`).
  4.  This way, the heap always "discards" small elements and keeps only the `k` largest ones inside.
  5.  After we've processed the entire array, the top of the heap (`min_heap[0]`) will be the smallest among the `k` largest elements. This is exactly the `k`-th largest element.

  This approach has a time complexity of **O(N log k)**, which is better than O(N log N), especially if `k` is much smaller than `N`.

### 2. Algorithm

1.  Initialize an empty min-heap `min_heap`.
2.  Iterate through each `num` in the `nums` array.
3.  Add `num` to the `min_heap`.
4.  If the size of `min_heap` becomes greater than `k`, remove the minimum element (`heappop`).
5.  After the loop finishes, return the top of the heap (`min_heap[0]`).

---

## Solution Code

```python
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
```

---

## Complexity Analysis

- **Time Complexity:** **O(N log k)**. We iterate `N` times through the array. Each `heappush` and `heappop` operation for a heap of size `k` takes `O(log k)` time.
- **Space Complexity:** **O(k)**. We need to store at most `k` elements in the heap.

---

## Key Takeaways / Pattern

- **"Top K Elements" Pattern:** For problems that require finding the `k` largest/smallest/most frequent elements, a heap is one of the most suitable data structures.
- **Using a Min-Heap for Max-Elements:** To find the `k` **largest** elements, it's efficient to use a **min-heap** of size `k`. It acts as a "bouncer" for small elements, always keeping only the "top-k" inside. Similarly, to find the `k` **smallest** elements, a **max-heap** is used.
