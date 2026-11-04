package main

import (
	"bufio"         // Чтение ввода пользователя
	"encoding/json" // Работа с форматом JSON
	"fmt"           // Вывод текста на экран
	"os"            // Работа с файлами
	"strconv"       // Преобразование строк в числа
	"strings"       // Обработка строк
)

// Task — структура для хранения информации о задаче.
type Task struct {
	Title string `json:"title"` // Название задачи
	Done  bool   `json:"done"`  // Статус выполнения
}

// Имя файла для сохранения задач.
const fileName = "tasks.json"

// Функция загрузки задач из файла.
func loadTasks() ([]Task, error) {

	// Читаем содержимое файла.
	data, err := os.ReadFile(fileName)

	// Если файла ещё нет, создаём пустой список.
	if os.IsNotExist(err) {
		return []Task{}, nil
	}

	// Проверяем наличие ошибки чтения.
	if err != nil {
		return nil, err
	}

	// Создаём срез для хранения задач.
	var tasks []Task

	// Преобразуем JSON в структуры Go.
	if err := json.Unmarshal(data, &tasks); err != nil {
		return nil, err
	}

	return tasks, nil
}

// Функция сохранения задач в файл.
func saveTasks(tasks []Task) error {

	// Преобразуем список задач в JSON.
	data, err := json.MarshalIndent(tasks, "", "  ")

	if err != nil {
		return err
	}

	// Записываем данные в файл.
	return os.WriteFile(fileName, data, 0600)
}

// Главная функция программы.
func main() {

	// Загружаем ранее сохранённые задачи.
	tasks, err := loadTasks()

	if err != nil {
		fmt.Println("Ошибка загрузки:", err)
		return
	}

	// Создаём инструмент для чтения ввода.
	input := bufio.NewScanner(os.Stdin)

	// Основной цикл программы.
	for {

		// Выводим меню на экран.
		fmt.Println("\n=== МЕНЕДЖЕР ЗАДАЧ ===")
		fmt.Println("1. Добавить задачу")
		fmt.Println("2. Показать задачи")
		fmt.Println("3. Отметить выполненной")
		fmt.Println("4. Удалить задачу")
		fmt.Println("5. Выход")

		fmt.Print("Выберите действие: ")

		// Считываем выбранный пункт.
		if !input.Scan() {
			return
		}

		// Убираем лишние пробелы.
		choice := strings.TrimSpace(input.Text())

		// Флаг изменения списка задач.
		changed := false

		// Выбираем действие пользователя.
		switch choice {

		case "1":

			// ДОБАВЛЕНИЕ ЗАДАЧИ

			fmt.Print("Введите название задачи: ")

			if !input.Scan() {
				return
			}

			title := strings.TrimSpace(input.Text())

			// Проверяем, что название не пустое.
			if title == "" {
				fmt.Println("Название не может быть пустым!")
				break
			}

			// Добавляем новую задачу в список.
			// Изначально задача не выполнена.
			tasks = append(tasks, Task{
				Title: title,
				Done:  false,
			})

			fmt.Println("Задача добавлена!")
			changed = true

		case "2":

			// ПРОСМОТР СПИСКА ЗАДАЧ

			// Проверяем, есть ли задачи.
			if len(tasks) == 0 {
				fmt.Println("Список задач пуст.")
			}

			// Перебираем все задачи.
			for i, task := range tasks {

				// Пробел означает невыполненную задачу.
				status := " "

				// Если задача выполнена, ставим x.
				if task.Done {
					status = "✓"
				}

				// Выводим номер, статус и название.
				fmt.Printf("%d. [%s] %s\n",
					i+1, status, task.Title)
			}

		case "3", "4":

			// ВЫПОЛНЕНИЕ ИЛИ УДАЛЕНИЕ ЗАДАЧИ

			// Проверяем, что список не пустой.
			if len(tasks) == 0 {
				fmt.Println("Список задач пуст.")
				break
			}

			fmt.Print("Введите номер задачи: ")

			if !input.Scan() {
				return
			}

			// Преобразуем введённую строку в число.
			number, err := strconv.Atoi(
				strings.TrimSpace(input.Text()),
			)

			// Проверяем корректность номера.
			if err != nil || number < 1 ||
				number > len(tasks) {
				fmt.Println("Неверный номер задачи!")
				break
			}

			// Индексация срезов в Go начинается с 0.
			index := number - 1

			if choice == "3" {

				// Отмечаем задачу выполненной.
				tasks[index].Done = true

				fmt.Println("Задача выполнена!")

			} else {

				// Удаляем выбранную задачу из среза.
				tasks = append(
					tasks[:index],
					tasks[index+1:]...,
				)

				fmt.Println("Задача удалена!")
			}

			changed = true

		case "5":

			// ЗАВЕРШЕНИЕ ПРОГРАММЫ

			fmt.Println("До свидания!")
			return

		default:

			// Обработка неправильного пункта меню.
			fmt.Println("Выберите число от 1 до 5!")
		}

		// Если задачи изменились, сохраняем их.
		if changed {
			if err := saveTasks(tasks); err != nil {
				fmt.Println("Ошибка сохранения:", err)
			}
		}
	}
}
