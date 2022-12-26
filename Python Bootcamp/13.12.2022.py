# loop for
# int not iter object if i<100 print i

# int = 65
# for i in range(50, 101, 5):
#     print(i)
    
# list = [1, 2, 3, 4, 5]    
# dict1 = { 
#         'name':'Admin', 
#         'post':'superuser',
#         'id':'1'
#          } 
# for i in dict1.items():
#     print(i) 
    
# i = 1000
# while i > 1: #условие
#     i -= 100 #-= i - 100; i += i + 5
#     print('error')

# i = 1000
# while i >= 0:
#     print('Hello')
#     print(i)
    
# list1 = [1,2,3,4,5,6,7,8,9,10]
# for i in list1:
#     if i%2==1:
#       print(i)

# list1 = [1,2,3,4,5,6,7,8,9,10]
# list2 = []
# list3 = []
# for i in list1:
#     if i%2==0:
#         list2.append(i)
#     else: 
#         list3.append(i)
# print(list2)        
# print(list3)

# i = 10
# while i != 0:
#     i =+ 1 
#     print(i)
#     if i == 5:
#         break 

# list6 = [1,2,3,4,5,6,7,8,9]
# for item in list6:
#     if item == 7:
#         break
#     print(item)

# list6 = ['hi', 'my', 'name', 'si', 'nein']
# for item in list6:
#     print(item, end = '/') #\n
    
# for i in range(5):
#     print('*', end = '\n')
#     for j in range(4):
#         print('*', end ='')
#         for k in range(3):
#             print('*', end = '')
#             for q in range(2):
#                 print('*', end = '')
#                 for l in range(1):
#                     print('*', end = '')                


#1)add new fruits 2)show new fruits
# a = 1
# while a > 0:
#     list1 = ['apple', 'banana', 'cherry'] 
#     list1.append('orange')
#     list1.append('pineapple')
#     a -= 1
#     print(list1)


# 2) astronaut 1000-7 print('space') 0 > loop print('quantum)

# a = 1000
# while True:
#     print('space')
#     a -= 7
#     if a <= 0:
#         print('quantum')
#         break


# 3) print 'hello, Python' with while

# a = 3
# while a > 0:
#     print('Hello, Python')
#     a -= 1
# print('Hello Java')
    
    
# 4) calc with while

# while True:
#     operator = input('Enter the operator (+ - / *): ')
#     number1 = float(input('Enter the first numer: '))
#     number2 = float(input('Enter the second number: '))

#     if operator == '+':
#         result = number1 + number2
#         print(result)
#     elif operator == '-':
#         result = number1 - number2
#         print(result)
#     elif operator == '/':
#         result = number1 / number2
#         print(result)
#     elif operator == '*':
#         result = number1 * number2
#         print(result)
#     else:
#         ('error')
#     astronaut = input('Would you want to continue? Yes/No: ')
#     if astronaut == 'Yes':
#         print()
#     elif astronaut == 'No':
#         print('Closing calculator.')
#         break
#     else:
#         print('error')

# 5) треугольник с помощью цикла

# a = 1
# while a > 0:
#     for i in range(1, 10):
#         print('#' * i)
#     break 
    
# 6) clear text "heLlOMyNAmEisShELby" all letter lower

# astronaut = 'heLlOMyNAmEisShELby'
# quantum = []

# for i in astronaut:
#     if i.isupper():
#         print(astronaut.replace(i, ''))
# print(astronaut.lower())


# АВТОРИЗАЦИЯ 

# user = {
#     'Astronaut': {
#         'phone' : '87087617161',
#         'name' : 'Abay',
#         'balance' : 100000,
#         'password' : 'astronaut'
#     },
#     'Random': {
#         'phone' : '87017757575',
#         'name' : 'Random',
#         'balance' : 50000,
#         'password' : 'random'
#     },
# }

# key = None
# while True:
#     table = int(input("""
#         1 >>> Зарегистрироваться
#         2 >>> Авторизоваться
#         3 >>> Перевод баланса
#         4 >>> Список пользователей
#         5 >>> Информация
#         6 >>> Номер телефона   
#         7 >>> Выйти 
#         """))
    
