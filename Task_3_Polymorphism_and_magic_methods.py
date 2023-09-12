class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finished_courses(self, course_name):
        self.finished_courses.append(course_name)
        return self.finished_courses

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
            return lecturer.grades
        else:
            return 'Ошибка'

    def _average_grade_student(self):
        grades = list(self.grades.values())
        sum_grade = 0
        for grade in grades:
            sum_grade += grade

        average_grade = sum_grade / len(grades)
        return average_grade
    
    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n' 
            f'Средняя оценка за лекции: {self._average_grade_student()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        )
    
    def __lt__(self, other):
        if isinstance(other, Student):
            if self._average_grade_student() < other._average_grade_student():
                return True
            else: 
                return False
        return "Ошибка"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade_lecturer()}'

    def _average_grade_lecturer(self):
        grades = list(self.grades.values())
        sum_grade = 0
        for grade in grades:
            sum_grade += grade

        average_grade = sum_grade / len(grades)
        return average_grade
    
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if self._average_grade_lecturer() < other._average_grade_lecturer():
                return True
            else: 
                return False
        return "Ошибка"


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            return student.grades
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

