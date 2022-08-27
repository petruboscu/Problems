class Student:
    count = 0

    def __init__(self, name: str, surname: str, age: int, degree: str, scholar_ship: bool):
        self.name = name
        self.surname = surname
        self.age = age
        self.degree = degree
        self.scholar_ship = scholar_ship
        Student.count += 1

    def __del__(self):
        Student.count -= 1

    def get_full_name(self):
        return self.name + ' ' + self.surname


def show_student_full_names(students: list):
    names = []
    for student in students:
        names.append(student.get_full_name())
    print('Names: ' + ', '.join(names))


if __name__ == '__main__':
    university_students = [Student('Petru', 'Boscu', 20, 'Physics', True),
                           Student('Hello', 'World', 4, 'Physics', False)]

    high_school_student = [Student('Hero', 'Neko', 16, 'Physics', True),
                           Student('Hello', 'World', 0, 'Physics', False)]

    show_student_full_names(university_students)
    show_student_full_names(high_school_student)

    print('Total student count: ' + str(Student.count))
