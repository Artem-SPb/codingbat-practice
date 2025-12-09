# [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дан массив `prices`, где `prices[i]` — это цена данной акции в `i`-й день.

Вы хотите максимизировать свою прибыль, выбрав **один** день для покупки акции и **другой день в будущем** для ее продажи.

Верните максимальную прибыль, которую вы можете получить от этой сделки. Если вы не можете получить никакой прибыли, верните `0`.

**Пример 1:**
**Input:** prices = [7, 1, 5, 3, 6, 4]
**Output:** 5
**Пояснение:** Покупаем на 2-й день (цена = 1) и продаем на 5-й день (цена = 6), прибыль = 6-1 = 5. Обратите внимание, что покупка на 2-й день и продажа на 1-й невозможна, так как вы должны купить перед продажей.

**Пример 2:**
**Input:** prices = [7, 6, 4, 3, 1]
**Output:** 0
**Пояснение:** В этом случае сделка не совершается, так как максимальная прибыль равна 0.

---

## Мой подход к решению

### 1. Размышления (Thought Process)

- **Подход "в лоб" (Brute-force):** Можно перебрать все возможные пары дней для покупки и продажи. Покупаем в день `i`, продаем в день `j`, где `j > i`. Это решение с вложенными циклами и временной сложностью **O(n²)**. Слишком медленно.

- **Оптимальный подход (Один проход / Два указателя):** Нам нужно найти максимальную разницу `prices[j] - prices[i]` при условии `j > i`. Это можно сделать за один проход по массиву.

Идея заключается в том, чтобы итерировать по массиву, отслеживая всего две вещи:

1.  **Самую низкую цену**, которую мы видели до сих пор (`min_price` или цена в день `buy_pointer`).
2.  **Максимальную прибыль**, которую мы могли бы получить (`max_profit`).

Мы можем использовать два указателя: `buy_pointer` будет указывать на день с минимальной ценой, найденной на данный момент, а `sell_pointer` будет просто итерироваться по массиву.

На каждом шаге (для каждого `sell_pointer`):

- Мы сравниваем цену продажи с ценой покупки.
- Если цена продажи **ниже** цены покупки (`prices[sell_pointer] < prices[buy_pointer]`), это означает, что мы нашли новый, еще более выгодный день для покупки. Мы не можем получить прибыль, продав в этот день, поэтому мы просто обновляем наш `buy_pointer` на текущую позицию.
- Если цена продажи **выше**, мы можем получить прибыль. Мы вычисляем ее (`prices[sell_pointer] - prices[buy_pointer]`) и сравниваем с уже сохраненной `max_profit`, обновляя ее при необходимости.

Этот подход позволяет нам найти решение за один проход, что дает линейную временную сложность.

### 2. Алгоритм

1.  Инициализировать `buy_pointer = 0` и `max_profit = 0`.
2.  Запустить цикл для `sell_pointer` от `1` до конца массива `prices`.
3.  Внутри цикла:
    a. Если `prices[sell_pointer]` меньше `prices[buy_pointer]`:
    i. Обновить `buy_pointer = sell_pointer`.
    b. Иначе (если цена продажи выше или равна цене покупки):
    i. Вычислить `profit = prices[sell_pointer] - prices[buy_pointer]`.
    ii. Обновить `max_profit = max(max_profit, profit)`.
4.  После завершения цикла вернуть `max_profit`.

---

## Код решения

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy_pointer = 0
        max_profit = 0

        for sell_pointer in range(1, len(prices)):
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
            else:
                profit = prices[sell_pointer] - prices[buy_pointer]
                max_profit = max(max_profit, profit)

        return max_profit
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**. Мы проходим по массиву `prices` ровно один раз.
- **Сложность по памяти (Space Complexity):** **O(1)**. Мы используем только несколько переменных для хранения состояния, независимо от размера входных данных.

---

## Ключевые выводы / Паттерн

