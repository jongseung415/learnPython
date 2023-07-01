workedTime = int(input("근무시간을 입력하시오:"))

wageAtTime = int(input("시간당 임금을 입력하시오:"))

if workedTime < 40 :
    totalWage = workedTime * wageAtTime
    
    message = "총임금은 " + str(totalWage)
    print(message)
else :
    workedOverTime = workedTime - 40
    overTimeWage = wageAtTime * 1.5

    totalWage = 40 * wageAtTime + workedOverTime * overTimeWage

    message = "총임금은 " + str(totalWage)
    print(message)
