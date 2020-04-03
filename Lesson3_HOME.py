
# 0. Чтение содержимого файла в переменную text
#  f = open('text.txt', 'r')
f = open(r'i:\PYTHON\Обучение\Lesson3\text.txt', 'r')
text=f.read()
f.close()
# print(type(text),text)

# 1. Методами строк очистить текст от знаков препинания

znaki=',?!—;:".«»()\r\t\''
for i in range(len(znaki)):
      text=text.replace(znaki[i],'')
text=text.replace('\n',' ')
print(text)

# 2 Cформировать list со словами (split)

wordlist=text.split(' ')
print(wordlist)

# 3 Привести все слова к нижнему регистру (map)

L_wordlist = list(map(lambda x: x.lower(), wordlist))
print(L_wordlist)

# 4 Получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте

Dic_text={}
for i in range(len(L_wordlist)):
      Dic_text=Dic_text.fromkeys=(L_wordlist[i],0)
print(Dic_text.keys())


