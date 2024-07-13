#Запросим строку у пользователя
print ("Enter word")
example = input()

#Выведем первый символ
print(example[0])

#Выведем последний символ
print(example[-1])

#Выведем на экран вторую половину этой строки
length = len(example)
index = length//2
print(example[index:])

#Выведем на экран слово наоборот
print(example[::-1])

#Выведем на экран каждый второй символ
print(example[1::2])