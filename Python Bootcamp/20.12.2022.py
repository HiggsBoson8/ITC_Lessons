# while True:
#     a = input('Enter: ')
#     if a == '1':
#         try:
#             print('123')
#         except:
#             print('error')
            
            


# print(''' Welcome to the game! ''')
# player1 = int(input('1: Rock \U000F270A \n2: Paper \U0001F91A \n3: Scissors \U000F270C \nPlease select: '))
# player2 = int(input('1: Rock \U000F270A \n2: Paper \U0001F91A \n3: Scissors \U000F270C \nPlease select: '))

# if player1 == player2:
#     print('Tie')
# elif player1 == 1 and player2 == 2:
#     print ('Player 2 win')
# elif player1 == 1 and player2 == 3:
#     print ('Player 1 win')
# elif player1 == 2 and player2 == 1:
#     print ('Player 1 win')
# elif player1 == 2 and player2 == 3:
#     print ('Player 2 win')
# elif player1 == 3 and player2 == 1:
#     print ('Player 2 win')
# elif player1 == 3 and player2 == 2:
#     print ('Player 1 win')
# else:
#     print()



# HAHATON ------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 'Задание №1':

# while True:
#     hahaton = open('hahaton.txt', 'a+')
#     operator = input('Марсель сделал запрос на: (+ - / * % **): ')
#     num1 = float(input('Enter the first number: '))
#     num2 = float(input('Enter the second number: '))
#     if operator == '+':
#         result = num1 + num2
#         hahaton.write(f' \nПользователь запросил: {num1} + {num2} = {result} ')
#         print(f'{num1} + {num2} = {result}')
#     elif operator == '-':
#         result = num1 - num2
#         hahaton.write(f' \nПользователь запросил: {num1} - {num2} = {result} ')
#         print(f'{num1} - {num2} = {result}')
#     elif operator == '/':
#         result = num1 / num2
#         hahaton.write(f' \nПользователь запросил: {num1} / {num2} = {result} ')
#         print(f'{num1} / {num2} = {result}')
#     elif operator == '*':
#         result = num1 * num2
#         hahaton.write(f' \nПользователь запросил: {num1} * {num2} = {result} ')
#         print(f'{num1} * {num2} = {result}')
#     elif operator == '%':
#         result = num1 % num2
#         hahaton.write(f' \nПользователь запросил: {num1} % {num2} = {result} ')
#         print(f'{num1} % {num2} = {result}')
#     elif operator == '**':
#         result = num1 ** num2
#         hahaton.write(f' \nПользователь запросил: {num1} ** {num2} = {result} ')
#         print(f'{num1} ** {num2} = {result}')
#     else:
#         print('error')
        
#     cont = input('Would Marselle want to continue? Yes/No ')
#     if cont == 'Yes':
#         print()
#     elif cont == 'No':
#         print()
#         break
#     else:
#         print('error')
#         break
    
# 2 

# users = []

# while True:
#     text = int(input('''
#             1 >>> Зарегистрироваться
#             2 >>> Авторизоваться
#             >>> '''))
#     if text == 1:   
#         login = input('введите свой логин - ')
#         pas = input('введите свой пароль - ')
#         users.append(login)
#         users.append(pas)
#     elif text == 2:
#         login = input('введите свой логин - ')
#         pas = input('введите свой пароль - ')
#         if login not in users or pas not in users:
#             print('НЕПРАВИЛЬНЫЙ ЛОГИН ИЛИ ПАРОЛЬ')
#             continue
#         else:           
#             print('ДОБРО ПОЖАЛОВАТЬ')

# 3

# dict1 = {'a': 5, 'b': 3, 'c': 10, 'd': 15, 'e': 20, 'f':30, 'g': 42, 'h': 50}

# for key in dict1:
#     if dict1[key] % 3 == 0 and dict1[key] % 5 == 0:
#         print(f'{key} - Hi-Bye')
#     elif dict1[key] % 5 == 0:
#         print(f'{key} - Bye')
#     elif dict1[key] % 3 == 0:
#         print(f'{key} - Hi')
#     else:
#         continue

# 4

# counter = 0
# for i in range(1, 1001):
#     if i % 3 == 0 or i % 5 == 0:
#         counter += i
# print(counter)

# 5

# counter = 0
# for i in "4729461084":
#     counter += int(i)
# print(counter)

# 6  Создайте input() который принимает от пользователя дату в формате: "2020-10-24 18:30" и возвращает dictionary разделённую по значениям даты: 
# date = {"year": "2020", "month": "10", .....}""",

# date = {}
# date['year'] = int(input('Введите год - '))
# date['month'] = int(input('Введите месяц (от 1 до 12) - '))
# date['day'] = int(input('Введите день (от 1 до 31) - '))
# date['hour'] = int(input('Введите час - '))
# date['minute'] = int(input('Введите минуты'))

# print(date)

# 7

# !!!!!!!!!!!
# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar',
#             'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor',
#             'слова', 'фраза', 'введите', 'слово', 'кнопку']

# reverse = words[::-1]
# if(words == reverse):
#     print('right')
# else:
#     (words != reverse)
#     print('uncorrect')



# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar',
#             'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor',
#             'слова', 'фраза', 'введите', 'слово', 'кнопку',] 
# palindroms = [] 
# for i in words:
#     if i == i[::-1]:
#         palindroms.append(i) 
#         print(f'слово {i} - палиндром') 
#     else:
#         continue
# print('Эти слова являются палнидромами') 
# print(*palindroms) 

# 8 final:

# cities = []
# while True:
    
#     text = input(''' Выберите действие:
#     1. Добавить новый город
#     2. Отобразить список городов
#     3. Заменить город
#     4. Удалить город
#     5. Выход
#     >>>  ''')

#     if text == '1':
#         new_city = input('Введите название города: ')
#         if new_city in cities:
#             print('Такой город уже есть!')
#         elif new_city.isalpha == False:
#             print('Некорректное название!')
#         else:
#             cities.append(new_city)
            
#     elif text == '2':
#         for i in cities:
#             print(cities.index(i), i)
            
#     elif text == '3':
#         current_city = input('Текущий город: ')
#         replace_city = input('Новый город: ')
#         if current_city not in cities:
#             print('Текущий город отсутствует')
#         elif replace_city in cities:
#             print('Такой город уже есть!')
#         elif replace_city.isalpha() == False:
#             print('Некорректное название!')
#         else:
#             cities.remove(current_city)
#             cities.append(replace_city)
#             print('Город заменен.')

#     elif text == '4':
#         remove_city = input(' Введите название города: ')
#         if remove_city not in cities:
#             print('Текущий город отсутствует.')
#         elif remove_city.isalpha() == False:
#             print('Некорректное название!')
#         else:
#             cities.remove(remove_city)
#             print('Город удален!')

#     elif text == '5':
#         print('Программа завершена!')
#         break