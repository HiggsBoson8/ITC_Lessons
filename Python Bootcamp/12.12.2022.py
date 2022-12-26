# dictionary {}
# set [list]

# # di = {}#dic
# # f = dict()#dic

# n = {"name" : "Ali",
#     "age" : 3
# }
# # print(n)
# # print(n["name"], n["age"])

# # print(n.keys())# -  выводит ключи
# # print(n.values())# - выводит значения
# # print(n.items())# - выводит все

# # print(n.pop("name"))

# # n.popitem()#-удаляет последний элмент 
# # print(n)


# f ={"fff" : "ddd"}
# n.update(f)# обьединяет словари 
# print(n)

# # a = n.fromkeys("d", 123)
# # print(a)


# m = {"x" : 4, "y" :4 }
# # m.setdefault("z", 123)# - добавляет ключь и значение 
# # print(m)


# # m[1]= 1234# добавляет новые значения в словарь 
# # print(n)

# n=m.copy()# - копирует данные в переменной n
# print(n)

# ---------------------

# изменяемый тип данных и не изменяемый тип данных: frozen.set & set

# .add("*") - Добавляет элемент в множеcтво

# .remove("*") - Удаляет объект из множества

# .clear() - Удаляет всё внутри множетсва.

# .difference("*") - Сравнивает оригинальное множество с * и возвращает объекты которых нет в *

# .update("*") - Добавляет в множетсво всё что вы передали в UPDATE()

# .discard("*") - Удаляет * из множетсва, если * нету во множестве, ошибки не будет как если бы это было remove()

# .intersection("*") - Возрвращает объекты которые есть и во множестве и в *.

# .intersection_update(*) - Удаляет из множетсва непохожие и оставляет только те объекты которые есть и во множестве и в *

# .pop() - для удаления в dictionary, мы используем вместо индекса в названии ключа
# .pop() - удаление по индексу
# .pop в set удаляет рандомно
# .remove() - удаление по элементу


# a = {'x':4, 'y':5}
# m.setdefault('z', '123')
# print(m)

# a = {'x':4, 'y':5}
# b = a.copy()
# b['123'] = 123
# print(a)
# print(b)

# frozenset - изменяемый тип данных
# a = {'name', 123, 321, 'name', True, False, False}
# b = frozenset([1, 2, 3, 4])
# print(b)

# .isdisjoint - пересекание, если пересекается - True
# a.union(b) = a | b
# # a.intersection(b) = a & b
# a = {'name', 123, 321, 'name', True, False, False}
# b = ['name', 123, 321, 'asd']
# c = {'1', '13'}
# print(c.isdisjoint(a))
# print(b.isdisjoint(a))

# print(a.union(b))
# print(a | b) 

# print(a.intersection(b)) 
# print(a & b)

# print(a.difference(b))
# print(a - b)
# print(b - a)

# print(a.symmetric_difference(b))

# 0)Из множества № 1 в Google Colab - удалите число 7.
# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# a.remove(7)
# print(a)

# 1) Hайти объекты которые есть и в SET №2 и в SET №3 из Google Colab

# a = {'god', 'motor', 'abay', 88, 'cosmos', 'jarhead', 'zaga'}
# b = {'lesson', 88, 'inter', 'marselle', 'name', 'jarhead', 'motor'}

# print(a.intersection(b))

# # 2) В SET №3 из Google Colab найдите объекты которых нет SET №2
# a = {'god', 'motor', 'abay', 88, 'cosmos', 'jarhead', 'zaga'}
# b = {'lesson', 88, 'inter', 'marselle', 'name', 'jarhead', 'motor'}
# print(a.difference(b))

# 3) Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент. А затем удалите через .pop() элемент и посмотрите что же вы удалили.

# astronaut = {'asd', 'head', 'camp', 'metal', 'echo'}
# astronaut.add('god')
# print(astronaut)
# k = astronaut.pop()
# print(k)

# !!!! set - не содержит дубликатов(удаляет) !!!!
# 4) Problem 000: Из Dictionary №1: Добавьте в меню 'besh_barmak' который стоит  130 сом. Оказалось лагман слишком дешевый. Обновите цену на 135. Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо. Удалить borsh
# DICTIONARY
# menu = {'lagman', 'steak', 'borsch', 'vegan'}
# menu = {
#     'besh_barmak': 130, 
#     'fish': 100,
# }
# menu['fish'] = 110
# menu['borsch'] = 150
# menu.pop('besh_barmak')
# print(menu) 

