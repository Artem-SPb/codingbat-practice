// Файл: java/warmup-1/NotString.java

public class NotString {

    /*
     --- Условие ---
     Given a string, return a new string where "not " has been added to the front.
     However, if the string already begins with "not", return the string unchanged.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Используем строковый метод startsWith().
     2. Крайние случаи: Пустая строка, короткие строки. `startsWith()`
        корректно их обрабатывает.
     3. Сложность:
        - Временная: O(N), где N - длина строки (из-за конкатенации).
        - Пространственная: O(N), т.к. создается новая строка.
     4. Альтернативы: Использовать `str.length() >= 3 && str.substring(0, 3).equals("not")`.
        Этот вариант более громоздкий и требует явной проверки длины.
        `startsWith()` предпочтительнее.
    */

    // --- Решение ---
    public String notString(String str) {
        if (str.startsWith("not")) {
            return str;
        }
        return "not " + str;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        NotString solution = new NotString();

        System.out.println("Тестирование метода notString:");
        // Ожидаем: not candy
        System.out.println(solution.notString("candy"));
        // Ожидаем: not bad
        System.out.println(solution.notString("not bad"));
        // Ожидаем: not
        System.out.println(solution.notString(""));
    }
}
