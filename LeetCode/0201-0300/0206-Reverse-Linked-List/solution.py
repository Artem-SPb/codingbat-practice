from typing import Optional


# Определение узла односвязного списка (предоставляется LeetCode)
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Разворачивает односвязный список итеративным способом.

        Сложность по времени: O(N)
        Сложность по памяти: O(1)
        """
        prev = None
        curr = head

        while curr:
            # 1. Сохраняем ссылку на продолжение списка
            next_temp = curr.next
            # 2. Разворачиваем ссылку текущего узла назад
            curr.next = prev
            # 3. Сдвигаем указатель prev вперед
            prev = curr
            # 4. Сдвигаем указатель curr вперед
            curr = next_temp

        return prev
