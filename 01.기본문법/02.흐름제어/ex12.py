# 남탕 여탕 갈지 선택 -> 남여 성별 선택 -> 나이 제한     #CONTROL + C = 재생 강제종료
#1.남탕에 대한 조건: 남자이거나 여자이면서 나이가 4세미만
#2.여탕에 대한 조거: 여자이거나 남자이면서 나이가 4세미만 
while True:
    type = input("1.남탕|2.여탕|0.종료>")
    if type == "0":
        print("프로그램을 종료합니다.")
        break
    elif type=="1" or type=="2":
        gender = input("1.남자|2.여자>")
        if type =="1": #남탕
            if gender =="1": #남자
                print("남자이므로 남탕입장이 가능합니다.")
            else:#여자
                age = int(input("나이>"))
                if age < 4:
                    print("여자지만 4세미만으로 남탕에 입장이 가능합니다.")

                else:
                    print("여자이고 4세이상이므로 남탕에 입장이 불가능합니다.")
        if type =="2":
            if gender =="2":
                print("여자이므로 여탕입장이 가능합니다.")
            else:#남자
                age = int(input("나이>"))
                if age < 3:
                    print("남자지만 3세미만으로 남탕에 입장이 가능합니다.")
                else:
                    print("남자이고 3세이상이므로 여탕에 입장이 불가능합니다.")

