from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Вычисляет произведение всех элементов массива, кроме самого себя.
        Использует технику Prefix и Postfix (накопительное произведение).
        Не использует деление.

        Сложность по времени: O(N)
        Сложность по памяти: O(1) (не считая массива ответа)
        """
        n = len(nums)
        answer = [1] * n

        # Шаг 1: Проход слева направо (считаем префиксы)
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Шаг 2: Проход справа налево
        # (считаем постфиксы и сразу домножаем в answer)
        postfix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]

        return answer
