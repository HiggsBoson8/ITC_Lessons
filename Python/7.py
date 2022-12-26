# удаление четных/нечетных индексов вручную
# mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# for i in range(1, 5):
#         mylist.pop(i)
# print(mylist) 

# удаление четных/нечетных индексов 
mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for i in range(1, len(mylist) // 2 + 1):
    mylist.pop(i)
print(mylist) 

# ['e', 'f', 'g', 'h', 'a', 'b', 'c', 'd'] первые 4 элемента переместить назад 