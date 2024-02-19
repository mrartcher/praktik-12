a = []
flag = 0

k = float(input('Введіть контрольний результат '))

n = int(input('Введіть кількість результатів випробувань '))
for i in range(n):
    result = float(input(f'Введіть результат {i + 1} спроби: '))
    a.append(result)


for i in range(n):
  if a[i] == k:
    flag = i + 1
    break

if flag != 0:
    print(f'Перша спроба з однаковим результатом - спроба №{flag}')
else:
    print('Жодна спроба не має такого самого результату як контрольний')
