# Файл: python/warmup-1/sleep_in.py

# --- Условие ---
# The parameter weekday is True if it is a weekday,
# and the parameter vacation is
# True if we are on vacation. We sleep in if it is not a weekday or we're on
# vacation. Return True if we sleep in.
#
# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True

# --- Мой анализ ---
# 1. Понимание: Функция принимает два boolean значения. Нужно вернуть True,
#    если мы спим. Условие для сна: (не будний день) ИЛИ (отпуск).
# 2. Крайние случаи: Здесь их нет, входные данные всегда boolean.
# 3. Сложность:
#    - Временная: O(1) - количество операций постоянно.
#    - Пространственная: O(1) - дополнительная память не используется.
# 4. Альтернативы: Можно было бы написать через if/else, но это избыточно.
#    Прямое возвращение результата логического выражения - самый чистый способ.

# --- Решение ---


def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


# --- Более элегантное решение (предпочтительное) ---
def sleep_in_optimal(weekday, vacation):
    not weekday or vacation
