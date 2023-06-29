weightOverCharge = 20000
countOverCharge = 30000
count = int(input("짐의 개수는 몇개입니까?"))
weight = int(input("짐의 무게는 얼마입니까?"))
price = weightOverCharge + countOverCharge

if count >= 2 :
 if weight > 20 :
    print("2개 이상의 짐과 무거운 짐은 %s원을 내셔야 합니다." % price)
 else :
    print("짐이 2개 이상이므로 %s원을 내셔야 합니다." % countOverCharge)
else :
 if weight > 20 :
   print("무거운 짐은 %s원을 내셔야 합니다." % weightOverCharge)
 else :
   print("짐에 대한 수수료는 없습니다.")
print("감사합니다")
