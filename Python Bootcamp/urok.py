# print('Hello, world space')

# for i in range (1, 10, 2):
#     print('*' * i)
# for i in range (11, 0, -2):
#     print('*' * i)

# print('\n'.join
# (
#     [''.join
#         (
#             [
#                 " \U0001F495 \U0001F495 \U0001F495 " [(x-y) % 11]
#                 if((x / 20) ** 2 + (y / 10) ** 2 - 1) ** 3 - (x / 10) ** 2 * (y / 10) ** 3 <= 0 else ' '
#                 for x in range (-30, 30, 1)
#             ]
#         )
#         for y in range(28, -19, -1)
#     ]
# ))


p1 = int(input('Введите пароль: '))
p2 = int(input('Повторите пароль: '))

if p1 == p2:
    if len(p2) >= 8:
        print('Пропускаем') 
        if '123' not in p2:
            password = p2
            print('|*|'.join(password))
            print(p2)
        else:
            print('Ваш пароль слишком простой')
    else:
        print('Ваш пароль должен быть больше 8 символов')
else:
    print('У вас не совпадает пароль.')


