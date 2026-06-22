from typing import List


class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        """
        Вычисляет арифметическое выражение в Обратной польской записи (ОПЗ).
        Использует стек для хранения промежуточных операндов.

        Сложность по времени: O(N)
        Сложность по памяти: O(N)
        """
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                # Порядок pop() критически важен:
                # сначала достаем правый операнд, затем левый
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b = stack.pop()
                a = stack.pop()
                # Используем int(a / b) вместо a // b для корректного
                # усечения отрицательных чисел к нулю
                stack.append(int(a / b))
            else:
                # Если это не оператор, значит это число
                stack.append(int(token))

        # На вершине стека останется итоговый результат
        return stack[0]
