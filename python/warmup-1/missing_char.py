# Файл: python/warmup-1/missing_char.py

# --- Условие ---
# Given a non-empty string and an int n, return a new string where the char
# at index n has been removed. The value of n will be a valid index of a
# char in the original string
# (i.e. n will be in the range 0..len(str)-1 inclusive).
#
# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'

# --- Мой анализ ---
# 1. Понимание: Вход - строка и индекс.
# Нужно "вырезать" символ по этому индексу.
# 2. Крайние случаи: n=0 (удаление первого символа), n=len(str)-1 (удаление
#    последнего). Срезы Python корректно обрабатывают оба случая.
# 3. Сложность:
#    - Временная: O(N), N - длина строки.
#    - Пространственная: O(N).
# 4. Альтернативы: Можно было бы итерировать по строке и строить новую,
#    пропуская символ с индексом n, но это было бы намного сложнее и медленнее,
#    чем идиоматичное решение со срезами.

# --- Решение ---


def missing_char(str, n):
    front = str[:n]
    back = str[n+1:]
    return front + back
