# Файл: python/warmup-2/front_times.py

# --- Условие ---
# Given a string and a non-negative int n, we'll say that the front
# of the string is the first 3 chars, or whatever is there if the
# string is less than length 3. Return n copies of the front.
#
# front_times('Chocolate', 2) → 'ChoCho'
# front_times('Abc', 3) → 'AbcAbcAbc'

# --- Мой анализ ---
# 1. Понимание: Комбинация двух задач: взять "front" (первые 3 символа
#    или меньше) и повторить его n раз.
# 2. Крайние случаи: Строки длиной < 3. Срез `[:3]` в Python
#    корректно их обрабатывает. n = 0 вернет пустую строку.
# 3. Сложность:
#    - Временная: O(n), т.к. итоговая длина строки зависит от n.
#    - Пространственная: O(n).
# 4. Альтернативы: Нет. Это самый идиоматичный способ в Python.

# --- Решение ---


def front_times(str, n):
    front = str[:3]
    return front * n
