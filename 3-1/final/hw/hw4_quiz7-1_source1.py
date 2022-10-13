# 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.

# - x주차 주간 보고 -
# 부서 : 
# 이름 : 
# 업무 요약 :

# 1주차부터 50주차 까지의 보고서 파일을 만드는 프로그램이 만든다"-

for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서:")
        report_file.write("\n이름:")
        report_file.write("\n업무요약:")

#open : 파일을 엶
#w: 쓰기위한 파일
#a: 파일 뒤에 이어서 씀
#r : 파일을 읽어옴
# read(): 터미널 영역에 파일 내용 읽어서 불러옴
# readline(): 줄별로 읽어옴
# utf8 : 한글 정상 출력을 위해 씀
# write : 텍스트를 입력해놓음

