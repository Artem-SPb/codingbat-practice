// Файл: java/warmup-1/MissingChar.java

public class MissingChar {

    /*
     --- Условие ---
     Given a non-empty string and an int n, return a new string where the char
     at index n has been removed. The value of n will be a valid index.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. "Вырезаем" символ, соединяя
        две подстроки: до индекса n и после него.
     2. Крайние случаи: n=0, n=str.length()-1. Метод substring()
        корректно их обрабатывает.
     3. Сложность:
        - Временная: O(N), N - длина строки.
        - Пространственная: O(N).
     4. Альтернативы: Использование StringBuilder/StringBuffer для построения
        новой строки. Для такой простой задачи это избыточно, но в более
        сложных случаях манипуляции со строками это более эффективный подход.
    */

    // --- Решение ---
    public String missingChar(String str, int n) {
        String front = str.substring(0, n);
        String back = str.substring(n + 1, str.length()); // str.length() можно опустить
        return front + back;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        MissingChar solution = new MissingChar();

        System.out.println("Тестирование метода missingChar:");
        // Ожидаем: ktten
        System.out.println(solution.missingChar("kitten", 1));
        // Ожидаем: itten
        System.out.println(solution.missingChar("kitten", 0));
        // Ожидаем: kittn
        System.out.println(solution.missingChar("kitten", 4));
    }
}
