def password(number):
    code = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                code += str(i) + str(j)
    return code

print('Введите число: ')
print('Ваш шифр:', password(int(input())))