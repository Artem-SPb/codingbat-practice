// Файл: java/warmup-2/StringSplosion.java

public class StringSplosion {

    /*
     --- Условие ---
     Given a non-empty string like "Code" return a string like "CCoCodCode".

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Итеративно строим строку из
        префиксов возрастающей длины.
     2. Крайние случаи: Строка из одного символа 'a' -> 'a'. Корректно.
     3. Сложность:
        - Временная: O(N^2). Цикл выполняется N раз, `substring` занимает O(i)
          и `append` - O(i). Сумма от 1 до N дает N^2.
        - Пространственная: O(N^2) для хранения результата в StringBuilder.
     4. Альтернативы: Использование `String result += ...` в цикле было бы
        крайне неэффективно в Java. StringBuilder - стандартная практика.
    */

    // --- Решение ---
    public String stringSplosion(String str) {
        StringBuilder result = new StringBuilder();
        for (int i = 1; i <= str.length(); i++) {
            result.append(str.substring(0, i));
        }
        return result.toString();
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        StringSplosion solution = new StringSplosion();

        System.out.println("Тестирование метода stringSplosion:");
        // Ожидаем: CCoCodCode
        System.out.println(solution.stringSplosion("Code"));
        // Ожидаем: aababc
        System.out.println(solution.stringSplosion("abc"));
        // Ожидаем: aab
        System.out.println(solution.stringSplosion("ab"));
    }
}
