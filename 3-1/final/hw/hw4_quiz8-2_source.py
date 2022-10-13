             #평수 추가

class house:
    def __init__(self, location, house_type,deal_type , price\
        , completion_year,area):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year=completion_year
        self.area = area

    def show_detail(self):
        print(self.location,self.house_type, self.deal_type,self.price\
            ,self.completion_year,self.area)

houses = []
house1 = house("강남", "아파트", "매매", "10억", "2010년","45평")
house2 = house("마포", "오피스텔", "전세", "5억", "2007년", "42평")
house3 = house("송파", "빌라", "월세", "500/50", "2000년", "23평")
house4 = house("종로", "한옥", "매매", "15억", "2020년", "32평")

houses.append(house1)
houses.append(house2)
houses.append(house3)
houses.append(house4)

print("총 {0}의 매물이 있습니다.", format(len(houses))) #houses리스트의 원소 개수 반환
for house in houses:
    house.show_detail()
