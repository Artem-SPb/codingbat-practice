from typing import Optional


# Определение узла односвязного списка
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Определяет наличие цикла в связном списке.
        Использует алгоритм зайца и черепахи Флойда (Fast & Slow Pointers).

        Сложность по времени: O(N)
        Сложность по памяти: O(1)
        """
        slow = head
        fast = head

        # Пока быстрый указатель может безопасно сделать 2 шага вперед
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # Если указатели встретились — в списке есть кольцо
            if slow == fast:
                return True

        # Быстрый указатель достиг конца списка (None) — цикла нет
        return False
