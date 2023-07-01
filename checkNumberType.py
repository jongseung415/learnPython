integer = int(input("정수를 입력하시오: "))
#
# if integer > 0 :
#     print("입력한 정수는 양수입니다.")
# elif integer < 0 :
#     print("입력한 정수는 음수입니다.")
# else :
#     print("입력한 정수는 0입니다.")

if integer >= 0 :
    if integer == 0 :
        print("입력된 정수는 0입니다.")
    else :
        print("입력된 정수는 양수입니다.")
else :
    print("입력된 정수는 음수입니다.")