// Файл: java/warmup-1/NearHundred.java

public class NearHundred {

    /*
     --- Условие ---
     Given an int n, return True if it is within 10 of 100 or 200.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Проверяем, что абсолютная
        разница между n и 100 (или 200) не превышает 10.
     2. Крайние случаи: 90, 110, 190, 210 - должны быть включены.
     3. Сложность:
        - Временная: O(1).
        - Пространственная: O(1).
     4. Альтернативы: Прямое сравнение с диапазонами:
        (n >= 90 && n <= 110) || (n >= 190 && n <= 210).
        Решение с Math.abs() выглядит элегантнее.
    */

    // --- Решение ---
    public boolean nearHundred(int n) {
        boolean isNear100 = (Math.abs(100 - n) <= 10);
        boolean isNear200 = (Math.abs(200 - n) <= 10);
        return isNear100 || isNear200;
    }

    // --- Метод для самопроверки ---
    public static void main(String[] args) {
        NearHundred solution = new NearHundred();

        System.out.println("Тестирование метода nearHundred:");
        // Ожидаем: true
        System.out.println(solution.nearHundred(93));
        // Ожидаем: false
        System.out.println(solution.nearHundred(89));
        // Ожидаем: true
        System.out.println(solution.nearHundred(209));
        // Ожидаем: false
        System.out.println(solution.nearHundred(211));
    }
}
