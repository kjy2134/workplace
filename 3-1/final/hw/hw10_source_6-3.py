from tkinter import N
김민수 = {"name":"김민수", "assignment" : [80,50,40,20], "test":[75,75], "lab":[78.20, 77.20]}
이민아 = {"name":"이민아", "assignment": [82,56,44,30], "test":[83,95], "lab":[67.90, 78.32]}
배철수 = {"name":"배철수", "assignment":[77,82,23,39], \
    "test":[78,77], "lab":[80,80]}
    
def get_ave(marks):
    total_sum=sum(marks)
    total_sum=float(total_sum)
    return total_sum/len(marks)
def cal_total_ave(student):
    assignment= get_ave(student["assignment"])
    test = get_ave(student["lab"])
    lab = get_ave(student["lab"])
    return (0.1*assignment + 0.7 *test+0.2*lab)
def assign_letter_grade(s):
    if s >= 90: return "A"
    elif s>= 80: return "B"
    elif s>=70: return "C"
    elif s>=60: return "D"
    else: return "F"
def class_ave(student_list):
    print("students 리스크를 출력합니다(딕셔너리 리스트)")
    print(student_list)
    print()
    result_list = []
    for student in student_list:
        stu_avg=cal_total_ave(student)
        result_list.append(stu_avg)
    return get_ave(result_list)
student = [김민수, 이민아, 배철수]
for i in student:
    print(i["name"])
    print("==================================")
    assign_letter_grade(cal_total_ave(i))

    print()

    class_av= class_ave(student)
    print("반평균점수=%0.2f" %(class_av))
    print("반 전체 평균 등급= %s"%(assign_letter_grade(class_av)))