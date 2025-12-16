# Файл: python/warmup-2/string_times.py

# --- Условие ---
# Given a string and a non-negative int n, return a larger string that is
# n copies of the original string.
#
# string_times('Hi', 2) → 'HiHi'
# string_times('Hi', 3) → 'HiHiHi'

# --- Мой анализ ---
# 1. Понимание: Повторить данную строку n раз.
# 2. Крайние случаи: n = 0. `str * 0` в Python корректно вернет
#    пустую строку `''`. n = 1 вернет саму строку.
# 3. Сложность:
#    - Временная: O(N * M), где N=len(str), M=n.
#    - Пространственная: O(N * M).
# 4. Альтернативы: Можно было бы использовать цикл for и конкатенацию,
#    но это было бы медленнее и многословнее, чем оператор `*`.

# --- Решение ---


def string_times(str, n):
    return str * n
