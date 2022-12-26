# аргумент
# параметры
# объекты в функции

# lists = [1,2,3,4,5,6]
# a = [*lists, 4,5,6]
# print(a)


# def test(name, *a):
#     return f"Привет {name} у тебя прикольные животные {a}"
# print(test('marselle', ['кошка', 'собака', 'черепаха']))


# def kwargs(**kwargs):
#     return kwargs.keys() #keys & items
# print(kwargs(name='marselle', age = 19, animals = [1,2,3,4]))


# a = {
#     'name': 'marselle',
#     'age': 19,
#     'animals': [1,2,3,4]
# }
# print(a.items())    


# 7  # 1*2*3*4*5*6*7 = 7!
# def test(a):
#     a += 1
#     print(a)
#     return test1(a)
# def test1(a):
#     a += 1
#     print(a)
#     return test(a)
# print(test(1))


# def test2():
#     return test2()
# test2()


# def defind_factorial(num):
#     if num == 1:
#         return num 
#     else:
#         return num * defind_factorial(num - 1)
# print(defind_factorial(5))


# def object_function():
#     return f'Привет'
# hello_name = object_function()
# print(hello_name) 


# def main_decorator(func):
#     def decor1(): 
#         a = input('name: ')
#         func()
#         return a
#     return decor1

# @main_decorator 
# def hello_name():
#     for i in range(1,100+1):
#         print(i)

# print(hello_name)
# print(main_decorator(hello_name))
# get_main = main_decorator(hello_name)
# get_main()

# def hello_name():
#     print('1234567890') 
# hello_name2()


# def get_main(food):
#     def get_decorator():
#         food('суп')
#         print('овощи, мясо, соль, приправа, морковь ...')
#         print('Bon appetite!')
#     return get_decorator 

# @get_main
# def main(a):
#     print(f'Вкусный {a}:')
# main()


# def get_main(name_peope):
#     def get_decorator(last_name, first_name):
#         print(f'Hello {last_name} {first_name}')
#         name_people(last_name, first_name)
#     return get_decorator

# @get_main
# def name_people(last_name, first_name):
#     print(f'Меня зовут {last_name} {first_name}')
# name_people('naz')


# a = lambda x: x*x
# print(a(5))
# a = lambda x: (x*x)(5)
# print(a)

# 1) Написать lambda которая принимает 3 параметра и умножает все параметры между собой. Функция должна вернуть строку: "Объём бассейна " и значение которое получилось.

# app = lambda x,y,c: x*y*c 
# print(f'Объем {app(4,5,6)} ')

# 2) Написать lambda которая получает сколько дней ПРОШЛО с нового года как параметр и говорит пользователю сколько дней ОСТАЛОСЬ до нового года.

# import datetime
# day = 31
# mouth = 12
# year = 2022
# day1 = datetime.datetime.now().strftime('%d %m %y')
# print(day1)

# def new_year(d,m,y):
#     import datetime
#     d1 = datetime.datetime.now().strftime('%d')
#     m1 = datetime.datetime.now().strftime('%m')
#     y1 = datetime.datetime.now().strftime('%y')
#     print(d1, m1, y1)
#     return f'До нового года осталось {d - int(d1)}d {m - int(m1)}m {y - int(y1)}y'
# print(new_year(31, 12, 2022)) 


# 3) Напишите программу которая выводит только нечётные числа с помощью рекурсии.

def main(number):
    a = []
    for i in range(number):
        if main(number) % 2 == 0:
            main(number - 1)
            continue
        else:
            a.append(main(number))
    return a    
print(main(20))

# def main(a , n=1):
#     if n>a:
#         return
#     else:
#         print(n, end=' ')
#         main(a,n+2)
# main(30)
    
# number = int(input('Enter the number: '))
# if number % 2 == 0:
#     print('Even number')
# elif number % 2 == 1:
#     print('Uneven number: ')
# else:
#     print()


