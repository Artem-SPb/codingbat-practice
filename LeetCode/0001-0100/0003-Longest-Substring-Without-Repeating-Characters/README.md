# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дана строка `s`. Необходимо найти длину **самой длинной подстроки** без повторяющихся символов.

**Пример 1:**
**Input:** s = "abcabcbb"
**Output:** 3
**Пояснение:** Ответ - "abc", с длиной 3.

**Пример 2:**
**Input:** s = "pwwkew"
**Output:** 3
**Пояснение:** Ответ - "wke", с длиной 3. Обратите внимание, что "pwke" является подпоследовательностью, а не подстрокой.

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Решение "в лоб" (проверить каждую возможную подстроку на уникальность) будет иметь сложность O(n²) или даже O(n³), что слишком медленно.

Эта задача — классический пример на применение паттерна **"Скользящее окно" (Sliding Window)**. Идея состоит в том, чтобы поддерживать "окно" (подстроку), которое всегда удовлетворяет нашему условию (не содержит повторяющихся символов).

1.  Мы будем расширять это окно, двигая его правую границу (`r`) вправо.
2.  Нам нужен эффективный способ проверять, есть ли новый символ `s[r]` уже в нашем окне. Для этого идеально подходит **хэш-сет (`set`)**.
3.  Как только мы встречаем символ `s[r]`, который уже есть в сете, наше окно становится "невалидным".
4.  Чтобы исправить это, мы начинаем сужать окно, двигая его левую границу (`l`) вправо и удаляя символы `s[l]` из сета. Мы делаем это до тех пор, пока дубликат символа `s[r]` не будет удален из окна.
5.  После каждого расширения валидного окна мы обновляем максимальную найденную длину.

Таким образом, мы проходим по строке всего один раз, двигая оба указателя только вперед, что приводит к линейной временной сложности.

### 2. Алгоритм

1.  Инициализировать хэш-сет `char_set` для хранения символов текущего окна.
2.  Инициализировать левый указатель `l = 0` и переменную для результата `res = 0`.
3.  Запустить цикл для правого указателя `r` от `0` до конца строки.
4.  Внутри цикла:
    a. Проверить, есть ли `s[r]` в `char_set`.
    b. Если есть, запустить внутренний `while` цикл: удалять `s[l]` из `char_set` и инкрементировать `l` до тех пор, пока `s[r]` не перестанет быть в `char_set`.
    c. Добавить `s[r]` в `char_set`.
    d. Обновить результат: `res = max(res, r - l + 1)`.
5.  После завершения цикла вернуть `res`.

---

## Код решения

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**. Несмотря на вложенный `while` цикл, каждый символ строки посещается левым и правым указателем не более одного раза. Оба указателя движутся только вперед.
- **Сложность по памяти (Space Complexity):** **O(k)**, где `k` — количество уникальных символов в строке. В худшем случае (все символы уникальны) `k` может быть равно `n`. Если алфавит ограничен (например, ASCII или латиница), то сложность можно считать константной **O(1)**.

---

## Ключевые выводы / Паттерн

- **Скользящее окно (Sliding Window):** Этот паттерн идеально подходит для задач, где нужно найти оптимальную (самую длинную, самую короткую и т.д.) **непрерывную** подструктуру (подмассив или подстроку), удовлетворяющую определенному условию. Характеризуется наличием двух указателей (границ окна), которые движутся в одном направлении.
- **Комбинация с хэш-сетом/таблицей:** "Скользящее окно" часто используется в паре с хэш-сетом или хэш-таблицей для эффективного отслеживания состояния внутри текущего окна (например, уникальности элементов или их частоты).

---

<br>

### 🇬🇧 English Version

## Task Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

**Example 1:**
**Input:** s = "abcabcbb"
**Output:** 3
**Explanation:** The answer is "abc", with the length of 3.

**Example 2:**
**Input:** s = "pwwkew"
**Output:** 3
**Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

## My Approach to the Solution

### 1. Thought Process

A brute-force solution (checking every possible substring for uniqueness) would be O(n²) or O(n³), which is too slow.

This problem is a classic example for the **Sliding Window** pattern. The core idea is to maintain a "window" (a substring) that always satisfies our condition (contains no repeating characters).

1.  We will expand this window by moving its right boundary (`r`) to the right.
2.  We need an efficient way to check if the new character `s[r]` is already in our window. A **hash set (`set`)** is perfect for this.
3.  As soon as we encounter a character `s[r]` that is already in the set, our window becomes "invalid".
4.  To fix this, we start shrinking the window by moving its left boundary (`l`) to the right, removing `s[l]` from the set. We do this until the duplicate of `s[r]` has been removed from the window.
5.  After each valid expansion of the window, we update the maximum length found so far.

This way, we traverse the string just once, with both pointers only moving forward, resulting in linear time complexity.

### 2. Algorithm

1.  Initialize a hash set `char_set` to store the characters of the current window.
2.  Initialize a left pointer `l = 0` and a result variable `res = 0`.
3.  Start a loop for the right pointer `r` from `0` to the end of the string.
4.  Inside the loop:
    a. Check if `s[r]` is in `char_set`.
    b. If it is, start an inner `while` loop: remove `s[l]` from `char_set` and increment `l` until `s[r]` is no longer in `char_set`.
    c. Add `s[r]` to `char_set`.
    d. Update the result: `res = max(res, r - l + 1)`.
5.  After the loop finishes, return `res`.

---

## Solution Code

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])
            res = max(res, r - l + 1)

        return res
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**. Despite the nested `while` loop, each character of the string is visited by the left and right pointers at most once. Both pointers only move forward.
- **Space Complexity:** **O(k)**, where `k` is the number of unique characters in the string. In the worst case (all characters are unique), `k` can be equal to `n`. If the character set is limited (e.g., ASCII or Latin alphabet), the complexity can be considered constant **O(1)**.

---

## Key Takeaways / Pattern

- **Sliding Window:** This pattern is ideal for problems that require finding an optimal (longest, shortest, etc.) **contiguous** substructure (subarray or substring) that satisfies a certain condition. It is characterized by two pointers (the window boundaries) that move in the same direction.
- **Combination with Hash Set/Map:** The Sliding Window pattern is often paired with a hash set or hash map to efficiently track the state within the current window (e.g., uniqueness of elements or their frequencies).
