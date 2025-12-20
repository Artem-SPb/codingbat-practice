# Файл: python/warmup-2/last2.py

# --- Условие ---
# Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxhi" yields 1 (we won't count the end substring).
#
# last2('hixxhi') → 1
# last2('xaxxaxaxx') → 1

# --- Мой анализ ---
# 1. Понимание: Найти последние 2 символа. Затем посчитать, сколько раз
#    эта пара встречается в остальной части строки (исключая конец).
# 2. Крайние случаи: Строка длиной < 2. Возвращаем 0.
# 3. Сложность:
#    - Временная: O(N), т.к. проходим по строке один раз.
#    - Пространственная: O(1).
# 4. Альтернативы: Нет. Цикл - самый прямой способ решения этой задачи.

# --- Решение ---


def last2(str):
    if len(str) < 2:
        return 0
    last2 = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        sub = str[i:i+2]
        if sub == last2:
            count = count + 1
    return count
