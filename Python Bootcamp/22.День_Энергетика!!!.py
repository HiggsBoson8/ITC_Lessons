# function, функция - специальный вызываемый код 

# процедурный, функциональный, ООП

# append - только для листа, на str нельзя
# shuffle
# update

# def add(x, y):
#     print(f'sum: {x + y}')
# add (2, 3)

# def test() :
#     print('null funk')
# test() 

# def test():
#     return 'Hello Python'
# print(test())

# def test(x = 78, y = 78):
#     return x + y
# print(test(25))

# *args, **kwargs, * = args, kwargs = ** 
# arg - неизвестное количество неименованных аргументов, если поставить * перед именем, его тип list. 
# kwarg - ключевые аргументы, принимает ключ и значения, dictionary
# * - звездочка - 'all', import *, from random import *

# def add(z, y, w):
#     return z + y + w

# def add (*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum 
# print(add(4, 5, 6, 7, 9, 23, 78, 55, 88))

# def add(*qwe): #tuple
#     sum = 0
#     for i in qwe:
#         sum += i
#     return sum
# print(add())

# a = [1, 2, 3, True]
# n = [4,5,*a,6, False] 
# print(n)

# from random import choice 
# def main(*args):
#     list1 = ['Jason', 'Kholhida', 'Sparta', 'Aphrodite']
#     return choice(list1), choice(args)
# print(('25','24','23','22'))

# from random import choice
# def main(*args):
#         names = ['Miras', 'Stas', 'Abay', 'Darkhan', 'Abilaykhan', ' Gulzim', 'Roman', 'Alibek', 'Marselle', 'Adi']
#         return choice(names), choice (args)


# set1 = {1,2,3,4,5,6,7,8}

# set2 = set(list1)
# list2 = list(set2)

# # print(list1)
# print(list2)
#1: генерация пароля 2: отправляет пароль 3: спрашивает 4: проверка 5: True or False 

# import random 
# def message(*args):
#     password = [] 
#     for i in args:
#         num1 = random.randint(0, 9) 
#         password.append(num1) 
#     print(password) 
# message(12) 
        
        
# num_code = [1,2,3,4,5,6,7,8,9,0]
#     for i in range(size_pass):
#         password.append(choice(list1))
#     for j in range(6):
#         if len(code) >= 6:
#             break
#         code.append(choice(num_code))
#     return password, code


# size_password = int(input('pass size: '))
# end_pass = main(size_password, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')


# baza = {}

# import random
# def generic_password(letters = 4, numbers = 4, symbols = 4):
#     alph = 'qwertyuiopasdasdfghjklzxvbnm'
#     num = '1234567890'
#     symbol = '!@#$%^&*'
#     password = []
#     letters = int(input('How many letters do you want: '))
#     numbers = int(input('How many numbers do you want: '))
#     symbols = int(input('How many symbols do you want: '))

#     for i in range(1, letters + 1):
#         password += random.choice(alph)
#     for i in range(1, numbers + 1):
#         password += random.choice(num)
#     for i in range(1, symbols + 1):
#         password += random.choice(symbol)
#     # print(password)
#     # print(random.shuffle(password))
#     random.shuffle(password) 
    
#     password_string = ''
#     for i in password: 
#         password_string += i
#     print(password_string)
# # generic_password()

# def code_check(login, password2):
#     num = ['1','2','3','4','5','6','7','8','9','0']
#     code = ''
    
#     for i in range[1, 7]:
#         code += random.choice(num)
#         # return int(code) 
# # print(code_check())

# while True:
#     table = int(input('''
#     register 1
#     authorisation 2
#                       '''))
    
#     if table == 1:
#         login = input('login: ')
#         password2 = generic_password()
#         code = code_check()
#         print(code)
#         try:
#             inpcode = int(input('code: '))
#         except ValuError:
#             print('пиши код в цифрах')
#         else:
#             while inpcode != code:
#                 print('повторите ввод кода')
#                 inpcode = int(input('code: '))
#             else:
#                 print('ты зарегистрирован')
#                 baza.update({
#                     'login: login'
#                     'password': password2
#                 })
#                 print(baza)
#     elif table == 2:
#         login = input('login: ')
#         password2 = input('Введите password: ')
#         if login in baza.values:
#             if password2 in baza.values:
#                 print('вы авторизованы')
#             else:
#                 print('не верный пароль: ')
#         else:
#             print('у нас нет такого пользователя')
#     else: 
#         print('убедитесь что вы ввели правильную команду ')
        


# from random import choice
# def main(size_pass: int, *list1):
#     password = []
#     code = []
#     num_code = ['1','2','3','4','5','6','7','8','9','0']
#     for i in range(size_pass):
#         password.append(choice(list1))
#     for j in range(6):
#         if len(code) >= 6:
#             break
#         code.append(choice(num_code))
#     return password, code
# size_password = int(input('pass size: '))
# end_pass = main(size_password, '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
# passs = ''.join(end_pass[0])
# code = ''.join(end_pass[1])
# print(passs, code)        
        

        
# a = 1
# b = 2
# print(a + b)

# def add(a, b):
#     # print('hi')
#     return a + b

# def minus(a = 1, b = 2):
#     # print('asd')
#     return a + b
# # add(2,1)
# print(add(2,1))
# print(minus(5, 5))

# a = [1,2,3]
# b = [*a, 4,5,6]
# print(a)
# print(b)

# def test(*args):
#     return args 
# print(test(a))
# a = {1,2,3,4,5,6}
# b = ([1,2,3,4])

# list1 = [1,2,3,4,5,6,7,8, 8, 4, 6]
# # set1 = {1,2,3,4,5,6,7,8}

# set2 = set(list1)
# list2 = list(set2)

# # print(list1)
# print(list2)


# HOMEWORK:

# os.system('ls > ls.txt')

# list_ls = []
# list_code = ['py','html','txt','css']

# with open('ls.txt', 'r') as f:
#     f = f.read()
#     for i in f.split():
#         list_ls.append(i)
    
#     for passes in list_ls:
#         for j in passes.split('.'):
#             if j in list_code:
#                 os.system(f'mv {passes} /home/marselle/Рабочий\ стол/def\ main/lessons2')



# def file_passes():
#     list_file = ['Загрузки','Видео','Музыка','Рабочий\ стол','Изображения']
#     for i in range(1):
#         for passes in list_file:
            
#     os.system('cd')
#     time.sleep(1)
#     os.system(f'cd {passes}')
#     time.sleep(1)
#     os.system('ls > list.txt')
        
        
# import os, time
        

# def download_passes():
#     list_file = []
#     list_expansion = ['png', 'jpg', 'jpeg']
#     os.system('cd /home/marselle/Загрузки')
#     os.system('ls /home/marselle/Загрузки > /home/marselle/Рабочий\ стол/def\ main/list.txt')
#     time.sleep(1)
#     with open('list.txt', 'r') as file:
#         ls_download = file.read()
#     for name_file in ls_download.split():
        
#         print(name_file)
        
        
#     for items in ls_download.split('.'):
#         p = items.split()
#         if p in list_expansion:
#             os.system(f'mv {items} /home/marselle/Изображения')
#         else:
#             continue
            
                
#             # if item in list_expansion.split('.'):
# print(download_passes()) 
























