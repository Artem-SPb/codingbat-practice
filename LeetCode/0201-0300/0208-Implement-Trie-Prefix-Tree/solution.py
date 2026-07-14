class TrieNode:
    def __init__(self):
        # Словарь для хранения дочерних узлов в формате {символ: TrieNode}
        self.children = {}
        # Флаг, указывающий, что на этом узле заканчивается полноценное слово
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        """
        Инициализирует корень префиксного дерева.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Вставляет слово в префиксное дерево за O(M), где M - длина слова.
        """
        curr = self.root
        for char in word:
            # Если символа еще нет в детях текущего узла, создаем новый узел
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # Спускаемся на уровень ниже
            curr = curr.children[char]

        # Помечаем конец вставленного слова
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Возвращает True, если слово есть в дереве (целиком).
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # Возвращаем True только если это конец слова,
        # а не просто префикс другого слова
        return curr.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        """
        Возвращает True, если в дереве есть слово,
        начинающееся с заданного префикса.
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # Если мы дошли сюда, значит весь префикс успешно найден
        return True
