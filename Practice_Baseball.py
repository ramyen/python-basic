# Practice [Base Ball]

# CPU는 3자리 수를 랜덤으로 만든다.
# 같은 숫자는 나올 수 없다.
# 유저는 3자리 수를 입력한다.
# 유저가 입력한 수가, CPU가 만든 수와 비교한다.
# 정해진 기회안에 CPU의 수를 맞추면 이기는 게임

# 조건 1, 같은 수, 같은 자리 일 경우 1 Strike
# 조건 2, 같은 수, 다른 자리 일 경우 1 Ball
# 조건 3, USER가 입력한 숫자가 CPU값에 없는 경우 1 Out
# ex)
# 143(CPU), 156(USER) = 1 Strike
# 925(CPU), 457(USER) = 1 Ball 2 OUT

import random as ran
from typing import Tuple

def isValidNumber(number:str) -> bool:
    for i in range(len(number)):
        singleInput = number[i:i+1]
        otherInput = number[i+1:]
        if otherInput.find(singleInput) != -1:
            return False

    return True

def getRandom3digit(digit:int) -> str:
    val = ""
    while (len(val) < digit):
        tempInt = ran.randint(0, 9)
        if val.find(str(tempInt)) == -1:
            val += str(tempInt)
    
    return val

def checkResult(cpuInput:str, userInput:str) -> tuple[bool, str]:
    result = False
    strike = 0
    ball = 0
    out = 0

    if cpuInput != userInput:
        for i in range(len(userInput)):
            userSingleInput = userInput[i:i+1]
            index = cpuInput.find(userSingleInput)
            if index == i:
                strike += 1
            elif index != -1:
                ball += 1
            else:
                out += 1

    else:
        result = True
        strike = 3

    return [result, str(f"{strike} Strike / {ball} Ball / {out} Out")]


tryCount = 10
currentCount = 0
cpuNum = getRandom3digit(3)
lastResult = Tuple[bool, str]


print("================[BASE BALL]================")
content = """
CPU는 3자리 수를 랜덤으로 만든다.\n
이 숫자안에는 같은 숫자가 중복되지는 않는다.\n
유저는 3자리 수를 입력한다.\n
정해진 기회안에 CPU의 수를 맞추면 이기는 게임이다.\n
"""
print(content)
print("================[게임 시작]================")

while currentCount < tryCount:

    userNum = input(f"[{currentCount + 1}번째 시도] 3자리 수를 입력하시오\n")
    if userNum.isnumeric() == False:
        print(f"{userNum}는 숫자가 아닙니다.")
        continue
    elif len(userNum) != 3:
        print(f"{userNum}는 3자리 수가 아닙니다.")
        continue
    elif isValidNumber(userNum) == False:
        print(f"{userNum}에는 중복된 수가 있습니다.")
        continue
        
    lastResult = checkResult(cpuNum, userNum)

    if  lastResult[0] == True:
        break
    else:
        currentCount += 1
        print(f"[{userNum}]Result : {lastResult[1]}")


if lastResult[0] == True:
    print("================[게임 승리!!!]================")
else:
    print(f"================[게임 패배 ㅠㅠ] : CPU Number : {cpuNum}================")