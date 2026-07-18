from typing import Optional


# Определение узла односвязного списка (предоставляется LeetCode)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
            self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Объединяет два отсортированных связных списка в один.
        Использует паттерн Dummy Node для упрощения граничных случаев.

        Сложность по времени: O(N + M)
        Сложность по памяти: O(1)
        """
        # Создаем фиктивный узел для безопасного старта
        dummy = ListNode()
        tail = dummy

        # Пока оба списка не пусты, сравниваем узлы и прикрепляем меньший
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            # Сдвигаем хвост нашего нового списка
            tail = tail.next

        # Прикрепляем остаток того списка, который не закончился
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        # dummy.next указывает на реальное начало слитого списка
        return dummy.next
