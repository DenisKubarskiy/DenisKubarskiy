
# 0. Чтение содержимого файла в переменную text
# f = open('text.txt', 'r')
f = open(r'i:\PYTHON\Обучение\Study\Lesson3\text.txt', 'r')
text=f.read()
f.close()
# print(type(text),text)

# 1. Методами строк очистить текст от знаков препинания

znaki=',?!—;:".«»()\r\t\f\v\''
for i in range(len(znaki)):
      text=text.replace(znaki[i],'')
text=text.replace('\n',' ')   # удаление перехода на новый абзац
text=text.replace('  ',' ')   # удаление двойного пробела
print('Текст: ',text)

# 2 Cформировать list со словами (split)

wordlist=text.split(' ')
print('Список слов: ', wordlist)

# 3 Привести все слова к нижнему регистру (map)

L_wordlist = list(map(lambda x: x.lower(), wordlist))
print('Список слов в нижнем регистре: ', L_wordlist)

# 4 Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

Dic_text=dict.fromkeys(L_wordlist,0)
for i in L_wordlist:
      Dic_text[i]+=1
print('Словарь слов: ', Dic_text)

# 5 вывести 5 наиболее часто встречающихся слов (sort)
#   вывести количество разных слов в тексте (set)

Dict_list=list(Dic_text.values())
print('Сколько раз встречается слово: ',Dict_list)
Dict_list.sort(reverse=True)
print('Сколько раз встречается слово - по убыванию: ',Dict_list)
Dict_list=Dict_list[:5]
# print('5 наиболее часто встречающихся слов: ',Dict_list)
print('5 наиболее часто встречающихся слов: ', end=' ')
for key,value in Dic_text.items():
      if value in Dict_list:
            print(key, end=' ')

amount=set(L_wordlist)
print()
print('Всего слов: ',len(L_wordlist)) #Всего слов
print('Всего разных слов: ',len(amount))     #количество разных слов в тексте