- **Отслеживание минимума/максимума "на лету":** Это очень распространенный под-паттерн. Вместо того чтобы каждый раз заново искать минимум в пройденной части массива, мы поддерживаем переменную, которая хранит актуальный минимум. Это позволяет решать многие задачи за один проход.
- **Гибкость "Двух указателей":** Этот паттерн не всегда означает, что указатели движутся навстречу или синхронно. Здесь один указатель (`sell_pointer`) всегда движется вперед, а второй (`buy_pointer`) "прыгает" на новую позицию только тогда, когда находится лучшее условие (более низкая цена).

---

<br>

### 🇬🇧 English Version

## Task Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`-th day.

You want to maximize your profit by choosing a **single** day to buy one stock and choosing a **different day in the future** to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

**Example 1:**
**Input:** prices = [7, 1, 5, 3, 6, 4]
**Output:** 5
**Explanation:** Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5. Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

**Example 2:**
**Input:** prices = [7, 6, 4, 3, 1]
**Output:** 0
**Explanation:** In this case, no transactions are done and the max profit is 0.

---

## My Approach to the Solution

### 1. Thought Process

- **Brute-force Approach:** We could iterate through all possible pairs of buy and sell days. Buy on day `i`, sell on day `j`, where `j > i`. This is a nested loop solution with a time complexity of **O(n²)**. Too slow.

- **Optimal Approach (One Pass / Two Pointers):** We need to find the maximum difference `prices[j] - prices[i]` given that `j > i`. This can be done in a single pass.

The idea is to iterate through the array while keeping track of just two things:

1.  The **lowest price** seen so far (`min_price` or the price on the `buy_pointer` day).
2.  The **maximum profit** we could have achieved (`max_profit`).

We can use two pointers: `buy_pointer` will point to the day with the minimum price found so far, and `sell_pointer` will simply iterate through the array.

At each step (for each `sell_pointer`):

- We compare the sell price with the buy price.
- If the sell price is **lower** than the buy price (`prices[sell_pointer] < prices[buy_pointer]`), it means we've found a new, even better day to buy. We can't make a profit by selling on this day, so we just update our `buy_pointer` to the current position.
- If the sell price is **higher**, we can make a profit. We calculate it (`prices[sell_pointer] - prices[buy_pointer]`) and compare it with our stored `max_profit`, updating it if necessary.

This approach allows us to find the solution in a single pass, resulting in linear time complexity.

### 2. Algorithm

1.  Initialize `buy_pointer = 0` and `max_profit = 0`.
2.  Start a loop for `sell_pointer` from `1` to the end of the `prices` array.
3.  Inside the loop:
    a. If `prices[sell_pointer]` is less than `prices[buy_pointer]`:
    i. Update `buy_pointer = sell_pointer`.
    b. Else (if the sell price is higher or equal to the buy price):
    i. Calculate `profit = prices[sell_pointer] - prices[buy_pointer]`.
    ii. Update `max_profit = max(max_profit, profit)`.
4.  After the loop finishes, return `max_profit`.

---

## Solution Code

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy_pointer = 0
        max_profit = 0

        for sell_pointer in range(1, len(prices)):
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
            else:
                profit = prices[sell_pointer] - prices[buy_pointer]
                max_profit = max(max_profit, profit)

        return max_profit
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**. We iterate through the `prices` array exactly once.
- **Space Complexity:** **O(1)**. We only use a few variables to store state, regardless of the input size.

---

## Key Takeaways / Pattern

- **Tracking Minimum/Maximum "On the Fly":** This is a very common sub-pattern. Instead of re-scanning the traversed part of the array to find the minimum each time, we maintain a variable that holds the current minimum. This allows many problems to be solved in a single pass.
- **Flexibility of "Two Pointers":** This pattern doesn't always mean pointers move towards each other or in sync. Here, one pointer (`sell_pointer`) always moves forward, while the other (`buy_pointer`) "jumps" to a new position only when a better condition (a lower price) is found.
