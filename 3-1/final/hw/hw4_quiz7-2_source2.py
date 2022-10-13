#약 3개월치(12주)의 보고서 파일 작성
for i in range(1,13):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report:
        report.write("- {0} 주차 주간보고 -".format(i))
        report.write("\n부서:")
        report.write("\n이름:")
        report.write("\n업무요약:")
        report.write("\n연락처:")

#연락처 항목 추가