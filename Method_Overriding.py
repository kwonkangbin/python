#클래스는 개념 위주로 냄 휴먼 만들었던 부분 잘봐라 인스턴스 시험!!!(1분 파이썬 보기),상속개념 중요







# #마린
# name = "마린"
# hp = 40
# damege = 5

# print(f"\n {name} 유닛이 생성되었습니다. ")
# print(f"체력 {hp} , 공격력 {demage}")

# #탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_demage = 35

# print(f"\n {tank_name} 유닛이 생성되었습니다. ")
# print(f"체력 {tank_hp} , 공격력 {tank_demage}")

# def attack(name,location,demage):
#     print(f"\n{name} : {location} 방향으로 적국을 공격합니다. 공격력 : {damage}")
    
# attack(name, "1시",demage)
# attack(tank_name, "2시",tank_demage)

class Unit : 
	def __init__(self,name,hp,demage):
		self.name = name
		self.hp = hp
		self.demage = demage
		print("\n {} 유닛이 생성되었습니다.".format(self.name))
		print(f"체력 {self.hp} , 공격력 {self.demage}")

marine1 = Unit("마린",40,5)
marine2 = Unit("마린",40,5)
tank = Unit("탱크",150,35)
