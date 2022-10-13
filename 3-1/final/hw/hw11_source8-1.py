def cre_stu(name, korean, math, english, science):
    return{"name" : name , "korean" : korean, "math" : math, "english" : english, "science" : science}

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_ave(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(student["name"],student_get_sum(student),student_get_ave(student))

students= [
    cre_stu("윤인성", 87,98,88,95),
    cre_stu("연하진",92,98,96,98),
    cre_stu("구지연", 76,96,94,90),
    cre_stu("나선주", 98,92,96,92),
    cre_stu("윤아린", 95,98,98,98),
    cre_stu("윤명월", 64,88,92,92)
]

print("딕셔너리 활용 성적 처리")
print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))