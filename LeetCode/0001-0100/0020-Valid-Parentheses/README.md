# [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

---

### 🇷🇺 Русская версия

## Описание задачи

Дана строка `s`, содержащая только символы `'('`, `')'`, `'{'`, `'}'`, `'['` и `']'`. Определите, является ли входная строка валидной.

Входная строка валидна, если:

1.  Открывающие скобки должны быть закрыты скобками того же типа.
2.  Открывающие скобки должны быть закрыты в правильном порядке.
3.  Каждой закрывающей скобке соответствует открывающая скобка того же типа.

**Пример 1:**
**Input:** s = "()"
**Output:** true

**Пример 2:**
**Input:** s = "()[]{}"
**Output:** true

**Пример 3:**
**Input:** s = "(]"
**Output:** false

---

## Мой подход к решению

### 1. Размышления (Thought Process)

Проблема требует проверки "правильного порядка" закрытия. Скобка, которая была открыта последней, должна быть закрыта первой. Например, в `([{}])` последняя открытая `{` должна быть закрыта `}` перед тем, как будет закрыта `[`.

Этот принцип — **"Последним пришел, первым ушел" (LIFO)** — является прямым указанием на использование структуры данных **Стек (Stack)**.

Идея очень проста:

1.  Мы идем по строке слева направо.
2.  Если мы встречаем **открывающую** скобку (`(`, `[`, `{`), мы ее "запоминаем на будущее", положив в стек.
3.  Если мы встречаем **закрывающую** скобку (`)`, `]`, `}`), мы должны проверить, соответствует ли она последней открытой скобке. Последняя открытая — это как раз та, что лежит на вершине стека.
    - Мы достаем элемент с вершины стека и сравниваем. Если они образуют правильную пару (например, `)` и `(`), то все хорошо, и мы продолжаем.
    - Если стек пуст (то есть закрывать нечего) или пара неправильная, то строка невалидна.
4.  После того как мы прошли всю строку, **стек должен быть пустым**. Если в нем что-то осталось, значит, какие-то открывающие скобки так и не были закрыты.

### 2. Алгоритм

1.  Инициализировать пустой `stack`.
2.  Создать `mapping` (словарь) для сопоставления закрывающих скобок открывающим.
3.  Итерировать по каждому символу `char` в строке `s`.
4.  Если `char` — **закрывающая** скобка (т.е. есть в ключах `mapping`):
    a. Проверить, пуст ли `stack`. Если да, вернуть `False`.
    b. Достать элемент с вершины стека (`stack.pop()`) и сравнить его со значением `mapping[char]`. Если они не равны, вернуть `False`.
5.  Если `char` — **открывающая** скобка:
    a. Положить `char` в `stack`.
6.  После завершения цикла, проверить, пуст ли `stack`. Вернуть `True`, если пуст, и `False` в противном случае.

---

## Код решения

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(n)**, так как мы проходим по строке длиной `n` ровно один раз.
- **Сложность по памяти (Space Complexity):** **O(n)**. В худшем случае (например, строка `((((...))))`) нам придется хранить в стеке до `n/2` открывающих скобок.

---

## Ключевые выводы / Паттерн

- **Стек для проверки сбалансированности/вложенности:** Это канонический паттерн. Стек идеально подходит для проверки любых структур, где есть парные открывающие/закрывающие элементы с правилами вложенности (скобки, HTML/XML теги и т.д.).
- **Использование словаря для сопоставления:** Хэш-таблица (словарь) отлично дополняет стек, позволяя мгновенно (за O(1)) находить парный символ для проверки.

---

<br>

### 🇬🇧 English Version

## Task Description

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.

An input string is valid if:

1.  Open brackets must be closed by the same type of brackets.
2.  Open brackets must be closed in the correct order.
3.  Every close bracket has a corresponding open bracket of the same type.

**Example 1:**
**Input:** s = "()"
**Output:** true

**Example 2:**
**Input:** s = "()[]{}"
**Output:** true

**Example 3:**
**Input:** s = "(]"
**Output:** false

---

## My Approach to the Solution

### 1. Thought Process

The problem requires checking the "correct order" of closing. The bracket that was opened last must be closed first. For example, in `([{}])`, the last opened `{` must be closed by `}` before `[` can be closed.

This principle — **"Last-In, First-Out" (LIFO)** — is a direct indicator for using a **Stack** data structure.

The idea is very simple:

1.  We iterate through the string from left to right.
2.  If we encounter an **opening** bracket (`(`, `[`, `{`), we "remember it for later" by pushing it onto the stack.
3.  If we encounter a **closing** bracket (`)`, `]`, `}`), we must check if it corresponds to the last opened bracket. The last opened one is exactly what's at the top of the stack.
    - We pop the element from the top of the stack and compare. If they form a valid pair (e.g., `)` and `(`), everything is fine, and we continue.
    - If the stack is empty (meaning there's nothing to close) or the pair is incorrect, the string is invalid.
4.  After we have traversed the entire string, the **stack must be empty**. If anything is left in it, it means some opening brackets were never closed.

### 2. Algorithm

1.  Initialize an empty `stack`.
2.  Create a `mapping` (dictionary) to match closing brackets to their opening counterparts.
3.  Iterate through each character `char` in the string `s`.
4.  If `char` is a **closing** bracket (i.e., a key in `mapping`):
    a. Check if the `stack` is empty. If so, return `False`.
    b. Pop the top element from the `stack` (`stack.pop()`) and compare it to `mapping[char]`. If they don't match, return `False`.
5.  If `char` is an **opening** bracket:
    a. Push `char` onto the `stack`.
6.  After the loop finishes, check if the `stack` is empty. Return `True` if it is, and `False` otherwise.

---

## Solution Code

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)

        return not stack
```

---

## Complexity Analysis

- **Time Complexity:** **O(n)**, as we traverse the string of length `n` exactly once.
- **Space Complexity:** **O(n)**. In the worst case (e.g., a string like `((((...))))`), we would have to store up to `n/2` opening brackets on the stack.

---

## Key Takeaways / Pattern

- **Stack for Validating Balance/Nesting:** This is a canonical pattern. A stack is perfectly suited for validating any structure with paired opening/closing elements that have nesting rules (parentheses, HTML/XML tags, etc.).
- **Using a Map for Matching:** A hash map (dictionary) perfectly complements the stack, allowing for instant (O(1)) lookup of the matching pair for validation.
