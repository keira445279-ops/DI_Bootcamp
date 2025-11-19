import string
 
# исходная строка
s = "Привет, мир! Это - тестовая строка. Как дела?"
 
# создание таблицы перевода символов
table = str.maketrans("", "", string.punctuation)
 
# применение таблицы к строке
new_s = s.translate(table)

print(new_s)