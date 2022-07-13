class InvalidStudentType(Exception):
    def __init__(self):
        self.message = 'Invalid student type, must be either UG or PG'


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.journals = []

    def set_student_type(self, student_type):
        if student_type not in ['UG', 'PG']:
            raise InvalidStudentType
        else:
            self.student_type = student_type

    def set_student_cgpa(self, cgpa):
        try:
            self.cgpa = int(cgpa)
        except ValueError:
            print("CGPA has to be floating number")

    def add_student_journal(self, title):
        self.journals.append(title)

    def get_student_cgpa(self):
        return self.cgpa

    def get_student_type(self):
        return self.student_type

    def get_student_journals(self):
        return self.journals


try:
    s1 = Student('Amit', 29)
    s1.set_student_type('UG')
    print(s1.student_type)

except Exception as err:
    print('Some exception occurred', err.message)





