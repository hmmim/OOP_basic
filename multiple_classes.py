#Object Orientated Programming in Python
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade  #0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name,max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        #self.is_active = False
    def add_student(self,student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/ len(self.students)

s1 = Student("Kane", 20, 65)
s2 = Student("Jude", 20, 76)
s3 = Student("Kyle", 20, 89)
course = Course("Science",3)
course.add_student(s1)
course.add_student(s2)
#print(course.students[0].name)
print(course.get_average_grade())
print(course.add_student(s3))



