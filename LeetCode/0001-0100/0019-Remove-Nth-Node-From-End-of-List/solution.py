from typing import Optional


# Определение узла односвязного списка
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        Удаляет n-й узел с конца списка за один проход.
        Использует паттерн фиктивного узла (Dummy Node) и два указателя.

        Сложность по времени: O(N)
        Сложность по памяти: O(1)
        """
        # Фиктивный узел спасает от краевых случаев
        # (например, удаления самой головы)
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # 1. Сдвигаем быстрый указатель на n шагов вперед
        for _ in range(n):
            fast = fast.next

        # 2. Двигаем оба указателя, пока fast не достигнет конца списка
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 3. Удаляем нужный узел, перекинув ссылку
        slow.next = slow.next.next

        # Возвращаем новую голову списка
        return dummy.next
