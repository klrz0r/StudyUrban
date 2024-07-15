import random

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
length_grades = len(grades)
list_students = list(students)
length_students = len(list_students)
list_students.sort()
new_dict = {}
def avargeScore(a: list):
    len_a = len(a)
    avarge_score = sum(a)/len_a
    return avarge_score
# И зачем тут это топорное условие?
if length_grades > length_students:
    length = length_students
elif length_grades < length_students:
    length = length_grades
else:
    length = length_grades

for index in range(length):
    new_dict[list_students[index]] = avargeScore(grades[index])
print(new_dict)
print('Дальше можно не смотреть')
# Может придумать что-нибудь поинтереснее?
# Может стоит добавить предмет?
areas = ['Math', 'Geometry', 'Physics']
new_areas = {}
students_reting = {}
students_avarge_score = {}
for area in areas:
    for student in students:
        rating_list = []
        for index in range(5):
            rating_list.append(random.randint(2, 5))
        students_reting[student] = rating_list
        students_avarge_score[student] = avargeScore(rating_list)
    print(area, students_reting)
    new_areas[area] = students_avarge_score
print(new_areas)