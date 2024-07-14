immutable_var = 1, True, 'three', [1, 'a', False], 1.7
print("Immutable tuple:", immutable_var)
#Тут чуть-чуть странный блок с объяснениями, почему нельзя менять данные в кортеже
#immutable_var[0] = "Хочу стать первым элементом кортежа"
#Потому что кортеж - это неизменяемый тип данных
#А вот со списком можно поиграться чуть-чуть
count = int(input('Введите количество объектов в списке: '))
mutable_list = []
for i in range(count):
    print("Введите элемент списка", i+1)
    mutable_list.append(input())
print(mutable_list)
#Изменение элементов списка
def editList (list_1: list):
    index = int(input("Введите номер элемента на замену: "))
    if index - 1 > len(list_1) or index < 0:
        print("Указанный номер не входит в текущий список!")
        return list_1
    elif index == 0:
        list_1[index] = input("Введите новый элемент списка: ")
        answer = input("Требуется изменить еще элемент списка? ")
        list_1 = answerAnalisis(answer, list_1)
        return list_1
    else:
        list_1[index-1] = input("Введите новый элемент списка: ")
        answer = input("Требуется изменить еще элемент списка? ")
        list_1 = answerAnalisis(answer, list_1)
        return list_1

#Для анализа ответа пользователя
def answerAnalisis (answer: str, list_1: list):
    if answer == "yes":
        list_1 = editList(list_1)
        return list_1
    elif answer == "no":
        return list_1
    else:
        print("Вводимые данные некорректны. Пожалуйста используйте ответ 'yes' или 'no'")
        answer = input("Требуется изменить еще элемент списка? ")
        list_1 = answerAnalisis(answer, list_1)
        return list_1
mutable_list = editList(mutable_list)
print("Mutable list:", mutable_list)