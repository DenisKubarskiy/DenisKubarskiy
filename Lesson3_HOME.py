
# 0. Чтение содержимого файла в переменную text
#  f = open('text.txt', 'r')
f = open(r'i:\PYTHON\Обучение\Lesson3\text.txt', 'r')
text=f.read()
f.close()
# print(type(text),text)

# 1. Методами строк очистить текст от знаков препинания

znaki=',?!—;:".«»()\r\t'
for i in range(len(znaki)):
      text=text.replace(znaki[i],'')
print(text)
