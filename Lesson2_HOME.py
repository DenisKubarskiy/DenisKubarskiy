# Задачи на циклы и оператор условия------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

# x=input('Введите, сколько нулей должно быть в строке ')
# x=int(x)
# for i in range(1,6):
#     print(i,end=' ')
#     for j in range(1, x+1):
#         print(0,end='')
#     print()

'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''

# amount=0
# for i in range(1,11):
#     print('Введите цифру №',i,': ',end=' ')
#     x=input()
#     x=int(x)
#     if x==5:
#         amount+=1
# print('Количество введенных цифр 5: ',amount)


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)

'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
# proizv=1
# for i in range(1,11):
#     proizv=proizv*i
# print('Произведение ряда чисел от 1 до 10 равно', proizv)


'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

# integer_number = 2129
#
# #print(integer_number%10,integer_number//10)
#
# while integer_number>0:
#     print(integer_number%10)
#     integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''

# x=input('Введите число ')
# x=int(x)
# y=x
# sum=0
# while x>9:
#     sum=sum+x%10
#     x=x//10
# sum=sum+x
# print('Сумма цифр числа ',y,': ',sum)


'''
Задача 7
Найти произведение цифр числа.
'''

# x=input('Введите число ')
# x=int(x)
# y=x
# pr=1
# while x>9:
#     pr=pr*(x%10)
#     x=x//10
# pr=pr*x
# print('Произведение цифр числа ',y,': ',pr)

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
# integer_number = 213413
# while integer_number > 0:
#     if integer_number % 10 == 5:
#         print('Yes')
#         break
#     integer_number = integer_number // 10
# else:
#     print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''

# x=input('Введите число ')
# x=int(x)
# y=x
# max=0
# while x>9:
#     if max<x%10:
#         max=x%10
#     x=x//10
# if max<x:
#     max=x
# print('Максимальная цифра в числе ',y,': ',max)


'''
Задача   10
Найти количество цифр 5 в числе
'''

# x=input('Введите число ')
# x=int(x)
# y=x
# count=0
# while x>9:
#     if x%10==5:
#         count=count+1
#     x = x // 10
# if x==5:
#     count = count + 1
# print('Количество цифр 5 в числе ',y,': ',count)

number = int(input("введите цифру "))
digits_numbar = int(input("что ищем"))
count = 0
while number>0:
 if number%10 == digits_numbar:
    count += 1
 number=number//10
print(count)