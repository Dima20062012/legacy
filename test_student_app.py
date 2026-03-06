import unittest

from legacy_student_app import students

def add_student_test(name, group):
    student = {
        "id": len(students) + 1,
        "name": name,
        "group": group,
        "grades": []
    }

    students.append(student)

    return student

def add_grade_test(student, grade):
    student["grades"].append(grade)

class TestStudentApp(unittest.TestCase):

    def setUp(self):
        students.clear()

    # Test 1
    def test_add_student(self):

        student = add_student_test("Иванов", "ИС-101")

        self.assertEqual(student["name"], "Иванов")
        self.assertEqual(student["group"], "ИС-101")
        self.assertEqual(len(students), 1)

    # Test 2
    def test_add_grade(self):

        student = add_student_test("Петров", "ИС-102")

        add_grade_test(student, 5)

        self.assertEqual(student["grades"], [5])

    # Test 3
    def test_multiple_grades(self):

        student = add_student_test("Сидоров", "ИС-103")

        add_grade_test(student, 4)
        add_grade_test(student, 5)

        self.assertEqual(student["grades"], [4, 5])

if __name__ == "__main__":
    unittest.main()