#     if table == 1:
#         if key in None:
#             login = input('Пожалуйста, введите логин: ')
#             if login.isalpha():
#                 name = input('Пожалуйста, введите имя: ')
#                 if name.alpha():
#                     phone = input('Пожалуйста, введите номер телефона: ')
#                     if phone.isdigit():
#                         password1 = input('Создайте пароль: ')
#                         password2 = input('Повторите пароль: ')
#                         while password != password2:
#                             password = input('Создайте пароль не меньше 8ми символов: ')
#                             password1 = input('Повторите свой пароль: ')
#                         else:
#                             user.update({
#                                 login: {
#                                     'name': name,
#                                     'phone': phone,
#                                     'balance': 100,
#                                     'password': password2,
#                                 }
#                             })
#                     else:
#                         print('Номер должен состоят только из цифр')
#                 else:
#                     print('Имя должен быть только из букв')
#             else:
#                 print('Логин должен быть только из букв')
#         else:
#             print('Вы уже зарегистрированы')
            
#     elif table == 2:
#         if key is None:
#             login = input('Введите логин: ')
#             if login in user.keys():
#                 password = input('Введите пароль: ')
#                 if password == user [login]['password']:
#                     print('Вы авторизованы')
#                     key = login
#                 else:
#                     print('У вас пароль неправильный')
#             else:
#                 print('В базе нет такого пользователя')
#         else:
#             print('Вы уже авторитзованы')
            
#     elif table == 3:
#         if key is not None:
#             login_komu = input('Введите логин получателя: ')
#             if login_komu.isalpha() and login_komu in user.keys():
#                 summa = int(input('Введите сумму перевода: '))
#                 if summa <= user[login]['balance']:
#                     user[login]['balance'] -= summa
#                     user[login_komu] += summa
#                     print('Отправлено')
#                 else: 
#                     print('У вас не хватает денег для перевода')
#             else:
#                 print('Не верно указали логин или нет такого пользователя')
#         else:
#             print('Сначала авторизуйтесь')
    
#     elif table == 4:
#         if key is not None:
#             print(user)
#         else:
#             print('Сначала авторизуйтесь')
    
#     elif table == 5:
#         if key is not None:
#             print(f'''
#             Ваши данные:
            
#             login: {key}
#             name: {user[login]['balance']} 
#             balance: {user[login]['balance']}
#             password: {user[login['password']]}  
#                   ''')
#         else:
#             print('Сначала авторизуйтесь')
            
#     elif table == 6:
#         if key is not None:
#             print(f"phone number: +7{user[login]['phone']}")
#         else:
#             print('Сначала авторизуйтесь')
            
#     elif table == 7:
#         key = None
#         print('Вы вышли из аккаунта')



# д/з: сделать ромб с помощью циклов

# for i in range(1, 10, 2):
#     print('*' * i)
# for i in range(11,0, -2):
#     print('*' * i)
# for i in range(-10, 0, 2):
#     print('*' * i)
# for i in range(0, -10, -2):
#     print('*' * i)

# д/з: ромб с цифрами
# n = int(input()) 
# x = ""
# for i in range(1, n + 1): 
#     x = x + str(i)
#     print(' '*(n-i) + x + x[-2::-1])
# for i in range(n-1, 0, -1):
#     print(' '*(n-i), sep='', end='')
#     for k in range(1, i + 1):
#         print(k, end='')
#     print()
    

# a = 8
# b = '*'
# c = a * len(b) * 2
# for i in range(1, a * 2 + 1, 2):
#     print(f'{b * i}'.center(c))
# for i in range(a * 2 - 3, 0, -2):
#     print(f'{b * i}'.center(c))

# n = 8 
# z = '*'
# a = n * len(z) * 2
# for i in range(1, n * 2 + 1, 2):
#     print(f'{z * i}'.center(a))
# for i in range(n * 2 - 3, 0, -2):
#     print(f'{z * i}'.center(a))
    
    