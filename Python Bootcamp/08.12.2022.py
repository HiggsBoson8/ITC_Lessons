# str - string - не изменяемый тип данных
# peremen = input('Put the name: ')

# print(peremen.title()) # Все начальные буквы в верхнем регистре
# print(peremen.upper()) # Все буквы в верхнем регистре 
# print(peremen.lower()) # Все буквы в нижний регистр
# print(peremen.swapcase()) # Все большие в маленький и маленькие в большие буквы
# print(peremen.capitalize()) # Начальную букву в верхний регистр

# a = 'StarDust'
# print(a.isdigit()) #Все ли состоит из цифр
# print(a.isalpha()) #Все ли состоит из букв 
# print(a.isidentifier()) #Все ли у нас слитно 
# print(a.islower()) #Все ли у нас в нижнем регистре
# print(a.isupper()) #Все ли у нас в верхнем регистре
# print(a.istitle()) #Все ли у нас начинаются с большой буквы
# print(a.isnumeric()) #Все ли у нас состоит из цифр
# print(a.isspace()) #Все ли у нас в пробелах
# print(a.isprintable()) #Все ли можем спринтовать

# text = 'Я играю на гитаре'
# print(text.strip('Я')) #Удаление начальной буквы
# print(text.rstrip('е')) #Удаление последнюю букву
# print(text.lstrip('Я')) #Удаление начальной буквы

# text = 'Abay'
# # print(text.center(6, '*')) #Выравнивание строк
# # print(text.rjust(6, '*')) #Выравнивание строк справа
# # print(text.ljust(6,'*')) #Выравнивание строк слева
# # print(text.zfill(100)) #Дополнение текста на 0

# print(f"asdfg{text}")
# print("marselle {0} name: {1}".format ('Marselle', 'hello'))

# text = 'гитарист'
# if text == text.isdigit():
#     print('true')
# else:
#     print('false')

# if text == text.isalpha():
#     print('false')
# else:
#     print('true')

# text = 'python, golang, java' 
# print(text.replace('java', 'csharp')) #замена одного текста на другой текст
# print(text.find('o')) #показать индекс буквы
# print(text.find('o', 3)) #показать индекс буквы после 3 индекса
# print(text.index('g', 4))
# print('*'.join(text)) #вернуть текст после каждой буквы *

# text = 'Hello, world'
# print(text.count('o'))#сколько в тексте букв о(2)
# print(text.count('o', 5))#сколько в тексте букв о после 5 индекса(1)

# print(text.split()) #разделит наш текст и обернет в массив
# print(text.splitlines()) #весь текст обернуть в массив
# print(text.partition('H')) #разделить букву 'H' от строки

# print(text.startswitch('H')) #Начинается ли наш текст с буквы H
# print(text.endswitch('d')) #заканчивается ли наш текст с буквы d

# print(len(text)) #подсчитать весь в тексте

# text = 'Hello'
# print(text[1:3]) #срез текста

# создать предложение где одна его половина написана в маленьком регистре, а вторая в полностью в большом
# a = 'HelloWorld'
# print(a[5:].lower(), a[5:].upper())

# p1 = int(input('Введите пароль: '))
# p2 = int(input('Повторите пароль: '))

# if p1 == p2:
#     if len(p2) >= 8:
#         print('Пропускаем') 
#         if '123' not in p2:
#             password = p2
#             print('|*|'.join(password))
#             print(p2)
#         else:
#             print('Ваш пароль слишком простой')
#     else:
#         print('Ваш пароль должен быть больше 8 символов')
# else:
#     print('У вас не совпадает пароль.')

# Спросить у пользователя имя, возраст и любимый фильм
# print('Greetings!')
# a = input('Введите свое имя: ')
# b = input('Введите свой возраст: ')
# c = input('Назовите ваш фильм: ')
# # print('Greetings ' + a + '! ' + 'Nice to meet you! ' + 'Your age is ' + b + '. Your movie ' + c + ' is nice!')
# print(f"Greetings {a} ! Nice to meet you! Your age is {b} . Your movie {c} is nice!")

#  спросить имя у пользователя и после каждого символа проставить '|'
# text = input("Type your name: ")
# print('|'.join(text))

# взять строку и заменить все буквы на ч на число 4
# space = 'ч ч ч ч'
# print(space.replace('ч', '4'))


# login должен быть в нижнем регистре и на английском языке,в нем не должны быть символы %:?*()
# password должен быть > 8 символов и в пароле должны быть цифры, буквы на английском и символы.

# a = input('Login: ')
# b = input('Password: ')
