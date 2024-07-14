#Запросим имя пользователя
print("What is your name?")
name = input()

#Выведем имя на экран
print(f' Name: {name}')

#Запросим возраст
print("How old are you?")
age = input()

#Выведем возраст на экран
print(f'Age: {age}')

#А теперь добавим к возрасту пару годиков
age = int(age) + 3

#Вывведем возраст на экран
print(f'New age: {age}')

#Спросим является ли пользователь студентом
def isStudent(is_student):
    if is_student == "yes":
        is_student = True
        return is_student
    elif is_student == "no":
        is_student = False
        return is_student
    else:
        print("Data is not correct! Please, enter 'yes' or 'no'.")
        print("Are you student? y/n")
        is_student = input()
        return isStudent(is_student)
print ("Are you student? y/n")
is_student = input()
is_student = isStudent(is_student)

#Выведем результат на экран
print(f'Is student: {is_student}')


