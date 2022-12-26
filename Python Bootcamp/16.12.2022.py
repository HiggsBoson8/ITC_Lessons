# GITHUB
# ---------------------------------------------------------------------------------------------------------

# Если хотим запушить все на новую репозиторию 
# rm -rf                                    = Удаляем папку .git которая уже связано к старой репозитории
# git init                                  = инитцализирует и создает папку .git
# git remote add origin (shh репозитория)   = Копируем ssh нашего репозирия и вставляем
# git add .                                 = Выделяем все наши файлы
# git commit -m "all"                       = Коментим репозиторию
# git push -u origin master                 = Пушим все в ветку мастер

# ---------------------------------------------------------------------------------------------------------

# Если хотим отправить на тот же репозитории тогда не удаляем папку .git
# git add .                                 = Выделяем все наши файлы
# git commit -m "all"                       = Коментим репозиторию
# git push -u origin master                 = Пушим все в ветку мастер

# ---------------------------------------------------------------------------------------------------------
# OPEN and WITH

# Режим  Описание
# r      = Только для чтения.
# r+  = Для чтения и записи.
# w+  = Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# w      = Только для записи. 
# Создаст новый файл, если не найдет с указанным именем.
# 
# a      = Откроет для добавления нового содержимого.
# Создаст новый файл для записи, если не найдет с указанным именем.

# a+  = Откроет для добавления нового содержимого.
# Создаст новый файл для чтения записи, если не найдет с указанным именем.


# f = open('ITCBootcamp.txt','r')
# # a= f.read(4)
# b = f.readLine() #Прочитать указанную
# c = f.readLines() #Прочитать файл полностью
# print(c)
# f.close()

# a = open()
# a.write()
# a.close()
# with open() as f:
#     f.write()



# login = input('Введите свой логин: ')
# password = input('Введите свой пароль: ')
# with open('users.txt','a+') as f:
#     f.write(f'Логин: {login}, Пароль: {password}')
#     a = f.readline()
#     for i in a:
#         if i == 'w':
#             print('Да') 
#         else: 
#             print('Нет')


# 4) Создайте текстовый файл python.txt и запишите в него текст #1 из Classroom: Затем, считайте его. Пробежитесь по всем его словам, и если слово содержит букву “t” или “T”, 
# то запишите его в список t_words = [ ]. После окончания списка, выведите на экран все полученные слова. Подсказка: используйте for.
t_work = []
with open('python.txt', 'w') as f:
    f.write('''
            qwertyuiop[asdfghjkl;'zxcvbnm,. asdfghjkl;'zxcvbnm,./
            zxcvbnm,asdfghjkl;qwertyuiopthjkl;tyuiopdfghjk]
            ''')
with open('python.txt', 'r') as a:
    text = a.read()
    for i in text.split():
        for j in i:
            if j == 't' or j == 'T':
                t_work.append(i)
print('t_work')

# 5) Создайте database.txt файл с несколькими логинами и паролями. Затем попросите пользователя войти или зарегистрироваться. Спросите его логин и пароль. 
# Если такой логин уже есть скажите ему что логин уже существует и предложите авторизоваться спросив пароль. Если такого логина неоказалось среди уже существющих продолжайте регистрацию. 
# Спросите у него Пароль 2 раза и сохраните в в файл datebase.txt только если пароли совпадают.

# l = input()
# p = input()

# with open('db.txt', 'a+') as f:
#     f.write(f'{l}, {p}')
    
# with open('db.txt', 'r') as r:
#     lp = r.readlines()
#     print(lp)
    
# while True:
#     table = input('''
#                   1 registration
#                   2 authorisation
#                   ''')
#     if table == '1':
#         login = input()
#         password = input()
#         password2 = input()
#         while password != password2:
#             password = input()
#             password2 = input()
#         else:
#             with open('db.txt', 'r') as f:
#                 db = f.readlines()
#                 for i in db:
#                     if i == f'{login}, {password}':
#                         print('Такой пользователь уже есть')
#                     else:
#                         for i in range(1):
#                             with open('db.txt', 'a+') as new_db:
#                                 new_db.txt.write(f'{login}, {password}')
#                             print('Вы успешно зарегистрированы')

# 6) Создайте форму регистрации которая спрашивает у пользователя: Логин, Пароль и Фото. Заранее подготовьте фото на компьютере и когда программа спросит ваше фото просто 
# укажите полный путь до места где лежит ваше фото. Программа должна проверить если фото правда существует по такому пути И также это фото с одним из 3 расширений("jpeg", "jpg", "png") 
# то вы сохраняете в файл логин, пароль, путь до фото которое указал пользователь. А самому пользователю вы говорите о том что Регистрация Успешна!

login = input('Введите логин: ')
password = input('Введите пароль: ')
photo = input('Введите путь до фотографии: ')

        
# 7) 

