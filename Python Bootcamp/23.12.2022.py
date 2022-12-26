# Web, CRM, robotics, AI/AR
# Django = web development 



# global - опреление переменной для всей программы
# local - обычное состояние программы

# map - дефолтная функция пайтона

# lambda - анонимная функция

# iterating types, итерация - изучить на практике! 

#  документация пайтона

# def main(x, y):
#     return x + y
# print(main(1, 1))
# l = lambda *a: set(a) 
# print(l(1,2,3,4,5))

# ---------------------------------------------------------------

def operator(num1, num2):
    operator = input("Enter and operator: (+ - / * % **): ")
    if operator == "+":
        result = num1 + num2
        print(result)
    elif operator == "-":
        result = num1 - num2
        print(result)
    elif operator == "/":
        result = num1 / num2
        print(result)
    elif operator == "*":
        result = num1 * num2
        print(result)
    elif operator == "%":
        result = num1 % num2
        print(result)
    elif operator == "**":
        result = num1 ** num2
        print(result)
    else: 
        print("error")
while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator(num1, num2)
    cnt = input('Do you want to continue? Yes/No: ')
    if cnt == 'Yes':
        print() 
    elif cnt == 'No':
        print('End of the program.')
        break
    else:
        print('error')
        break

# ---------------------------------------------
# while True:
#     num = int(input('num1 '))
#     num2 = int(input('num2 '))
#     table = input('''
#     +       1              
#     -       2       
#     *       3
#     /       4
#     **      5
#     //      6
#     >:    ''')
#     if table == '1':
#         res = lambda x, y: x + y
#         print(res(num, num2))
#     elif table == '2':
#         res = lambda x, y: x - y
#         print(res(num, num2))
#     elif table == '3':
#         res = lambda x, y: x * y
#         print(res(num, num2))
#     elif table == '4':
#         res = lambda x, y: x / y
#         print(res(num, num2))
#     elif table == '5':
#         res = lambda x, y: x ** y
#         print(res(num, num2))
#     elif table == '6':
#         res = lambda x, y: x // y
        
#     elif table == '7':
#         res = lambda x, y: x % y
#         print(res(num, num2))
#     else:
#         print('error')
#         break


# alternative calculator
# def calculate(num, num2):
#     while True:
#         table = input('''
#         5 * 5 = 25
#         +      1
#         -      2
#         *      3
#         **     4
#         /      5
#         //     6
#         %      7
#         >: ''')
#         if table == '1':
#             rez = lambda x, y: x + y
#             print(rez(num, num2))
#             calculate(int(input('num1 ')), int(input('num2 ')))
#         elif table == '2':
#             rez = lambda x, y: x - y
#             print(rez(num, num2))
#             calculate(int(input('num1 ')), int(input('num2 ')))
# calculate(int(input('num1 ')), int(input('num2 ')))
        

# a = [1,2,3,4]
# l = lambda x: x ** x, a
# print( l ) 


# a = [1,2,3,4]
# l = list(map(lambda x: x * x, a))
# print( l )


# l = list(map(lambda x: x % 2 == 0, [1,2,3,4]))
# print(l) 


# def ma():
#     m = '12' #local
#     return m


# Задача. Вам будет предоставлен массив чисел. Вы должны сортировать нечетные числа в порядке возрастания, оставляя четные числа на их исходных позициях.
# Примеры
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# def main(lists):
#     for i in range(0, len(lists)):
#         for f in range(i, len(lists)):
#             if (lists[i] % 2 == 1 and lists[f] % 2 == 1):
#                 if (lists[f] < lists[i]):
#                     num = lists[i]
#                     lists[i] = lists[f]
#                     lists[f] = num
#     return lists
# print(main([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))


# Итерация
a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
o = [i for i in a if i%2]
e = [i for i in a if not i%2]
h = [0 if i%2 else 1 for i in a]
print(h)
print(o)
print(e)
for i in range(len(a)):
    h[i] = e.pop(0) if h[i] else o.pop(0)
print(h)




