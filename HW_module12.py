per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = (int(input('введите сумму вклада :')))
b1 = per_cent.get('ТКБ')
b2 = per_cent.get('СКБ')
b3 = per_cent.get('ВТБ')
b4 = per_cent.get('СБЕР')
s1 = round(b1 * money / 100)
s2 = round(b2 * money / 100)
s3 = round(b3 * money / 100)
s4 = round(b4 * money / 100)
deposit = [s1, s2, s3, s4]
print('Накопленные средства за год вклада в каждом из банков', deposit)
print('Максимальная сумма, которую вы можете заработать -', max(deposit))
