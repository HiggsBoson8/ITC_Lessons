# def - def1 - def2

# #git init 
# import os
# os.system('clear')

# # a = 5
# # b = 5
# #print(a + b)

# def len1(a):  #def - функция
#     n = 0
#     if a.isalpha():
#         for i in a:
#             n += 1
#     return n 

# print(len1('asdfghjk'))

# a = int(input: ())
# b = 1
# print(a + b)

# def adi(b, a = 10):
#     return a + b

# print(adi(6, 8))


# def calculator(oper, x, y):
#     if oper == '+':
#         return x + y
#     elif oper == '-':
#         return x - y
#     elif oper == '*':
#         return x * y
#     elif oper == '/':
#         return x / y
#     return 'Choose another operation: '
#     # else:
#     #     return 'Choose another operation: '

# print(calculator('+', 1,2))


# 1) # 1 Функция, заполняющая список числами. Напишите функцию, которая заполняет список случайными числами в указанном количестве и в пределах заданных границ значений. 
#   Реализуйте код вызова этой функции.

# from random import randint
# def random_int(num_list: list, size_list: int, min_n: int, max_n: int):
#     for i in range(size_list):
#         num_list.append(randint(min_n, max_n))

# n = []
# minint = int(input('minint: '))
# maxint = int(input('maxint: '))
# size_l = int(input('size_list: '))
# random_int(n, size_l, minint, maxint)
# print(n)

# 2)Функции Фибоначчи. Примеры двух функция для ряда Фибоначчи. Первая функция принимает номер элемента ряда и возвращает его значение. 
# Вторая функция принимает номер элемента и выводит на экран весь ряд Фибоначчи до элемента с заданным номером включительно.

# start = int(input('starting: '))
# def chislo_fib(num): #num - аргумент
#     start, b = 0, 1
#     for i in range (num):
#         yield start  #yield - команда универсальная
#         start, b = b, start + b 
# print(list(chislo_fib(start)))

# def fibonaci1():
#     fib1 = fib2 = 1
#     n = input("Номер элемента ряда Фибоначчи: ")
#     n = int(n) - 2
#     while n > 0:
#         fib1, fib2 = fib2, fib1 + fib2
#         n -= 1
#     print("Значение этого элемента:", fib2)

# def fibonaci2():
#     fib1 = fib2 = 1
#     n = int(input('Введите номер элемента последовательности: '))
#     print(fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')

# fib1 = 1
# fib2 = 1
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
# print("Значение этого элемента:", fib2)

#3)В строке изменить последовательность слов на обратную. Напишите функцию, которая принимает строку слов и возвращает строку с теми же словами,но идущими в обратном порядке.

# def reverse_text(text):
#     text = text.split()
#     text.reverse()
#     return ' ' .join(text)

# print(reverse_text(input('Введите текст: ')))

# 4)Заполнение массива случайными числами. Заполнить список случайными целыми числами и вывести на экран. (С помощью функции)

# from random import randint 
# def random_num(l: list, s_l: int):
#     for i in range(s_l):
#         l.append(randint(1,100))
#     return l 
# list_num = []
# size_list = int(input('size: '))
# print(random_num(list_num, size_list))

# from random import randint
# def random_num(max_num = 100):
#     l = []
#     for i in range(max_num):
#         l.append(randint(1,max_num))
#     return l
# max_num = int(input("size "))
# print(random_num(max_num))




