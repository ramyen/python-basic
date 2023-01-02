def add(first, second):
    return first + second

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return f"Can't be divided by zero"
    return a / b

def multiply(a, b):
    return a * b

def split(source:str, delimiters:set[str]) -> tuple[list[str], list[str]]:
    valList = []
    operatorList = []
    startIndex = -1
    for index in range(len(source)):
        c = source[index]
        if c in delimiters:
            if startIndex != -1:
                valList.append(source[startIndex:index])
                startIndex = -1

            operatorList.append(c)

        elif startIndex == -1:
                startIndex = index

    if startIndex != -1:
        valList.append(source[startIndex:])

    return (valList, operatorList)

print("====== 계산기 ======")
delimiters = {"+", "-", "*", "/", "="}

result = True
while result:
    userInput = input("\n")
    # print(split(userInput, delimiters))
    
    # make sure there is no alphabet
    if userInput.isalpha():
        print(f"Can't calculrate user input.")
        continue

    # remove leading and tailing whitespaces
    userInput.strip() 
    # make sure it has a equal operator
    if userInput[len(userInput) - 1] != "=":
        userInput += "="

    result = split(userInput, delimiters)
    valueList = result[0]
    operatorList = result[1]

    if len(valueList) != len(operatorList):
        print(f"Can't calculrate user input.")
        continue

    if operatorList.count("=") > 1:
        print(f"Can't calculrate user input.")
        continue

    lastValue = -1
    lastOperator = ""
    for index in range(len(valueList)):
        value = int(valueList[index])
        operator = operatorList[index]

        if lastValue == -1 and lastOperator == "":
            lastValue = value
            lastOperator = operator
            continue
   
        match lastOperator:
            case "+":
                lastValue = add(lastValue, value)
            case "-":
                lastValue = subtract(lastValue, value)
        
        lastOperator = operator




    print(f"{userInput} {lastValue}")
        
        
            


