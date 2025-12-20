# [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан целочисленный массив `nums` и целое число `k`. Верните `k` самых часто встречающихся элементов. Вы можете вернуть ответ в любом порядке.

**Пример 1:**
**Input:** nums = [1, 1, 1, 2, 2, 3], k = 2
**Output:** [1, 2]

**Пример 2:**
**Input:** nums = [1], k = 1
**Output:** [1]

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Эта задача элегантно решается в два этапа, комбинируя два изученных нами паттерна.

- **Этап 1: Как посчитать частоту каждого элемента?**
  Нам нужно знать, сколько раз встречается каждое число. Для этой задачи идеально подходит **хэш-таблица (словарь)**, где ключом будет число, а значением — его частота. Мы проходим по всему массиву `nums` один раз и заполняем этот словарь.

- **Этап 2: Как найти `k` элементов с наибольшей частотой?**
  После первого этапа у нас есть набор пар `(элемент, частота)`. Нам нужно найти `k` пар с самой большой частотой. Это в точности задача **"Top K Elements"**, которую мы решали ранее. Идеальный инструмент для этого — **куча (heap)**.

  Как и в прошлый раз, мы будем использовать **min-heap** размером `k`. Мы будем итерировать по нашему словарю частот. В кучу будем добавлять кортежи `(частота, элемент)`. Куча автоматически будет упорядочивать их по первому элементу, то есть по частоте. Если размер кучи превысит `k`, мы будем удалять элемент с наименьшей частотой.

  После того как мы обработаем все элементы из словаря, в куче останутся ровно `k` пар с самыми высокими частотами. Нам останется только извлечь из них сами элементы.

### 2. Алгоритм

1.  Создать хэш-таблицу (например, `collections.Counter`) для подсчета частот каждого числа в `nums`. Это займет O(N) времени.
2.  Инициализировать пустую min-кучу `min_heap`.
3.  Итерировать по всем парам `(число, частота)` в хэш-таблице.
4.  Для каждой пары:
    a. Добавить в кучу кортеж `(частота, число)`.
    b. Если размер кучи стал больше `k`, удалить из нее минимальный элемент (`heappop`).
5.  После цикла в куче останутся `k` нужных нам элементов. Создать список и извлечь в него числа (вторые элементы кортежей) из кучи.
6.  Вернуть получившийся список.

---

## Код решения

```python
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freq_map = Counter(nums)

        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = [num for freq, num in min_heap]

        return result
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(N log k)**.
  - `O(N)` на создание словаря частот.
  - `O(M log k)` на обработку `M` уникальных элементов с помощью кучи размером `k`.
  - Так как `M <= N`, общая сложность доминируется `O(N log k)`.
- **Сложность по памяти (Space Complexity):** **O(N)** в худшем случае.
  - `O(M)` для словаря частот (`M` может быть до `N`, если все элементы уникальны).
  - `O(k)` для кучи.
  - Общая сложность `O(M + k)`, что в худшем случае `O(N)`.

---

## Ключевые выводы / Паттерн

- **Композиция паттернов:** Многие сложные задачи решаются путем последовательного применения нескольких простых паттернов. В данном случае: **"Подсчет частот с помощью Hash Map" + "Поиск Top K с помощью Heap"**.
- **Предварительная обработка:** Часто бывает полезно сначала пройтись по данным и преобразовать их в более удобную структуру (как мы преобразовали массив в словарь частот), а уже потом применять основной, более сложный алгоритм.

---

<br>

### 🇬🇧 English Version

## Task Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Example 1:**
**Input:** nums = [1, 1, 1, 2, 2, 3], k = 2
**Output:** [1, 2]

**Example 2:**
**Input:** nums = [1], k = 1
**Output:** [1]

---

## My Approach to the Solution

### 1. Thought Process

This problem can be elegantly solved in two stages by combining two patterns we've already learned.

- **Stage 1: How to count the frequency of each element?**
  We need to know how many times each number appears. A **hash map (dictionary)** is perfect for this task, where the key will be the number and the value will be its frequency. We can iterate through the entire `nums` array once to populate this map.

- **Stage 2: How to find the `k` elements with the highest frequency?**
  After the first stage, we have a set of `(element, frequency)` pairs. We need to find the `k` pairs with the largest frequency. This is exactly the **"Top K Elements"** problem we've solved before. The ideal tool for this is a **heap**.

  Just like last time, we will use a **min-heap** of size `k`. We will iterate through our frequency map. We will push tuples `(frequency, element)` into the heap. The heap will automatically order them by the first item in the tuple, i.e., by frequency. If the heap size exceeds `k`, we will remove the element with the lowest frequency.

  After processing all elements from the map, the heap will contain exactly the `k` pairs with the highest frequencies. We just need to extract the elements themselves.

### 2. Algorithm

1.  Create a hash map (e.g., `collections.Counter`) to count the frequencies of each number in `nums`. This takes O(N) time.
2.  Initialize an empty min-heap `min_heap`.
3.  Iterate through all `(number, frequency)` pairs in the hash map.
4.  For each pair:
    a. Push the tuple `(frequency, number)` onto the heap.
    b. If the heap size becomes greater than `k`, pop the minimum element (`heappop`).
5.  After the loop, the heap contains the `k` elements we need. Create a list and extract the numbers (the second elements of the tuples) from the heap.
6.  Return the resulting list.

---

## Solution Code

```python
import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []

        freq_map = Counter(nums)

        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = [num for freq, num in min_heap]

        return result
```

---

## Complexity Analysis

- **Time Complexity:** **O(N log k)**.
  - `O(N)` to build the frequency map.
  - `O(M log k)` to process the `M` unique elements using a heap of size `k`.
  - Since `M <= N`, the overall complexity is dominated by `O(N log k)`.
- **Space Complexity:** **O(N)** in the worst case.
  - `O(M)` for the frequency map (`M` can be up to `N` if all elements are unique).
  - `O(k)` for the heap.
  - The total complexity is `O(M + k)`, which is `O(N)` in the worst case.

---

## Key Takeaways / Pattern

- **Composition of Patterns:** Many complex problems are solved by sequentially applying several simple patterns. In this case: **"Frequency Counting with a Hash Map" + "Finding Top K with a Heap"**.
- **Preprocessing:** It is often useful to first iterate through the data and transform it into a more convenient structure (like converting the array into a frequency map) before applying the main, more complex algorithm.
