# Файл: python/warmup-1/monkey_trouble.py

# --- Условие ---
# We have two monkeys, a and b, and the parameters a_smile and b_smile
# indicate if each is smiling. We are in trouble if they are both smiling
# or if neither of them is smiling. Return True if we are in trouble.
#
# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False

# --- Мой анализ ---
# 1. Понимание: Вход - два boolean.
# Нужно вернуть True, если их значения совпадают.
# 2. Крайние случаи: Отсутствуют.
# 3. Сложность:
#    - Временная: O(1) - одна операция сравнения.
#    - Пространственная: O(1) - дополнительная память не используется.
# 4. Альтернативы: Можно было использовать громоздкую конструкцию
#    (a_smile and b_smile) or (not a_smile and not b_smile),
#    но сравнение через '==' намного чище и эффективнее.

# --- Решение ---


def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile
