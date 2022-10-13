class person:
    def __init__(self,name,number):
        self.name = name
        self.number=number

class student(person):
    ungra = 0
    pogra = 1

    def __init__(self, name, number, studenttype):
        super().__init__(name,number)
        self.studenttype = studenttype
        self.gpa=0
        self.classes =[]
    
    def enrollcourse(self, course):
        self.classes.append(course)
    
    def __str__(self):
        return "\n이름=" + self.name + "\n주민번호=" + self.number + "\n수강과목=" +str(self.classes)\
             + "\n평점" +str(self.gpa)

class teacher(person):
    def __init__(self, name, number):
        super().__init__(name,number)
        self.courses=[]
        self.salary=3000000
    
    def assign(self, course):
        self.courses.append(course)
    
    def __str__(self):
        return "\n이름=" + self.name + "\n주민번호=" + self.number + "\n강의과목=" +str(self.courses)\
             + "\n월급=" +str(self.salary)

print("(1)----person클래스 상속에 의한 strudent 및 teacher 클래스 생성")

hong = student("홍길동", "12345678", student.ungra)
hong.enrollcourse("자료구조")
print(hong)

kim = teacher("김철수", "123456790")
kim.assign("python")
print(kim)