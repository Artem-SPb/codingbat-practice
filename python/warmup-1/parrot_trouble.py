# Файл: python/warmup-1/parrot_trouble.py

# --- Условие ---
# We have a loud talking parrot. The "hour" parameter is the current hour
# time in the range 0..23. We are in trouble if the parrot is talking and
# the hour is before 7 or after 20. Return True if we are in trouble.
#
# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False

# --- Мой анализ ---
# 1. Понимание: Вход - boolean `talking` и int `hour`.
#    Проблема возникает только при одновременном выполнении двух условий:
#    а) talking == True
#    б) hour < 7 или hour > 20
# 2. Крайние случаи: hour = 6, 7, 20, 21. Логика корректно
#    обрабатывает эти пограничные значения.
# 3. Сложность:
#    - Временная: O(1).
#    - Пространственная: O(1).
# 4. Альтернативы: Можно было бы использовать вложенные if, но прямое
#    возвращение результата логического выражения - самый чистый код.

# --- Решение ---


def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)
