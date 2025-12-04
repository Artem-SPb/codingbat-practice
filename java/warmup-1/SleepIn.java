// Файл: java/warmup-1/SleepIn.java

// 1. Объявление класса. Это "контейнер" для нашего кода.
// Его имя, SleepIn, должно совпадать с именем файла.
public class SleepIn {

    /*
     --- Условие ---
     The parameter weekday is True if it is a weekday, and the parameter vacation is
     True if we are on vacation. We sleep in if it is not a weekday or we're on
     vacation. Return True if we sleep in.

     --- Мой анализ ---
     1. Понимание: Логика идентична Python. Принимаем два boolean, возвращаем boolean.
        Условие сна: НЕ будний день ИЛИ отпуск.
     2. Крайние случаи: Отсутствуют.
     3. Сложность:
        - Временная: O(1) - постоянное время выполнения.
        - Пространственная: O(1) - дополнительная память не используется.
     4. Альтернативы: Можно использовать более громоздкий if/else, но прямое
        возвращение логического выражения является лучшей практикой.
    */

    // 2. Метод решения задачи. Он находится ВНУТРИ класса SleepIn.
    public boolean sleepIn(boolean weekday, boolean vacation) {
        return !weekday || vacation;
    }

    /*
     3. Точка входа (main method). Это специальный метод, который позволяет
        запустить этот файл как программу для самостоятельной проверки.
        IDE, такие как VS Code или IntelliJ IDEA, находят этот метод и
        позволяют запустить его одной кнопкой.
    */
    public static void main(String[] args) {
        // Создаем экземпляр нашего класса, чтобы получить доступ к его методам
        SleepIn solution = new SleepIn();

        System.out.println("Тестирование метода sleepIn:");

        // Тест 1: Не будний день, не отпуск -> спим
        // Ожидаемый результат: true
        System.out.println(solution.sleepIn(false, false));

        // Тест 2: Будний день, не отпуск -> не спим
        // Ожидаемый результат: false
        System.out.println(solution.sleepIn(true, false));

        // Тест 3: Не будний день, отпуск -> спим
        // Ожидаемый результат: true
        System.out.println(solution.sleepIn(false, true));
    }
}
