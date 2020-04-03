
# 0. Чтение содержимого файла в переменную text
#  f = open('text.txt', 'r')
f = open(r'i:\PYTHON\Обучение\Lesson3\text.txt', 'r')
text=f.read()
f.close()
# print(type(text),text)

# 1. Методами строк очистить текст от знаков препинания
text = text.replace(',', '')
text = text.replace('?', '')
text = text.replace('!', '')
text = text.replace('—', '')
text = text.replace(';', '')
text = text.replace('.', '')
text = text.replace('«', '')
text = text.replace('»', '')
text = text.replace('\r', ' ')
text = text.replace('\f', ' ')
text = text.replace('\t', ' ')
# text = text.replace('\n', ' ')
# print(text)
