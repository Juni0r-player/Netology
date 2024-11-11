def average_value(numbers):
    if numbers:
        if isinstance(numbers, dict):
            some_list = []
            for value in numbers.values():
                some_list += value
            return sum(some_list)/len(some_list)
        else:
            return sum(numbers)/len(numbers)
    else:
        return 0

def courses_rating(persons, course):
    res = 0
    lenth = 0
    for person in persons:
        if course in person.grades:
            if person.grades[course]:
                res += average_value(person.grades[course])
                lenth += 1
    if lenth != 0:
        return res/lenth
    
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def lecture_rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if isinstance(0 <= grade <= 10) :
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                print("Неверная оценка")
        else:
            return 'Ошибка'
    
    def __str__(self):
        result = str(f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка: {average_value(self.grades)}\n"
            f"Курсы в процессе обучения: {', '.join(self.courses_in_progress)}\n"
            f"Завершенные курсы: {', '.join(self.finished_courses)}\n")
        return result 
     
    def __gt__(self, other):
        return average_value(self.grades) > average_value(other.grades)     
    def __lt__(self, other):
        return average_value(self.grades) < average_value(other.grades)  
    def __ge__(self, other):
        return average_value(self.grades) >= average_value(other.grades)    
    def __le__(self, other):
        return average_value(self.grades) <= average_value(other.grades)
          
        
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
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {average_value()(self.grades)}"
    
    def __gt__(self, other):
        return average_value(self.grades) > average_value(other.grades)    
    def __lt__(self, other):
        return average_value(self.grades) < average_value(other.grades)
    def __ge__(self, other):
        return average_value(self.grades) >= average_value(other.grades)
    def __le__(self, other):
        return average_value(self.grades) <= average_value(other.grades)
    

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'