import tkinter as tk
from tkinter import messagebox  # Убрал лишний Listbox

MIN_GRADE = 1
MAX_GRADE = 5

# Глобальные переменные (плохо!)
student_list = []
current_id = 1

ENABLE_LOGGING = True

def log_action(action):
    if ENABLE_LOGGING:
        with open("log.txt", "a") as file:
            file.write(action + "\n")

def validate_grade(grade):
    if not grade.isdigit():
        return False

    grade = int(grade)
    return MIN_GRADE <= grade <= MAX_GRADE

# Смешанная логика и интерфейс (плохо!)
def create_student(student_id, name, group):
    return {
        "id": student_id,
        "name": name,
        "group": group,
        "grades": []
    }
def add_student():
    global current_id, name_entry, group_entry, listbox  # ❗ ДОБАВЛЕНО: нужен доступ к глобальным переменным
    
    name = name_entry.get()
    group = group_entry.get()

    if name and group:  # ❗ ИСПРАВЛЕНО: правильный отступ
        student = create_student(current_id, name, group)
        student_list.append(student)
        log_action("Student added")
        current_id += 1

        # Обновляем список в интерфейсе
        listbox.insert(tk.END, f"{student['id']}: {student['name']} ({student['group']})")

        # Очищаем поля
        name_entry.delete(0, tk.END)
        group_entry.delete(0, tk.END)
    else:  # ❗ ИСПРАВЛЕНО: else на одном уровне с if
        messagebox.showwarning("Ошибка", "Заполните все поля!")

def add_grade():
    try:
        selection = listbox.curselection()[0]
        student = student_list[selection]

        grade = grade_entry.get()
        if validate_grade(grade):
            student["grades"].append(int(grade))
            log_action("Grade added")
            grade_entry.delete(0, tk.END)
            messagebox.showinfo("Успех", f"Оценка {grade} добавлена для {student['name']}")
        else:
            messagebox.showwarning(
                "Ошибка",
                f"Введите число от {MIN_GRADE} до {MAX_GRADE}"
            )
    except:
        messagebox.showwarning("Ошибка", "Выберите студента!")

# Создание интерфейса (всё в одной функции!)
def create_gui():
    global name_entry, group_entry, grade_entry, listbox

    root = tk.Tk()
    root.title("Учет студентов (Legacy версия)")
    root.geometry("500x400")

    # Поля для ввода
    tk.Label(root, text="ФИО студента:").pack(pady=5)
    name_entry = tk.Entry(root, width=40)
    name_entry.pack(pady=5)

    tk.Label(root, text="Группа:").pack(pady=5)
    group_entry = tk.Entry(root, width=40)
    group_entry.pack(pady=5)

    tk.Button(root, text="Добавить студента", command=add_student).pack(pady=10)

    # Список студентов
    listbox = tk.Listbox(root, width=50, height=10)
    listbox.pack(pady=10)

    # Добавление оценки
    tk.Label(root, text="Добавить оценку:").pack(pady=5)
    grade_entry = tk.Entry(root, width=10)
    grade_entry.pack(pady=5)
    tk.Button(root, text="Добавить оценку", command=add_grade).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
