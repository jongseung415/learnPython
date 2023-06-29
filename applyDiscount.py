paiedAmount = int(input())

if paiedAmount > 100000 :
    discount = paiedAmount * 0.05
    sales = paiedAmount - discount
    message = "지불 금액은 " + str(sales)  + "원입니다."
    print(message)
else :
    goalSales = 100000 - paiedAmount

    message = "지불 금액은 " + str(paiedAmount) + "입니다.\n만약 " + str(goalSales) + "원 더 구매하시면 5% 할인 혜택을 받으실 수 있습니다!"
    print(message)
