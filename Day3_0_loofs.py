
import random
from secrets import choice
from unittest import result

numberList = list(range(1, 46))
# print(numberList)

resultList = set()
resultDic = {0:("현중", "학생", "밴쿠버")}
testValue = resultDic.get(0)
print(testValue[0])
print(testValue[1])
print(testValue[2])

list : 중복가능 / 순서 보장 / 하나씩 검색 => 느림
set : 중복가능X / 순서 보장X / Value 하나씩만 넣을 수 있어 / 검색 속도 빠름
dict : 중복가능X / 순서 보장X / Key : Value 를 쌍으로 넣어야 됨 /  검색 속도 개빠름
tuple : 중복가능 / 순서 보장 / 아무 Value 넣을 수 있어 / 검색 느림.


# for i in range(6):

# while len(resultList) < 6:
#     selected = choice(numberList)
#     # if not selected in resultList:
#     if selected in resultList:
#         resultList.add(selected)

# print(resultList)







# random.shuffle(numberList)
# print(numberList)

# for i in range(6):
#     selected = numberList.pop()
#     print(selected)

# print(numberList)

# menuList = []
# run = True
# while run :
#     dinner = input("원하는 저녁 메뉴를 입력하시오.")

#     if dinner == "exit":
#         run = False
#     else:
#         menuList.append(dinner)

# print(menuList)
# choiced = random.choice(menuList)
# print(choiced)
# menuList.remove(choiced)
# print(menuList)

# menuList = ["카레", "짬뽕", "라면", "김치찌게", "생선구이"]

# dinner = input("먹고싶은 메뉴를 입력하시오")
# found = False
# for element in menuList:
#     if element == dinner:
#         print(f"{dinner}가 해당 매뉴에 있습니다.")
#         found = True
#         break


# if found == False:
#     print(f"{dinner}가 해당 매뉴에 없습니다. 엄마에게 말하세요")






# def ShowList(list:list):
#     index =0
#     print("=========")
#     for element in list:
#         print(f"Index : {index} = {element}")
#         index += 1

# list0 = [1,2,3,4,5]
# ShowList(list0)

# list0.append(6)
# ShowList(list0)

# list0.remove(3)
# ShowList(list0)

# poppedNumber = list0.pop()o
# print(f"poppedNumber: {poppedNumber}")
# ShowList(list0)

# rangeObj = range(4, 10)
# for element in rangeObj:
#     print(element)

# print(list(rangeObj))

# import random


# tempList = [1,2,3]

# print(tempList)
# tempList[0] = 100


# tempInput = ""
# testBool = True
# while(testBool):
#     tempInput = input("입력하세요.")

#     if tempInput == "exit":
#         testBool = False

# comInt = random.randint(0, 99)
# count = 0
# while count < 20:
#     tempInput = int(input("입력하세요."))

#     if tempInput == comInt:
#         print("Win!!!")
#         break
#     else:
#         count += 1

# if count == 20:
#     print("Failure!!")