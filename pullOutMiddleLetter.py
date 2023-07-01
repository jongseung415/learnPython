targetString = input()

targetStringLength = len(targetString)

if targetStringLength % 2 == 0 :
    i = targetStringLength // 2
    print("중앙글자는 " + targetString[i-1]+targetString[i])
else :
    i = targetStringLength // 2
    print("중앙글자는 " + targetString[i])
