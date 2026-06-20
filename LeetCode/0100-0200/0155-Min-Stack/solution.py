class MinStack:
    def __init__(self):
        """
        Инициализирует пустой массив для хранения элементов стека.
        Каждый элемент будет представлять собой кортеж
        (значение, текущий_минимум).
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Добавляет элемент на вершину стека с
        сохранением минимального значения на текущий момент.
        """
        if not self.stack:
            self.stack.append((val, val))
        else:
            current_min = self.stack[-1][1]
            new_min = min(val, current_min)
            self.stack.append((val, new_min))

    def pop(self) -> None:
        """
        Удаляет элемент с вершины стека.
        """
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """
        Возвращает элемент на вершине стека.
        """
        if self.stack:
            return self.stack[-1][0]
        raise IndexError("top from empty stack")

    def getMin(self) -> int:
        """
        Возвращает минимальный элемент в стеке за O(1).
        """
        if self.stack:
            return self.stack[-1][1]
        raise IndexError("getMin from empty stack")
