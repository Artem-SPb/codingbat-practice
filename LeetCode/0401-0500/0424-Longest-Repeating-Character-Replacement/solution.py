class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Ищет самую длинную подстроку одинаковых символов с использованием
        паттерна "Скользящее окно" (Sliding Window).

        Сложность по времени: O(N)
        Сложность по памяти: O(1)
        """
        counts = {}
        left = 0
        max_freq = 0
        max_len = 0

        for right in range(len(s)):
            # Добавляем текущий символ в подсчет
            counts[s[right]] = counts.get(s[right], 0) + 1

            # Обновляем максимальную частоту встречаемости
            # одного символа в окне
            max_freq = max(max_freq, counts[s[right]])

            # Проверяем, валидно ли окно
            # (Длина окна - Самый частый символ <= k)
            window_len = right - left + 1
            if window_len - max_freq > k:
                # Окно невалидно, сужаем его слева
                counts[s[left]] -= 1
                left += 1

            # После возможной корректировки окна обновляем рекорд
            max_len = max(max_len, right - left + 1)

        return max_len
