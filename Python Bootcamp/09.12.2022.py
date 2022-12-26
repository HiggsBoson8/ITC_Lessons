# int
# str
# boolean
# float
# tuple
# print() len() type input
# var.method()


# a = ('hello' ,)
# print(type(a))

# list1 = ['Hello', 78, 2.31, True, False, 'qwerty']
# print(list1)
# list2 = list()
# list3 = []
# # ERROR tuple1 = ()
# tuple1 = ()

# print(tuple1)
# print(type(tuple1))
 
# slice - срезы
# [start:stop:step] SSS

# print(list1[: : -1]) реверсе
# print(list1[:4 : -1])

# user1 = input('input: ')
# if user1 == user1[: : -1]:
#     print(True)
# else:
#     print(False)

# user2 = input('input: ')
# if user2 == user2['input word: ']
# if user2 == user2[: : -1]:
#     print(True)
# else:
#     print(False)


# append добавляет в конце элемент
# list1 = ['Hello', 'world', 'Astana', False]
# list1.append(True)

# remove удаляет элемент
# list1.remove(False)

# extend
# list1.extend('789')

# pop 
# list1.pop(0)

# list1.count(False)

# print(list1.index(0))

# print(list1.clear())

# a = (list1.reverse()) массив задом наперед
# print(a, list1)

# условие if чередовать с реверсом

#  import timeit
#  list_test = timeit.timeit(stmt="(1,2,3,4,5')", number = 1000)
#  print(list_test)
 
#  не изменяемый

#   Пользователь вводит имя файла. Проверить, находится ли расширение файла в списке допустимых.

# print('select type of the file: ')
# list1 = ['png', 'jpg', 'jpeg', 'gif', 'svg']

# user = input().split('.')
# if user[0] in list1:
#     print(True)
# else:
#     print(False)

# 0) Создать список и 5 вложенных кортежей.
# space = []
# space.append(('qwe', 12, 45, 98, 90))
# print(space)
# 
# for i in range (6):
# #     array.append(12)
# # print(array)
# [8, 1]f[9, 2]l

# [8,9, 1, 2]
# 1) Создать Tuple из 3 элементов и вывести каждый из них по индексу.
# astra = [23, 90, 18]

# print(astra.index((90)))

# # 2) Создать Лист и заполнить его 5 РАЗНЫМИ ТИПАМИ ДАННЫХ.
# tesla = []
# tesla.append((123, 'asd', True, 3.14, (25, )))
# print(tesla)


# 3) 1.Создать Лист из 5 разных имён. 2.Создать пустую строку и через .join() соеденить пустую строку и все имена в списке.

# list1 = ['Joe', 'Rte', 'Anny', 'Molly', 'Ali']
# srt1 = ', '.join(list1)
# print(srt1)




# 4) Создать 2 списка(List) заполнить данными, к первому списку добавить все объекты второго списка
# tesla1 = ['asd', 12, 24, 36]
# tesla2 = ['qwe', 18, 30, 48]
# tesla3 = tesla1 + tesla2
# print(tesla3)

# tesla1 = ['asd', 12, 24, 36]
# tesla2 = ['qwe', 18, 30, 48]
# tesla1.append(tesla2)
# print(tesla1)

# 5) Взять Лист №1 из Google Colab и посчитать сколько раз там встречается имя "Jack".
# name_list = ['Marselle', 'Jack', 'Roman', 'Abay', 'Jack', 'Ali', 'Jack', 'Abay', 'Madina']
# print(name_list.count('Jack'))


# 6) Удалить из Листа №1 объект "Oskar"
# name = ['Anonim', 789, 'Oscar']
# name.remove('Oscar')
# print(name)


# 7) Создать пустой лист. Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.
# guitarist = []
# guitarist.append('Abay')
# guitarist.append(1995)
# guitarist.append('Python')
# print(guitarist)
# 8) Взять Лист №2 из Google Colab узнать индекс объекта(строки) "loop" и удалить его по индексу
# astronaut = ['Bob', 'Acer', 'loop']
# print(astronaut.index('loop'))
# astronaut.pop(2)
# print(astronaut)


# 9) Взять Лист №3 из Google Colab и посчитать произведение этих чисел т.е. умножить их все и вывести результат.

# astronaut = [2, 4, 6, 8]


# 10) Взять строку №1 создать два списка numbers и letters, пройтись по каждому элементу строки №1 и в numbers добавлять только числа, а в letters буквы

# numbers = [1, 2, 3, 4, 5, 6, 7]
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# # NL = numbers + letters
# # print(NL)
# # LN = numbers + letters
# # print(LN)
# numbers.append(letters)
# print(numbers)
# letters.append(numbers)
# print(letters)


# 11) Взять Лист №2 и вывести объекты с 1 по 3 индекс
# astronaut = ['cat', 'Back', 'Echo', 'Charlie', 'Singularity', 'Lennon']
# print(astronaut[1:3])

# 10?!
# list1 = []
# list2 = []
# while True:
#     print(list1)
#     print(list2)
#     table = input('1.текст: \n2.цифры:  \n>> ')
#     if table == '1':
#         a = input('Ввести текст: ')
#         list1.append(a)
#     elif table == '2':
#         b = input('Ввести цифры: ')    
#         list2.append(b)
#     else:
#         print('Такой команды нет.')
#         break
