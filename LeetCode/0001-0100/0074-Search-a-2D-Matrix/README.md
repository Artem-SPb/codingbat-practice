# [74. Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)

---

### 🇷🇺 Русская версия

## Описание задачи

Данa матрица `m x n` со следующими свойствами:

1.  Целые числа в каждой строке отсортированы слева направо.
2.  Первое целое число каждой строки больше, чем последнее целое число предыдущей строки.

Напишите эффективную функцию, которая ищет значение `target` в матрице. Если `target` найден, верните `true`, иначе `false`.

**Пример:**
**Input:** matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
**Output:** true

---

## Мой подход к решению

### 1. Размышления (Thought Process)

- **Линейный поиск:** Можно пройти по каждой ячейке матрицы. Сложность **O(m \* n)**. Неэффективно.
- **Бинарный поиск:** Ключевые свойства матрицы (строки отсортированы, и каждая следующая строка "продолжает" предыдущую) говорят нам о том, что всю матрицу можно рассматривать как **один большой отсортированный одномерный массив**.

Если мы можем так на нее смотреть, значит, мы можем применить стандартный бинарный поиск. Единственная сложность — это преобразование "одномерного" индекса `mid` (из нашего виртуального массива) в "двумерные" координаты `[row][col]` для доступа к элементу в реальной матрице.

Формула для преобразования:

- Пусть у нас `m` строк и `n` столбцов.
- Виртуальный массив имеет `m * n` элементов.
- `left = 0`, `right = m * n - 1`.
- Для любого индекса `mid` в этом виртуальном массиве:
  - `row = mid // n` (целочисленное деление на количество столбцов)
  - `col = mid % n` (остаток от деления на количество столбцов)

Вооружившись этой формулой, мы можем применить наш шаблон бинарного поиска практически без изменений.

### 2. Алгоритм

1.  Получить размеры матрицы: `rows` и `cols`.
2.  Инициализировать указатели для бинарного поиска в виртуальном 1D массиве: `left = 0`, `right = rows * cols - 1`.
3.  Запустить цикл `while left <= right`.
4.  Внутри цикла:
    a. Вычислить средний индекс `mid = (left + right) // 2`.
    b. Преобразовать `mid` в 2D координаты: `row = mid // cols`, `col = mid % cols`.
    c. Получить значение `mid_value = matrix[row][col]`.
    d. Сравнить `mid_value` с `target`:
    i. Если равны, вернуть `True`.
    ii. Если `mid_value < target`, сдвинуть левую границу: `left = mid + 1`.
    iii. Если `mid_value > target`, сдвинуть правую границу: `right = mid - 1`.
5.  Если цикл завершился, а элемент не найден, вернуть `False`.

---

## Код решения

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

---

## Анализ сложности

- **Сложность по времени (Time Complexity):** **O(log(m \* n))**. Мы применяем бинарный поиск к общему числу элементов `N = m * n`.
- **Сложность по памяти (Space Complexity):** **O(1)**. Мы не используем дополнительную память, зависящую от размера матрицы.

---

## Ключевые выводы / Паттерн

- **Абстракция данных:** Этот паттерн заключается в мысленном преобразовании одной структуры данных (2D матрица) в другую (1D массив), чтобы применить к ней известный алгоритм (бинарный поиск).
- **Математика индексов:** Умение работать с индексами и преобразовывать их из одной системы координат в другую — важный навык для решения алгоритмических задач.

---

<br>

### 🇬🇧 English Version

## Task Description

You are given an `m x n` integer matrix `matrix` with the following two properties:

1.  Each row is sorted in non-decreasing order.
2.  The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` if `target` is in `matrix` or `false` otherwise.

You must write a solution in **O(log(m \* n))** time complexity.

**Example:**
**Input:** matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
**Output:** true

---

## My Approach to the Solution

### 1. Thought Process

- **Linear Search:** We can iterate through every cell of the matrix. The complexity is **O(m \* n)**. Inefficient.
- **Binary Search:** The key properties of the matrix (sorted rows, and each row "continues" the previous one) tell us that the entire matrix can be treated as **one large, sorted, 1D array**.

If we can view it this way, we can apply a standard binary search. The only challenge is converting a "1D" index `mid` (from our virtual array) into "2D" coordinates `[row][col]` to access the element in the actual matrix.

The conversion formula is:

- Let's say we have `m` rows and `n` columns.
- The virtual array has `m * n` elements.
- `left = 0`, `right = m * n - 1`.
- For any index `mid` in this virtual array:
  - `row = mid // n` (integer division by the number of columns)
  - `col = mid % n` (modulo of division by the number of columns)

Armed with this formula, we can apply our binary search template almost without any changes.

### 2. Algorithm

1.  Get the matrix dimensions: `rows` and `cols`.
2.  Initialize pointers for the binary search on the virtual 1D array: `left = 0`, `right = rows * cols - 1`.
3.  Start a `while left <= right` loop.
4.  Inside the loop:
    a. Calculate the middle index `mid = (left + right) // 2`.
    b. Convert `mid` to 2D coordinates: `row = mid // cols`, `col = mid % cols`.
    c. Get the value `mid_value = matrix[row][col]`.
    d. Compare `mid_value` with `target`:
    i. If they are equal, return `True`.
    ii. If `mid_value < target`, move the left boundary: `left = mid + 1`.
    iii. If `mid_value > target`, move the right boundary: `right = mid - 1`.
5.  If the loop finishes and the element is not found, return `False`.

---

## Solution Code

```python
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])

        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols]

            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

---

## Complexity Analysis

- **Time Complexity:** **O(log(m \* n))**. We are applying binary search to the total number of elements `N = m * n`.
- **Space Complexity:** **O(1)**. We are not using extra space that depends on the size of the matrix.

---

## Key Takeaways / Pattern

- **Data Abstraction:** This pattern involves mentally converting one data structure (a 2D matrix) into another (a 1D array) to apply a known algorithm (binary search) to it.
- **Index Mathematics:** The ability to work with indices and convert them from one coordinate system to another is a crucial skill for solving algorithmic problems.
