number = input("숫자를 입력해주세요.")

number.isalnum()

if number.isalnum():
    if number == "1":
        print("하나")
    elif number == "2":
        print("둘")
    elif number == "3":
        print("셋")
    elif number == "4":
        print("넷")
    elif number == "5":
        print("다섯")
    elif number == "6":
        print("여섯")
    elif number == "7":
        print("일곱")
    elif number == "8":
        print("여덟")
    elif number == "9":
        print("아홉")
else:
    print("숫자가 아닙니다. 숫자를 입력해주세요")