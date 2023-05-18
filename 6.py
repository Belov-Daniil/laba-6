from itertools import *


fruits = ['Груша', 'Банан', 'Яблоко', 'Персик', 
          'Манго', 'Гранат', 'Апельсин']


days = ['Понедельник', 'Вторник', 'Среда',
        'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


fruits_list = list(permutations(fruits, days.__len__()))
days_list = list(permutations(days, days.__len__()))


counter = 0
for i in range(0, len(fruits_list)):
        for j in range(0 , 6):
                print(fruits_list[i][j] + " - " + days_list[i][j])
        counter += 1
        print('\n')

print(counter)
    