# 5) Problem 10: Из Dictionary №1: Добавьте в меню напитки как ключ "drinks", А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.

# menu = {
#     'drinks': 250
# }
# menu['juice'] = ['cola', 'fanta', 'sprite'] # значение словаря(dict) = лист
# print(menu)

# 6) Problem 020: Создайте SET который хранит в себе все методы  для работы  с  SET. Создайте второй SET который хранит в себе  методы  для работы  с  Dictionary которые вы сегодня узнали. Проверьте какие методы похожи у этих типов данные.

# astronaut = {'vakuum', 'dark', 'mattery', 'black', 'hole', 'planet', 'volcano'}
# earth = {'mountain', 'ocean', 'planet', 'volcano', 'aussie', 'land'}
# print(astronaut.difference(earth))
# print(earth.difference(astronaut))


# 7) Problem 31: Создайте пустой словарь. Запустите цикл который 3 раза спросит его имя и его пароль. Записывайте имя пользователя как ключ, а пароль как его значение.

# account = {}
# name = input('put the name: ')
# account[name] = input('put the password: ')
# print(account) 
# name2 = input('put the name: ')
# account[name] = input('put the password: ')
# print(account) 
# name3 = input('put the name: ')
# account[name] = input('put the password: ')
# print(account) 

# 8) Problem 27: Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия. С помощь цикла for пройти вывести на экран строку: "Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

# names = {}
# for i in range(1, 2):
#     name = input('Put the name: ')
#     profession = input('Profession: ')
#     print(f"Здравствуйте {name}! Прекрасная профессия {profession}!")
#     name2 = input('Put the name: ')
#     profession2 = input('Profession: ')
#     print(f"Здравствуйте {name2}! Прекрасная профессия {profession2}!")
# print(names)

# d = {}
# for i in range(1,2):
#     name = input('Введите имя: ')
#     prov = input('Введите профессию : ') 
#     d[f'{name}'] = prov   
#     name2 = input('Введите имя 2: ')
#     prov2 = input('Введите профессию 2: ') 
#     d[f'{name2}'] = prov2
# print(d)

# 9) Problem 22: Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET. Сделайте так чтобы эти данные уже никто не смог поменять позже.
# d = {1,2}
# for i in range(1, 11):
#     numbers = int(input('Put the numbers: '))
#     d.add(numbers)
# print(d)


# 10) Problem 11: Есть список Южноамериканских стран Google Colab - СПИСОК №2 в котором Суринам встречается два раза. Необходимо написать программу, которая удалит дублирующуюся запись, и возвратит в результате список.

# a = ['Argentina', 'Surinam', 'Cuba', 'Brasile', 'Surinam']
# a = set(a) #Убирает дубликаты, переводит в {}
# a = list(a) #Переводит в '[]'
# print(a)

# 11) Problem 101: Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст: suitcase = []. Однако он может вместить всего 5 вещей. Положите 5 вещей в чемодан. Вы передумали, и решили убрать последнюю вещь. 

# suitcase = [] 
# a = input('Things: ')
# b = input('Things: ')
# c = input('Things: ')
# d = input('Things: ')
# e = input('Things: ')
# f = input('Things: ')
# suitcase.append(a)
# suitcase.append(b)
# suitcase.append(c)
# suitcase.append(d)
# suitcase.append(e)
# suitcase.append(f)
# if len(suitcase) >= 5:
#     print('Больше 5 нельщя')
#     print(suitcase)
#     suitcase.pop(5)
#     print(suitcase)

# h = []
# for i in range(1,7):
#     h.append(i)
# if len(h) >= 5:
#     print('No more than 5 things')
#     print(h)
#     h.pop(5)
#     print(h)
    

# 12) Problem 001: Из Google Colab Множество 4 и 5. Напишите код, который: Выведет новое множество, которое есть как в первой ферме, так и во второй.



# 13) Problem 100: Из Google Colab Множество 4 и 5. Напишите код, который выведет новое множество, состоящее из животных, которые есть во второй ферме, но нет в первой.



# for i in range (1, 10, 1):
#     print('*' * i)
# for i in range (10, 0, -1):
#     print('*' * i)
