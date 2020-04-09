from functools import reduce
import random

# import copy
# 
# sample=[1,2,3,4,5]
# summ=reduce(lambda x,y:x+y, sample)
# max=reduce(lambda x,y: x if x>y else y, sample)
# print(summ, max)

# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка 
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

list1=['Михаил',"Анна", "Елена", 'Светлана', "Константин", "Наталья", 'Лизавета', "Денис", "Дмитрий", "Павел", "Жанна", "Мария", "Владимир", "Петр", "Зоя", "Леонид", "Александр", "Дональд", "Кристина", "Яна" ]
n1=int(input("Введите нужную длину списка не более 100 "))

def name_list_gen(new_list, n):
    new_list1 = []
    for i in range(n):
        x = random.randint(0, len(new_list)-1)
        new_list1.append(new_list[x])
    return  new_list1

def Most_frequent (new_list):
    count_word={}
    for w in new_list:
        count_word[w]=0
    for w in new_list:
        count_word[w]+=1
    print(count_word)
    sorted_count_word=dict(sorted(count_word.items(),key=lambda y:y[1], reverse=True))
    print(sorted_count_word)
    print(type(sorted_count_word), list(sorted_count_word.keys())[0])
    return list(sorted_count_word.keys())[0]

def Most_freq_Letter (new_list):
    first_letters_list=[]
    for i in new_list:
        word_list=list(tuple(i))
        # print(type(word_list),word_list)
        first_letters_list.append(word_list[0])
    print(first_letters_list, end=' ')
    count_Letter={}
    for w in first_letters_list:
        count_Letter[w]=0
    for w in first_letters_list:
        count_Letter[w]+=1
    sorted_letters=dict(sorted(count_Letter.items(),key=lambda y:y[1]))
    print(sorted_letters)
    print(list(sorted_letters.keys())[0])
    return list(sorted_letters.keys())[0]


new_list=name_list_gen(list1,n1)
print('Список имен: ', new_list)
Most_freq_name=Most_frequent(new_list)
print('Чаще встречается имя ', Most_freq_name)
Most_freq_Letter1=Most_freq_Letter(new_list)
print('Реже всего имена начинаются на букву  ', Most_freq_Letter1)



# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.



