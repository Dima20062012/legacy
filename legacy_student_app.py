import tkinter as tk
from tkinter import messagebox  # Убрал лишний Listbox

# Глобальные переменные (плохо!)
students = []
current_id = 1

# Смешанная логика и интерфейс (плохо!)
def add_student():
    global current_id, name_entry, group_entry, listbox  # ❗ ДОБАВЛЕНО: нужен доступ к глобальным переменным
    
    name = name_entry.get()
    group = group_entry.get()

    if name and group:  # ❗ ИСПРАВЛЕНО: правильный отступ
        student = {
            "id": current_id,
            "name": name,
            "group": group,
            "grades": []
        }
        students.append(student)
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
        student = students[selection]

        grade = grade_entry.get()
        if grade and grade.isdigit():
            student["grades"].append(int(grade))
            grade_entry.delete(0, tk.END)
            messagebox.showinfo("Успех", f"Оценка {grade} добавлена для {student['name']}")
        else:
            messagebox.showwarning("Ошибка", "Введите число от 1 до 5")
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
