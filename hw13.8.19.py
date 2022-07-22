cost = 0
bilets = int(input('Введите количесто билетов для покупки - '))
for i in range (bilets):
    age = int(input('Введите возраст посетителей - '))
    if 18 <= age <= 24:
        cost += 990
    elif age >= 25:
        cost += 1390
    else:
        cost += 0
if bilets > 3:
    cost *= 0.9
    print ('Сумма к оплате c учётом скидки 10%:', cost)
else:
    print('Сумма к оплате:', cost)