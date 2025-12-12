# Файл: python/warmup-1/front_back.py

# --- Условие ---
# Given a string, return a new string where the first and last chars
# have been exchanged.
#
# front_back('code') → 'eodc'
# front_back('a') → 'a'
# front_back('ab') → 'ba'

# --- Мой анализ ---
# 1. Понимание: Нужно поменять местами первый и последний символы строки.
# 2. Крайние случаи: Строки длиной 0 или 1. В этих случаях менять
#    нечего, нужно вернуть строку как есть.
# 3. Сложность:
#    - Временная: O(N), N - длина строки.
#    - Пространственная: O(N).
# 4. Альтернативы: Можно было бы преобразовать строку в список символов,
#    поменять элементы и собрать обратно, но это менее эффективно, чем срезы.

# --- Решение ---


def front_back(str):
    if len(str) <= 1:
        return str

    middle = str[1:-1]

    return str[-1] + middle + str[0]
