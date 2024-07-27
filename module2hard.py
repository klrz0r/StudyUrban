def search_password ():
    a = int(input('введите число '))
    password = ''
    for i in range(1, a):
        for n in range(1, a):
            if a % (i + n) == 0 and i < n:
                password = password + str(i) + str(n)
    return password

while True:
    password = search_password()
    print (password)
    answer = input('Подобрать новый пароль? y/n ')
    if answer == 'n' or answer == 'no':
        break