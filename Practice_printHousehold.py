
userInput = input("집에 거주하는 모든 사람의 이름을 입력하시오.")
memberList = userInput.split()
lastName = ""

lastNameDic = {}
for element in memberList:
    lastName = element[0]
    if  lastNameDic.get(lastName) == None:
        lastNameDic[lastName] = 1
    else :
        count = lastNameDic[lastName]
        lastNameDic[lastName] = count + 1

print(lastNameDic)

tempLastName = ""
for key, value in lastNameDic.items():
    if value == 1:
        tempLastName = key
        break

for element in memberList:
    print(element)
    if tempLastName in element:
        print(element)
