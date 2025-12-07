class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Находит длину самой длинной подстроки без повторяющихся символов,
        используя паттерн "Скользящее окно".

        Сложность по времени: O(n)
        Сложность по памяти: O(k), где k - количество уникальных символов
        """
        char_set = set()

        # Левая граница окна
        left = 0

        res = 0

        # Правая граница окна
        for right in range(len(s)):
            # Пока правый символ уже есть в сете, сдвигаем левую границу
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Добавляем правый символ в сет
            char_set.add(s[right])

            # Обновляем максимальную длину
            res = max(res, right - left + 1)

        return res
