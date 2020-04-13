# LIGHT:
# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
# 2) выводит список всех делителей числа;
# 3) выводит самый большой простой делитель числа.
# PRO:
# LIGHT +
# 4) функция выводит каноническое разложение числа (https://zaochnik.com/spravochnik/matematika/delimost/razlozhenie-chisel-na-prostye-mnozhiteli/) на простые множители;
# 5)функция выводит самый большой делитель (не обязательно простой) числа.

def simple (n):
    k=0
    for i in range (2, n):
        if n%i!=0: k+=1
    if k==n-2: print('Число ', n, '- простое')
    else: print('Число ', n, '- составное')
# m=int(input('Введите число '))
# simple(m)

def deliteli (n):
    print('делители числа ', n, ' : 1,', end="")
    for i in range (2, n):
        if n%i==0: print(i,end=",")
    print(n)
# m=int(input('Введите число '))
# deliteli(m)

def biggest_simple_delitel (n):
    for i in range (n-1, 0,-1):
        if n%i==0:
            k=0
            for j in range(2,i):
                if i % j != 0: k+=1
            if k == i - 2:
                print('Число ', i, '- наибольший простой делитель числа ', n)
                break
    if i==1: print('Число ', n, ' простое, поэтому его делители только 1 и само число')
# m=int(input('Введите число '))
# biggest_simple_delitel(m)

def biggest_delitel (n):
    for i in range (n-1, 0,-1):
        if n%i==0 and i!=1:
            print('Число ', i, '- наибольший делитель числа ', n)
            break
    if i==1: print('Число ', n, ' простое, поэтому его делители только 1 и само число')
# m=int(input('Введите число '))
# biggest_delitel(m)

n=int(input('Введите число от 1 до 1000 '))
deliteli=[]
print("Каноническое разложение числа ", n, "= ",end='')
k=0
while n!=1:
    for i in range(2, n+1):
        if n % i == 0:
            deliteli.append(i)
            k+=1
            if n / i==1:
                if k==1:
                    print(n,' (Число ', n, ' простое, поэтому его делители только 1 и само число)')
                else: print(i, end=' ')
            else:print(i, end='*')
            break
    n=int(n/i)
print()
deliteli_1 = {}
for w in deliteli:
    deliteli_1[w] = 0
for w in deliteli:
    deliteli_1[w] += 1
k1=0
for w in deliteli:
    if deliteli_1[w] > 1:
        k1+=1
k3=len(deliteli_1)
if k1>0:
    print('или ', end=" ")
    k2=0
    for key in deliteli_1:
        if k2<k3-1:
            if deliteli_1[key]==1:
                print(key,"*",end=" ")
            else: print(key,"^",deliteli_1[key], "*",end=" ")
        else:
            if deliteli_1[key]==1:
                print(key)
            else: print(key,"^",deliteli_1[key],end=" ")
        k2 += 1