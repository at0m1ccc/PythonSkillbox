from random import randint


class Student:
    def __init__(self, name, num_group, grade):
        self.name = name
        self.num_group = num_group
        self.grade = grade

    def average_grade(self):
        return sum(self.grade) / len(self.grade)

    def info_student(self):
        print(f'{self.name}, Номер группы: {self.num_group}, оценки: {self.grade}')


def sort_students(students_list):
    return sorted(students_list, key=lambda item: item.average_grade())


students = [Student(input(f'Введите имя {index + 1} студента: '),
                    randint(0, 1),
                    [randint(2, 5) for _ in range(5)]) for index in range(10)]

students = sort_students(students)

print('\nСтуденты отсортированные по среднему баллу:')
for student in students:
    student.info_student()
