# Файл: python/warmup-1/back_around.py

# --- Условие ---
# Given a string, take the last char and return a new string with the last
# char added at the front and back, so 'cat' yields 'tcatt'. The original
# string will be length 1 or more.
#
# back_around('cat') → 'tcatt'
# back_around('Hello') → 'oHelloo'

# --- Мой анализ ---
# 1. Понимание: Взять последний символ и "обернуть" им исходную строку.
# 2. Крайние случаи: Условие гарантирует, что строка будет длиной 1 или
#    больше, поэтому нам не нужно беспокоиться об ошибке с пустой строкой.
# 3. Сложность:
#    - Временная: O(N), из-за конкатенации строк.
#    - Пространственная: O(N), для создания новой строки.
# 4. Альтернативы: Нет более простого или идиоматичного способа в Python.

# --- Решение ---


def back_around(str):
    last_char = str[-1]
    return last_char + str + last_char
