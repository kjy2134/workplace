class student:
    def __init__(self,string,number,grade):
        self.string = string
        self.number = number
        self.grade = grade
    
    def ave_num(self,score):
        self.list = [['programming',4,'A-'],['physics',3,'B-'],['english',3,'A'],['math',3,'B+']]
        self.sum = 0
        self.sum_p = 0
        self.list1= {'A+':4.5, 'A':4.3, 'A-':4.0,\
                'B+':3.5, 'B' : 3.3, 'B-' :3.0,\
                'C+' : 2.5, 'C':2.3, 'C-':2.0}
        for i in list:
            self.sum += list[1]*list1[list[2]]
            self.sum_p += list[1]
        grade_mean= round(self.sum /self.sum_p,2)
        return grade_mean
  

    def ave_grade():