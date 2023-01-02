
# 안녕
# 내 이름은 xxx이고 x살이야.
# 나는 xxxx에 살아.
# 매주 xxx마다 python을 배우고 있지.
# 10년 후에는 멋진 개발자가 되어 있을거야.

greeting = "안녕"
name = "백경진"
age = 10
nation = 'Canada'
city = 'Vancouver'

day = "토요일"
language = 'python'

print(greeting)
print("내 이름은 %s이고 %d살이야" %(name, age))
print("나는 {} {}에 살아.".format(nation, city))
print("매주 {0}마다 {1}을 배우고 있지.".format(day, language))

dream = input("너는 커서 뭐가 되고 싶어?")
year = input(f"몇년뒤 {dream}(이)가 되고 싶어? (숫자)")

print("{}년 후에는 {wannabe}가 되고 싶어.".format(str(year), wannabe = dream))
