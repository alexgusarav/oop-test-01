class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _averagerating(self, grades):
        rate = 0
        len_rate = 0
        for value in grades.values():
            rate += sum(value)
            len_rate += len(value)
        return round(rate/len_rate, 1)

    def __str__(self):
        return (f'Имя:{self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._averagerating(self.grades)}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and
                (course in self.courses_in_progress or course in self.finished_courses)
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        return self._averagerating(self.grades) < other._averagerating(other.grades)

    def __gt__(self, other):
        return self._averagerating(self.grades) > other._averagerating(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def rate_hw(self, student, course, grade):
        return "нет прав"

    def _averagerating(self, grades):
        rate = 0
        len_rate = 0
        for value in grades.values():
            rate += sum(value)
            len_rate += len(value)
        return round(rate/len_rate, 1)

    def __str__(self):
        return f"Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._averagerating(self.grades)}"

    def __lt__(self, other):
        return self._averagerating(self.grades) < other._averagerating(other.grades)

    def __gt__(self, other):
        return self._averagerating(self.grades) > other._averagerating(other.grades)

class Reviewer(Mentor):

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def averageratinglector(lektors, course):
    rate=0
    lenrate=0
    for lektor in lektors:
        if course in lektor.courses_attached and isinstance(lektor, Lecturer):
            rate += sum(lektor.grades[course])
            lenrate += len(lektor.grades[course])
    return round(rate/lenrate, 1)

def averageratingstudent(students, course):
    rate=0
    lenrate=0
    for student in students:
        if (course in student.finished_courses or course in student.courses_in_progress) and isinstance(student, Student):
            rate += sum(student.grades[course])
            lenrate += len(student.grades[course])
    return round(rate/lenrate, 1)

student1 = Student('Ivan', 'Ivanov', 'your_gender')
student1.courses_in_progress += ['Python']

student2 = Student('Petr', 'Petrov', 'your_gender')
student2.courses_in_progress += ['Python']

reviever1 = Reviewer('Oleg', 'Buligin')
reviever1.courses_attached += ['Python']

lektor1 = Lecturer('Elena', 'Nikitina')
lektor1.courses_attached += ['Python']

lektor2 = Lecturer('Evgeniy', 'Shmargunov')
lektor2.courses_attached += ['Python']

reviever1.rate_hw(student1, 'Python', 8)
reviever1.rate_hw(student1, 'Python', 9)
reviever1.rate_hw(student2, 'Python', 10)
reviever1.rate_hw(student2, 'Python', 5)

student1.rate_hw(lektor1, 'Python', 9)
student1.rate_hw(lektor2,'Python', 8)
student2.rate_hw(lektor1,'Python', 10)
student2.rate_hw(lektor2,'Python', 10)

print(reviever1)
print('\n')
print(lektor2)
print('\n')
print(student1)
print('\n\n')

print(lektor1._averagerating(lektor1.grades))
print(lektor2._averagerating(lektor2.grades))
print(lektor1 > lektor2)

print(student1._averagerating(student1.grades))
print(student2._averagerating(student2.grades))
print(student1 <student2)

print(f'Средняя оценка Лекторов: {averageratinglector([lektor1,lektor2], "Python")}')
print(f'Средняя оценка Студентов: {averageratingstudent([student1,student2], "Python")}')
