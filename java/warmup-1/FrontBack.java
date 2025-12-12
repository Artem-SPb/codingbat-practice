// Файл: java/warmup-1/FrontBack.java

public class FrontBack {

    /*
     --- Условие ---
     Given a string, return a new string where the first and last chars
     have been exchanged.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Поменять местами первый и
        последний символы.
     2. Крайние случаи: Строки длиной 0 или 1. Обрабатываются в первую очередь.
     3. Сложность:
        - Временная: O(N), N - длина строки.
        - Пространственная: O(N).
     4. Альтернативы: Преобразование в массив символов (char array),
        обмен элементов и создание новой строки из массива. Для такой
        простой задачи конкатенация строк проще.
    */

    // --- Решение ---
    public String frontBack(String str) {
        if (str.length() <= 1) {
            return str;
        }

        String mid = str.substring(1, str.length() - 1);

        return str.charAt(str.length() - 1) + mid + str.charAt(0);
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        FrontBack solution = new FrontBack();

        System.out.println("Тестирование метода frontBack:");
        // Ожидаем: eodc
        System.out.println(solution.frontBack("code"));
        // Ожидаем: a
        System.out.println(solution.frontBack("a"));
        // Ожидаем: ba
        System.out.println(solution.frontBack("ab"));
    }
}
