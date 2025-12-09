from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Находит максимальную прибыль от одной сделки купли-продажи акций,
        используя подход с двумя указателями / отслеживанием минимума.

        Сложность по времени: O(n)
        Сложность по памяти: O(1)
        """
        # Если цен нет или всего одна, прибыли быть не может
        if not prices:
            return 0

        # Указатель на день покупки (начинаем с первого дня)
        buy_pointer = 0
        max_profit = 0

        # Указатель на день продажи (пробегаем все последующие дни)
        for sell_pointer in range(1, len(prices)):
            # Если мы нашли цену, которая ниже текущей цены покупки,
            # то выгоднее покупать в этот день. Перемещаем указатель покупки.
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
            else:
                # Иначе, это потенциально прибыльная сделка.
                # Считаем прибыль и обновляем максимум.
                profit = prices[sell_pointer] - prices[buy_pointer]
                max_profit = max(max_profit, profit)

        return max_profit
