// Файл: java/warmup-2/StringTimes.java

public class StringTimes {

    /*
     --- Условие ---
     Given a string and a non-negative int n, return a larger string that is
     n copies of the original string.

     --- Мой анализ ---
     1. Понимание: Нужно повторить строку n раз. В Java нет оператора `*` для
        строк, поэтому требуется итеративный подход.
     2. Крайние случаи: n = 0. Цикл `for (int i = 0; i < 0; i++)` не
        выполнится ни разу, и метод вернет пустую строку, что корректно.
     3. Сложность:
        - Временная: O(N * M), где N=str.length(), M=n.
        - Пространственная: O(N * M).
     4. Альтернативы:
        - Простая конкатенация с `+` в цикле: менее эффективна из-за создания
          множества промежуточных объектов строк.
        - `str.repeat(n)`: доступно с Java 11, самый лаконичный способ.
        - `StringBuilder` (используется в решении): самый эффективный и
          общепринятый способ для построения строк в циклах.
    */

    // --- Решение ---
    public String stringTimes(String str, int n) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(str);
        }
        return sb.toString();
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        StringTimes solution = new StringTimes();

        System.out.println("Тестирование метода stringTimes:");
        // Ожидаем: HiHi
        System.out.println(solution.stringTimes("Hi", 2));
        // Ожидаем: HiHiHi
        System.out.println(solution.stringTimes("Hi", 3));
        // Ожидаем: (пустая строка)
        System.out.println(solution.stringTimes("Hi", 0));
    }
}
