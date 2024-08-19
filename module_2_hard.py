def stone_trap(n):
    password = list()
    for i in range (1,n):
        for j in range (i+1,n):
            if n % (i + j) == 0:
                an = str(i) + str(j)
                password.append(an)
    return password

n = int(input('Ввод числа с 3 до 20:'))
while (n < 3 or n > 20):
    n = int(input('Ввести число с 3 до 20 :'))

result = str()
baseresult = stone_trap(n)
for i in range(len(baseresult)):
    result += baseresult[i]
print('Пароль для второго камня:', result)
