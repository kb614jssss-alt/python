#숫자가 입력될때까지 계속 입력하는 함수
def inputNum(title):
    while True:
        num = input(f"{title}>")
        if num.isnumeric():
            return int(num)
        elif num == "":
            return num        
        else:
            print("숫자로 입력하세요!")
        

num = inputNum("숫자입력")
print(num, type(num))