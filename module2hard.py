def pasword_guessing(n):
    result = ''
    for i in range(1,n):
        for j in range(i+1,n):
            if (i + j) % n == 0:
                result = result + str(i) + result + str(j)
    return result
number = 0
while number < 3 or number > 20:
    number = int(input("Введите число от 3 до 20: "))
pasword = pasword_guessing(number)
print(f'Пароль для вашего числа {number}: {pasword}')