# Файл: python/warmup-1/pos_neg.py

# --- Условие ---
# Given 2 int values, a and b, and a boolean parameter "negative".
# If negative is true, then return true only if both a and b are negative.
# If negative is false,
# then return true if one is negative and one is positive.
#
# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-4, -5, True) → True

# --- Мой анализ ---
# 1. Понимание: Логика разветвляется в зависимости от параметра `negative`.
#    - Если `negative` is True: ищем `a < 0 and b < 0`.
#    - Если `negative` is False: ищем `(a < 0 and b > 0) or (a > 0 and b < 0)`.
# 2. Крайние случаи: 0 не является ни положительным, ни отрицательным.
#    Алгоритм корректно обработает 0
# (например, pos_neg(0, -5, False) -> False).
# 3. Сложность: O(1) по времени и пространству.
# 4. Альтернативы: Для случая `negative is False` можно использовать
#    элегантный трюк: `a * b < 0`. Произведение отрицательно только тогда,
#    когда у чисел разные знаки.

# --- Решение ---


def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        # Если одно положительное, а другое отрицательное, их произведение < 0
        return a * b < 0
