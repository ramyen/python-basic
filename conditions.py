
testSet = {0, 1, "hello", 5.67}

print("hello" in testSet)
print(7 in testSet)


testDic = {0:"송윤근", 7:"주경희", 9:"송준백", 1:"송영근", "아배고파":"뭐먹지"}
print(testDic)

print(1 in testDic)
# print(testDic["아배고"])
print(testDic.get("아배고"))

if "아배고" in testDic:
    print(testDic["아배고"])


# testList = [0, 1,2,3,4,5,6]

# for element in testList:
#     print(element)
