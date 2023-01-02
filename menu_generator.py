

import random

countMax = 5

# menu = []
menu = set()
# menu = {0:"라면", 1:"아이스크림", 2:"돈까스"}


# while len(menu) < countMax:
#     curCount = len(menu)
#     menuName = input("먹고 싶은 메뉴를 입력하시오.")
#     if menuName in menu:
#         print("중복된 메뉴입니다.")
#     else:
#         menu.add(menuName)
# ran = random.choice(list(menu))
# print(ran)

items = input("먹고 싶은 메뉴를 입력하시오.")
menulist = items.split("/")
ran = random.choice(menulist)
print(ran)


