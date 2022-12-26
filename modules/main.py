# (19.12.2022)

# from core import config as file

# print(file.name, file.age)
# # print(config.age)

# print(f'name is {file.name} and your age is {file.age}') 

# import data #импортируем полностью

# print(data.a)

# from data import a, b #только импортируем переменную а

# import data
# print(data.a)
# print(data.b)

# x = data.a
# y = data.b

# print(x) 
# print(y)

# from tkinter import *   # * - выделить все
# from tkinter import ttk  # ttk - функция
# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# import random  # - генерирует рандомные числа, делает все рандомно

# a = random.randint(0, 1000) # random integer
# b = random.random() # - генерация дробных чисел
# list1 = [1, 2, 3, 4, 45, 8, 89, 'astronaut', True, False]
# list2 = random.choice(list1)
# print(list2)

# import datetime  # - показывает число в терминале

# a = datetime.datetime.now().strftime('%y %m %d')
# a = datetime.datetime.now().time()
# print(a)


# import os  # - исполнить команду терминала

# os.system('clear')
# os.system('ls')
# os.mkdir('Test')
# print(os.getcwd())

# import sys # - модуль sys используется для влияния на Python Интерпретатор.(не используется)

# print(sys.builtin_module_names)

# import calendar # - просто календарь

# print(calendar.calendar(40000))
# print(calendar.weekday(2022,12,31))
# print(calendar.isleap(2000))

# import time  # - просто время

# print('Astronaut')
# time.sleep(8)
# print(time.timezone('Asia/Almaty'))
# print(time.ctime())

# try and except #except - реагирует на ошибки

# try:
#     zero = 10/0
# except ArithmeticError:
#     print('На ноль делить нельзя')
    
# try:
#     z = 'hi' + 'astronaut'
# except:
#     print('error')
# else:
#     print('correct')
    
# try:
#     num = float(input('input number: '))
#     print('number')
# except:
#     print('convertation:') 
# finally:
#     print('End program')

# f = open('modules/test.txt', 'r')
# ints = []
# astronaut = []
# try:
#     for line in f.read():
#         ints.append(int(line))
#         astronaut.append(line.isastronaut())
# except:
#     print('Это не число ', astronaut)
# else:
#     print('All is ok')
# finally:
#     f.close()
#     print('End program')
# print(ints)

# 1)Внутри my_module.py создайте вызваннную print которая выводит текст "Я функция из my_module.py". А затем импортируйте my_module.py в другой файл, и вызовите его.

# import data
# print(data.a) 

# 2)Вам дан список имён names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"], вытащите 4 рандомных имени оттуда и сохраните в другой список.


# import random
# whoareyou =["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
# # print(random.choice(whoareyou))
# a = random.choice(whoareyou)
# print(a)


# 3)Узнайте какая у вас операционная система с помощью модуля sys и выведите на экран имя опрационной системы.

# import sys
# print(sys.platform)

# 4)Через терминал передайте Python несколько аргументов, а затем выведите их на экран.

# import os
# os.system('clear')

# 5) Через Python у себя на рабочем столе создайте директорию, а внутри дериктории создайте 5 РАНДОМНЫХ файлов. 

# import random
# import os

# os.system('mkdir astronaut')
# os.syste('cd mars')

# a = ['a', 'b', 'c', 'd', 'e']

# for i in range(5):
#     random.sample(a, 5)

# os.system(f'touch {}')    

# 6)Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.

# whoareyou =["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]