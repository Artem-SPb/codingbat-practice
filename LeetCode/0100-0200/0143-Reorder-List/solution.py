from typing import Optional, List


# Определение узла односвязного списка
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Переупорядочивает список in-place (без возврата значения).
        Объединяет 3 техники: поиск середины, разворот списка и слияние.

        Сложность по времени: O(N)
        Сложность по памяти: O(1)
        """
        if not head or not head.next:
            return

        # Шаг 1: Найти середину списка (Fast & Slow Pointers)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Шаг 2: Развернуть вторую половину списка
        second = slow.next
        prev = None
        slow.next = None  # Разрываем связь между первой и второй половиной

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # Шаг 3: Слияние двух половин (чередование)
        first, second = head, prev
        while second:
            # Сохраняем ссылки на продолжения обеих половин
            tmp1, tmp2 = first.next, second.next

            # Вставляем узел из второй половины после узла из первой
            first.next = second
            second.next = tmp1

            # Сдвигаем указатели вперед
            first, second = tmp1, tmp2


# --- Вспомогательные функции для самопроверки ---
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    current = head
    while current:
        res.append(current.val)
        current = current.next
    return res


if __name__ == "__main__":
    solution = Solution()

    # Тест 1: Четное количество элементов
    head1 = create_linked_list([1, 2, 3, 4])
    solution.reorderList(head1)
    assert linked_list_to_list(head1) == (
        [1, 4, 2, 3], f"Ошибка в тесте 1: {linked_list_to_list(head1)}")

    # Тест 2: Нечетное количество элементов
    head2 = create_linked_list([1, 2, 3, 4, 5])
    solution.reorderList(head2)
    assert linked_list_to_list(head2) == (
        [1, 5, 2, 4, 3], f"Ошибка в тесте 2: {linked_list_to_list(head2)}")

    # Тест 3: Список из двух элементов
    head3 = create_linked_list([1, 2])
    solution.reorderList(head3)
    assert linked_list_to_list(head3) == [1, 2], "Ошибка в тесте 3"

    print("Все тесты пройдены успешно!")
