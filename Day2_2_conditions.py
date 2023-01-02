
userInput = input("1~10 사이에 원하는 수를 입력하시오.")

if userInput[0] == '-':
    if userInput[1:len(userInput)].isnumeric():
        print("음수를 입력했어요")
    else:
        print("숫자를 입력하지 않았어요.")
elif not userInput.isalpha:    
    print("숫자를 입력하지 않았어요.")
elif not 1 <= int(userInput) <= 10:
    print("정해진 범위를 벗어났어요.")
else:
    print(f"입력한 수는 : {userInput} 입니다.")