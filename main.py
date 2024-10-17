#Создай класс Task, который позволяет управлять задачами (делами).
# У задачи должны быть атрибуты: описание задачи, срок выполнения и
# статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода
# списка текущих (не выполненных) задач.

class Task:
    def __init__(self, description, term, status=False):
        """Инициализация задачи: описание, срок и статус (по умолчанию 'не выполнено')"""
        self.description = description
        self.term = term  # срок выполнения
        self.status = status  # False для невыполненных задач, True для выполненных

    def add_description(self, text):
        """Добавление/обновление описания задачи"""
        self.description = text

    def mark_done(self):
        """Отметка задачи как выполненной"""
        self.status = True

    def __str__(self):
        """Строковое представление задачи"""
        return f"Задача: {self.description}, Срок: {self.term}, Статус: {'Выполнено' if self.status else 'Не выполнено'}"


class TaskManager:
    def __init__(self):
        """Инициализация списка задач"""
        self.tasks = []

    def add_task(self, description, term):
        """Добавление новой задачи в список"""
        task = Task(description, term)
        self.tasks.append(task)

    def mark_task_done(self, index):
        """Отметка задачи как выполненной по индексу"""
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            print("Задача с таким индексом не найдена")

    def show_incomplete_tasks(self):
        """Вывод списка текущих (невыполненных) задач"""
        print("Невыполненные задачи:")
        for i, task in enumerate(self.tasks):
            if not task.status:
                print(f"{i + 1}. {task}")


# Пример использования
manager = TaskManager()
manager.add_task("Купить продукты", "2024-10-15")
manager.add_task("Сдать отчет по проекту", "2024-10-20")
manager.add_task("Записаться к врачу", "2024-10-17")

# Вывод всех текущих невыполненных задач
manager.show_incomplete_tasks()

# Отметка первой задачи как выполненной
manager.mark_task_done(1)

# Вывод списка невыполненных задач снова
manager.show_incomplete_tasks()



