from statistics import mean


allowable_grades = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def get_average_grade(grades) -> float:
    """Возвращает среднее значение всех оценок из словаря 'grades' по всем курсам с округлением до 1 знака после запятой.
    """
    all_grades = []
    for course_grades in grades.values():
        all_grades += course_grades
    return round(mean(all_grades), 1)

def show_course_average_grade(course, cls):
    """Показывает среднее значение всех оценок по курсу 'course' среди всех членов класса 'cls' с округлением до 1 знака после запятой.
    """
    all_grades = []
    for person in cls.list_of_all:
        if course.title() in person.grades:
            all_grades += person.grades[course.title()]
        else:
            continue
    print(f'Средния оценка по курсу "{course.title()}" среди всех {cls.__name__}s - {round(mean(all_grades), 1)}\n')



class Person:
    def __init__(self, name, last_name):
        self.name = name.title()
        self.last_name = last_name.title()

class Student(Person):
    list_of_all = []

    def __init__(self, name, last_name, gender):
        super().__init__(name, last_name)
        self.gender = gender.lower()
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.list_of_all.append(self)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and grade in allowable_grades and course.title() in self.courses_in_progress and course.title() in lecturer.courses_attached:
            if course.title() in lecturer.grades:
                lecturer.grades[course.title()] += [grade]
            else:
                lecturer.grades[course.title()] = [grade]
        else:
            print('Ошибка')
            # return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\nФамилия: {self.last_name}\nСредняя оценка за домашние задания: {get_average_grade(self.grades)}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        )

    def __eq__(self, other):
        if isinstance(other, Student):
            if get_average_grade(self.grades) > get_average_grade(other.grades):
                print(f'Средняя оценка {self.name} выше чем у {other.name} - {get_average_grade(self.grades)}')
            elif get_average_grade(self.grades) < get_average_grade(other.grades):
                print(f'Средняя оценка {other.name} выше чем у {self.name} - {get_average_grade(other.grades)}')
            else:
                print(f'{self.name} и {other.name} имеют одинаковую среднюю оценку - {get_average_grade(self.grades)}')
            print()
        else:
            print('Ошибка')
            # return 'Ошибка'


class Mentor(Person):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.courses_attached = []

class Lecturer(Mentor):
    list_of_all = []

    def __init__(self, name, last_name):
        super().__init__(name, last_name)
        self.grades = {}
        self.list_of_all.append(self)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.last_name}\nСредняя оценка за лекции: {get_average_grade(self.grades)}'

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if get_average_grade(self.grades) > get_average_grade(other.grades):
                print(f'Средняя оценка {self.name} выше чем у {other.name} - {get_average_grade(self.grades)}')
            elif get_average_grade(self.grades) < get_average_grade(other.grades):
                print(f'Средняя оценка {other.name} выше чем у {self.name} - {get_average_grade(other.grades)}')
            else:
                print(f'{self.name} и {other.name} имеют одинаковую среднюю оценку- {get_average_grade(self.grades)}')
        else:
            print('Ошибка')
            # return 'Ошибка'

class Reviewer(Mentor):
    def __init__(self, name, last_name):
        super().__init__(name, last_name)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and grade in allowable_grades and course.title() in self.courses_attached and course.title() in student.courses_in_progress:
            if course.title() in student.grades:
                student.grades[course.title()] += [grade]
            else:
                student.grades[course.title()] = [grade]
        else:
            print('Ошибка')
            # return 'Ошибка'
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.last_name}'


# Создание объектов
jake = Student('jake', 'gyllenhaal', 'male')
jake.courses_in_progress += ['Python', 'C++']
jake.finished_courses.append('Git')
jake.grades['Python'] = [6, 9, 10]
jake.grades['C++'] = [5, 7, 9]
jake.grades['Git'] = [9, 10]

emily = Student('emily', 'blunt', 'female')
emily.courses_in_progress.append('C++')
emily.finished_courses += ['Python']
emily.grades['C++'] = [8, 9, 8]
emily.grades['Python'] = [10, 9, 10]

michelle = Reviewer('michelle', 'yeoh')
michelle.courses_attached += ('Python', 'Git')

joel = Reviewer('joel', 'kinnaman')
joel.courses_attached.append('C++')

jackie = Lecturer('jackie', 'chan')
jackie.courses_attached.append('Python')
jackie.grades['Python'] = [9, 10, 10]
jackie.grades['C++'] = [4, 7, 6]

hiroshi = Lecturer('hiroshi', 'kamiya')
hiroshi.courses_attached += ['C++', 'Git']
hiroshi.grades['Git'] = [4, 6, 7]
hiroshi.grades['C++'] = [8, 7, 10]

# Проверка функционала
print(hiroshi)
print()
jake.rate_lecture(hiroshi, 'c++', 6)
print(hiroshi)
print()

joel.rate_hw(jake, 'c++', 4)
print(jake)
print()

hiroshi == jackie
emily == jake


show_course_average_grade('python', Student)
show_course_average_grade('c++', Lecturer)