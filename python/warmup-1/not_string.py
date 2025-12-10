# Файл: python/warmup-1/not_string.py

# --- Условие ---
# Given a string, return a new string where "not " has been added to the front.
# However, if the string already begins with "not",
# return the string unchanged.
#
# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'

# --- Мой анализ ---
# 1. Понимание: Вход - строка. Нужно проверить, начинается ли она с "not".
#    Если да - вернуть как есть. Если нет - добавить "not " в начало.
# 2. Крайние случаи: Пустая строка "" -> "not ". Строка короче "not",
#    например "no" -> "not no". Метод startswith() корректно это обрабатывает.
# 3. Сложность:
#    - Временная: O(N), где N - длина строки (из-за конкатенации).
#    - Пространственная: O(N), т.к. в худшем случае создается новая строка.
# 4. Альтернативы: Можно было бы проверять срез `str[0:3] == 'not'`,
#    но это требует дополнительной проверки на длину строки, чтобы избежать
#    ошибки. `startswith()` - более безопасный и идиоматичный способ.

# --- Решение ---


def not_string(str):
    if str.startswith('not'):
        return str
    else:
        return 'not ' + str
