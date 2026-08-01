from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Находит количество дней ожидания до более высокой температуры.
        Использует паттерн "Монотонный убывающий стек"
        (Monotonic Stack) для достижения сложности O(N).
        """
        n = len(temperatures)
        answer = [0] * n
        stack = []  # Здесь будем хранить индексы дней, ожидающих потепления

        for i, current_temp in enumerate(temperatures):
            # Если текущий день теплее, чем день на вершине стека,
            # значит для дня на вершине стека ожидание окончено!
            while stack and current_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                # Разница индексов — это количество прошедших дней
                answer[prev_day] = i - prev_day

            # Кладем текущий день в стек ожидания
            stack.append(i)

        return answer


# --- Блок самопроверки ---
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Скачкообразная температура
    assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == (
        [1, 1, 4, 2, 1, 1, 0, 0], "Ошибка в тесте 1")

    # Тест 2: Строго возрастающая температура
    assert solution.dailyTemperatures([30, 40, 50, 60]) == (
        [1, 1, 1, 0], "Ошибка в тесте 2")

    # Тест 3: Строго убывающая температура
    assert solution.dailyTemperatures([30, 24, 21]) == (
        [0, 0, 0], "Ошибка в тесте 3")

    # Тест 4: Массив из одного элемента
    assert solution.dailyTemperatures([42]) == [0], "Ошибка в тесте 4"

    print("Все тесты пройдены успешно!")
