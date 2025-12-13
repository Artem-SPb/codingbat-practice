// Файл: java/warmup-1/Front3.java

public class Front3 {

    /*
     --- Условие ---
     Given a string, we'll say that the front is the first 3 chars of the
     string. If the string length is less than 3, the front is whatever
     is there. Return a new string which is 3 copies of the front.

     --- Мой анализ ---
     1. Понимание: Логика та же, что и в Python, но реализация требует
        явной проверки длины строки, чтобы избежать ошибки IndexOutOfBoundsException.
     2. Крайние случаи: Строки длиной < 3. Обрабатываются через if.
     3. Сложность:
        - Временная: O(1).
        - Пространственная: O(1).
     4. Альтернативы: В Java 11+ появился метод `String.repeat(n)`, который
        позволил бы написать `return front.repeat(3);`. Конкатенация
        `front + front + front` работает во всех версиях Java.
    */

    // --- Решение ---
    public String front3(String str) {
        String front;

        if (str.length() < 3) {
            front = str;
        } else {
            front = str.substring(0, 3);
        }

        return front + front + front;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        Front3 solution = new Front3();

        System.out.println("Тестирование метода front3:");
        // Ожидаем: JavJavJav
        System.out.println(solution.front3("Java"));
        // Ожидаем: ababab
        System.out.println(solution.front3("ab"));
        // Ожидаем: aaa
        System.out.println(solution.front3("a"));
    }
}
