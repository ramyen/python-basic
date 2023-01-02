



# 정수 : integer = int
# 문자열 : string = str



def SendMsg(name:str, msgFormat:str):
    print(msgFormat.format(_name=name))

# templist = ["송윤근", "송영근", "송준백", "주경희", "백경진"]
# templist = [1001, 1002, 1004, 1008, 9778768]

templist = list()
templist.append("송윤근")
templist.append("송영근")
templist.append("송준백")
templist.append("주경희")
templist.append("백경진")
 
msgFormat = "{_name}님, 5분 후에 서버가 종료됩니다."


for name in templist:
    SendMsg(name, msgFormat)


templist.remove("송영근")


msgFormat = "{_name}님, 1분 후에 서버가 종료됩니다."
for name in templist:
    SendMsg(name, msgFormat)