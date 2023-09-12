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
    

def student_course_average_rate(student_list, course):
    sum_average = 0
    student_count = 0
    for student in student_list:        
        if course in student.grades:
            sum_average += student.grades[course]
            student_count += 1
    return sum_average / student_count

def lecturer_course_average_rate(lecturer_list, course):
    sum_average = 0
    lecturer_count = 0
    for lecturer in lecturer_list:        
        if course in lecturer.grades:
            sum_average += lecturer.grades[course]
            lecturer_count += 1
    return sum_average / lecturer_count

stud1 = Student('Tony', 'Zinner', 'male')
stud1.finished_courses = ["Git"]
stud1.courses_in_progress = ["Python", "Java"]
stud1.grades = {"Git": 10, "Python": 10, "Java": 8}

stud2 = Student('Max', 'Rute', 'male')
stud2.finished_courses = ["Git", "Texts"]
stud2.courses_in_progress = ["Python", "Java"]
stud2.grades = {"Git": 8, "Texts": 9, "Python": 10}

rev1 = Reviewer("Tom", "Smith")
rev1.courses_attached =["Python"]
rev2 = Reviewer("Genry", "Pups")
rev2.courses_attached = ["Java"]
rev1.courses_attached = ["Git", "Texts", "Java", "Python"]
rev2.courses_attached = ["Git", "Texts", "Java", "Python"]

lec1 = Lecturer("Villy", "Gery") 
lec2 = Lecturer("Sam", "Winter")
lec1.grades = {"Git": 7, "Texts": 9, "Java": 8}
lec2.grades = {"Git": 10, "Texts": 5, "Python": 10, "Java": 10}
lec1.courses_attached = ["Git", "Texts", "Java"]
lec2.courses_attached = ["Git", "Texts", "Java", "Python"]

print(stud1.add_finished_courses("Texts"))
print(stud2.rate_lecturer(lec1, "Python", 10))
print(stud1)
print(stud1 < stud2)

print(lec1)
print(lec1 > lec2)

print(rev1)
print(rev2.rate_student(stud2, "Java", 8))

print(lecturer_course_average_rate([lec1, lec2], "Python"))
print(student_course_average_rate([stud1, stud2], "Git"))
