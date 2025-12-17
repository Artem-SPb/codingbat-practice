// Файл: java/warmup-2/FrontTimes.java

public class FrontTimes {

    /*
     --- Условие ---
     Given a string and a non-negative int n, we'll say that the front
     of the string is the first 3 chars, or whatever is there if the
     string is less than length 3. Return n copies of the front.

     --- Мой анализ ---
     1. Понимание: Комбинация логики из `front3` и `string_times` для Java.
     2. Крайние случаи: Строки длиной < 3 требуют явной проверки. n = 0
        приведет к тому, что цикл не выполнится, и будет возвращена
        пустая строка, что корректно.
     3. Сложность:
        - Временная: O(n).
        - Пространственная: O(n).
     4. Альтернативы: Использовать `front.repeat(n)` (начиная с Java 11),
        но решение с `StringBuilder` является более универсальным и
        показывает понимание основ построения строк.
    */

    // --- Решение ---
    public String frontTimes(String str, int n) {
        String front;
        if (str.length() < 3) {
            front = str;
        } else {
            front = str.substring(0, 3);
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < n; i++) {
            result.append(front);
        }

        return result.toString();
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        FrontTimes solution = new FrontTimes();

        System.out.println("Тестирование метода frontTimes:");
        // Ожидаем: ChoCho
        System.out.println(solution.frontTimes("Chocolate", 2));
        // Ожидаем: AbcAbcAbc
        System.out.println(solution.frontTimes("Abc", 3));
        // Ожидаем: aaaa
        System.out.println(solution.frontTimes("a", 4));
    }
}
