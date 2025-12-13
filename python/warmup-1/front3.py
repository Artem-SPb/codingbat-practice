# Файл: python/warmup-1/front3.py

# --- Условие ---
# Given a string, we'll say that the front is the first 3 chars of the
# string. If the string length is less than 3, the front is whatever
# is there. Return a new string which is 3 copies of the front.
#
# front3('Java') → 'JavJavJav'

# --- Мой анализ ---
# 1. Понимание: Взять первые 3 символа (или меньше, если строка короче)
#    и повторить их трижды.
# 2. Крайние случаи: Строки длиной 2, 1, 0. Срез `[:3]` в Python
#    элегатно обрабатывает все эти случаи без ошибок.
# 3. Сложность:
#    - Временная: O(1), т.к. работаем с подстроками константной длины.
#    - Пространственная: O(1), т.к. результат имеет константную макс. длину.
# 4. Альтернативы: Можно было бы написать if/else для проверки длины,
#    но это избыточно и не "по-питоновски".

# --- Решение ---


def front3(str):
    front = str[:3]
    return front * 3
