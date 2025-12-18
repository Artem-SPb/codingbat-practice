// Файл: java/warmup-2/StringBits.java

public class StringBits {

    /*
     --- Условие ---
     Given a string, return a new string made of every other char starting
     with the first, so "Hello" yields "Hlo".

     --- Мой анализ ---
     1. Понимание: Нужно собрать строку из символов с четными индексами.
        Так как в Java нет срезов с шагом, необходимо использовать цикл.
     2. Крайние случаи: Пустая строка (цикл не выполнится, вернется ""),
        строка из одного символа (цикл выполнится один раз). Все корректно.
     3. Сложность:
        - Временная: O(N), мы проходим по строке один раз.
        - Пространственная: O(N), для хранения результата.
     4. Альтернативы: Использовать цикл с шагом 1 и проверкой `if (i % 2 == 0)`.
        Решение с шагом 2 (`i += 2`) немного более прямолинейно и эффективно.
    */

    // --- Решение ---
    public String stringBits(String str) {
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < str.length(); i = i + 2) {
            result.append(str.charAt(i));
        }
        return result.toString();
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        StringBits solution = new StringBits();

        System.out.println("Тестирование метода stringBits:");
        // Ожидаем: Hlo
        System.out.println(solution.stringBits("Hello"));
        // Ожидаем: H
        System.out.println(solution.stringBits("Hi"));
        // Ожидаем: Hello
        System.out.println(solution.stringBits("Heeololeo"));
    }
}
